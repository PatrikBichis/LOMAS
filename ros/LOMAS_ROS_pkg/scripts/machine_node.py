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

status = machine_status()
last_status = machine_status()
port = "/dev/ttyUSB0"
path = "/media/gcode/"

# Defining publisher
pubMachineStatus = rospy.Publisher('LOMAS_MachineState', machine_status, queue_size=10)

status.ErrorNr = 0
last_status.ErrorNr = 99
update = False

def connectToMachine():
    global s
    global port
    global status
    global update
    global pubMachineStatus
    # Open serial port
    #s = serial.Serial('/dev/ttyACM0',115200)
    print 'Opening Serial Port'
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

def RunHomingSeq():
    global s
    global status
    global update
    
    status.IsSynced = False
    status.SequensStarted = True
    status.MachineMoving = True
    status.SequenseNr = 99

    pubMachineStatus.publish(status)
    
    s.write('G28 X Y' + '\n') # Send g-code block
    grbl_out = s.readline() # Wait for response with carriage return
    
    print ' : ' + grbl_out.strip()
    if grbl_out == 'oMGok\n':
        status.ErrorNr = 0
        status.IsSynced = True
        status.SequensStarted = False
        status.MachineMoving = False
        status.SequenseNr = 0
        pubMachineStatus.publish(status)

    

def XPosSeq():
    global s
    global status
    global update
    
    status.SequensStarted = True
    status.MachineMoving = True
    status.SequenseNr = 91

    pubMachineStatus.publish(status)
    
    s.write('G91\n'+'G0 X10 F1000\n') # Send g-code block
    grbl_out = s.readline() # Wait for response with carriage return
    
    print ' : ' + grbl_out.strip()
    if grbl_out == 'oMGok\n':
        status.ErrorNr = 0
        status.SequensStarted = False
        status.MachineMoving = False
        status.SequenseNr = 0
        pubMachineStatus.publish(status)


def XNegSeq():
    global s
    global status
    global update

    status.SequensStarted = True
    status.MachineMoving = True
    status.SequenseNr = 92

    pubMachineStatus.publish(status)
    
    s.write('G91\n'+'G0 X-10 F1000\n') # Send g-code block
    grbl_out = s.readline() # Wait for response with carriage return
    
    print ' : ' + grbl_out.strip()
    if grbl_out == 'oMGok\n':
        status.ErrorNr = 0
        status.SequensStarted = False
        status.MachineMoving = False
        status.SequenseNr = 0
        pubMachineStatus.publish(status)
        

def cmdCallback(data):
    global status
    print status
    if data.data == 99:
        print 'Starting to home robot'
        RunHomingSeq()
    elif data.data == 90:
        print 'Man. pos X'
        XPosSeq()
    elif data.data == 91:
        print 'Man. neg X'
        XNegSeq()

    print data




def main():
    global status
    global last_status
    global update

    # Subscribe for teleoperations
    rospy.Subscriber("LOMAS_MachineCmd", std_msgs.msg.UInt8, cmdCallback)
    rospy.loginfo("Starting up machine node")

    rospy.init_node('machine', anonymous=False)

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

    s.close()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
	pass