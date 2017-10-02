#!/usr/bin/env python
# license removed for brevit
import rospy
import roslib
import serial
import time
import argparse

from serial import SerialException
from LOMAS_ROS_pkg.msg import machine_status
from std_msgs.msg import *


# Settings
#IsInSimMode = True


# Global var
status = machine_status()
last_status = machine_status()
#port = "/dev/ttyUSB0"
#path = "/media/gcode/"

# Defining publisher
pubMachineStatus = rospy.Publisher('LOMAS_MachineState', machine_status, queue_size=10)

status.ErrorNr = 0
last_status.ErrorNr = 99
update = False

def loadParameters():
    global IsInSimMode
    
    IsInSimMode = rospy.get_param('~sim_port', True)
    port = rospy.get_param('~port', "/dev/ttyUSB0")
    path = rospy.get_param('~path', "/media/gcode/")
    print 'Param values'
    print IsInSimMode
    print port
    print path

def connectToMachine():
    global s
    global port
    global status
    global update
    global pubMachineStatus
    # Open serial port
    #s = serial.Serial('/dev/ttyACM0',115200)
    print 'Opening Serial Port'
    if IsInSimMode: 
        print 'Serial port will be simulated'
        status.ErrorNr = 0   
    else:
        try:
            s = serial.Serial(port,115200)
            # Wake up
            s.write("\r\n\r\n") # Hit enter a few times to wake the Printrbot
            time.sleep(2) # Wait for machine to initialize
            s.flushInput() # Flush startup text in serial input
            status.ErrorNr = 0
            print 'Serial port connected to machine'
        except SerialException:
            status.ErrorNr = 98
            print 'Error when opening Serial Port'
        

    pubMachineStatus.publish(status)

def sendSerialCmd(cmd):
    global s

    if IsInSimMode:
        grbl_out = 'oMGok\n' 
    else:
        s.write(cmd) # Send g-code block
        grbl_out = s.readline() # Wait for response with carriage return
    
    print ' : ' + grbl_out.strip()
    
    if grbl_out == 'oMGok\n':
        return True
    else:
        return False

    

def sendGCodeCmd(cmd):
    global status

    status.SequensStarted = True
    status.MachineMoving = True
    status.SequenseNr = 99

    pubMachineStatus.publish(status)
    
    ok = sendSerialCmd(cmd)

    if ok:
        status.ErrorNr = 0
        status.SequensStarted = False
        status.MachineMoving = False
        status.SequenseNr = 0

        

def cmdCallback(data):
    global status
 
    if data.data == 99:
        print 'Starting to home robot'
        status.IsSynced = False
        sendGCodeCmd('G28 X Y' + '\n')
        status.IsSynced = True

    elif data.data == 90:
        print 'Man. pos X'
        sendGCodeCmd('G91\n'+'G0 X10 F1000\n')
    elif data.data == 91:
        print 'Man. neg X'
        sendGCodeCmd('G91\n'+'G0 X-10 F1000\n')
    elif data.data == 92:
        print 'Man. pos Y'
        sendGCodeCmd('G91\n'+'G0 Y10 F1000\n')
    elif data.data == 93:
        print 'Man. neg Y'
        sendGCodeCmd('G91\n'+'G0 Y-10 F1000\n')
    elif data.data == 94:
        print 'Man. pos X pos Y'
        sendGCodeCmd('G91\n'+'G0 x10 Y10 F1000\n')
    elif data.data == 95:
        print 'Man. neg X pos Y'
        sendGCodeCmd('G91\n'+'G0 X-10 Y10 Y10 F1000\n')
    elif data.data == 96:
        print 'Man. pos X neg Y'
        sendGCodeCmd('G91\n'+'G0 X10 Y-10 Y10 F1000\n')
    elif data.data == 97:
        print 'Man. neg X neg Y'
        sendGCodeCmd('G91\n'+'G0 X-10 Y-10 Y10 F1000\n')

    pubMachineStatus.publish(status)
    print data




def main():
    global status
    global last_status
    global update

    # Subscribe for teleoperations
    rospy.Subscriber("LOMAS_MachineCmd", std_msgs.msg.UInt8, cmdCallback)
    rospy.loginfo("Starting up machine node")

    rospy.init_node('machine', anonymous=False)

    loadParameters()
    connectToMachine()

    print 'Machine is waiting for command..'

    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        #if update:
            #pubMachineStatus.publish(status)
            #last_status = status
            #update = False

        rate.sleep()
        #print("been here!")

    if IsInSimMode == False:
        s.close()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
	pass