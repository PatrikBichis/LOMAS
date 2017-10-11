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


# Global var
status = machine_status()
stop = False
abort = False
#port = "/dev/ttyUSB0"
#path = "/media/gcode/"

# Defining publisher
pubMachineStatus = rospy.Publisher('LOMAS_MachineState', machine_status, queue_size=10)

status.ErrorNr = 99


def loadParameters():
    global IsInSimMode
    global Status
    global port
    global path
    
    IsInSimMode = rospy.get_param('~sim_port', True)
    port = rospy.get_param('~port', "/dev/ttyUSB0")
    path = rospy.get_param('~path', "/media/gcode/")
    status.Interval = rospy.get_param('~cultivation_interval', 120)

    print 'Machine param values:'
    print " * IsInSimMode: ", IsInSimMode
    print " * Port:        ", port
    print " * Path:        ", path
    print " * Interval:    ", status.Interval
    print ''
    pubMachineStatus.publish(status)



def removeComment(string):
    if (string.find(';')==-1):
        return string
    else:
        return string[:string.index(';')]



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
        print 'Warning : Serial port will be simulated'
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



def sendGCodeFile(file, seq):
    global status
    global stop
    global abort
    global f

    status.SequensStarted = True
    status.MachineMoving = True

    stop = False
    abort = False

    pubMachineStatus.publish(status)
    # Open g-code file
    #f = open('/media/UNTITLED/shoulder.g','r');
    f = open(file,'r');
    print 'Opening gcode file'
    
    # Stream g-code
    for line in f:
        l = removeComment(line)
        l = l.strip() # Strip all EOL characters for streaming
        if (l.isspace()==False and len(l)>0) :
            ok = sendSerialCmd(l + '\n')

        if stop:
            print 'Stopped'
            status.SequenseNr = 90
            status.MachineMoving = False
            pubMachineStatus.publish(status)
            while stop:
                if abort:
                    status.SequenseNr = 91
                    print 'Aborting while'
                    pubMachineStatus.publish(status)
                    break

                time.sleep(0.1)

            print 'Restarted'
            status.MachineMoving = True
            status.SequenseNr = seq
            pubMachineStatus.publish(status)
            
        if abort:
            status.SequenseNr = 91
            pubMachineStatus.publish(status)
            print 'Aborting for'
            break

    f.close()
    status.ErrorNr = 0
    status.SequensStarted = False
    status.MachineMoving = False
    status.SequenseNr = 0
    abort = False
    


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

        
def stopCallback(data):
    global stop

    print 'Stop '
    stop = data.data


def abortCallback(data):
    global abort

    print 'Abort'
    abort = data.data


def intervallCallback(data):
    global status

    print 'Set intervall'
    print data.data

    status.Interval = data.data
    rospy.set_param('~cultivation_interval', data.data)

    pubMachineStatus.publish(status)



def cmdCallback(data):
    global status
    global path
    global stop
    global abort
 
    if data.data == 99:
        print 'Starting to home robot'
        status.IsSynced = False
        sendGCodeCmd('G28 X Y Z' + '\n')
        status.IsSynced = True
    elif data.data == 1:
        print 'Send cultivation.g file'
        status.SequenseNr = 1
        sendGCodeFile(path + 'cultivation.g', 1)
    elif data.data == 2:
        print 'Send seed.g file'
        status.SequenseNr = 2
        sendGCodeFile(path + 'seed.g', 2)
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
        sendGCodeCmd('G91\n'+'G0 X10 Y10 F1000\n')
    elif data.data == 95:
        print 'Man. neg X pos Y'
        sendGCodeCmd('G91\n'+'G0 X-10 Y10 F1000\n')
    elif data.data == 96:
        print 'Man. pos X neg Y'
        sendGCodeCmd('G91\n'+'G0 X10 Y-10 F1000\n')
    elif data.data == 97:
        print 'Man. neg X neg Y'
        sendGCodeCmd('G91\n'+'G0 X-10 Y-10 F1000\n')

    pubMachineStatus.publish(status)
    print data



def main():
    global status

    # Subscribe 
    rospy.Subscriber("LOMAS_MachineCmd", std_msgs.msg.UInt8, cmdCallback)
    rospy.Subscriber("LOMAS_MachineStop", std_msgs.msg.Bool, stopCallback)
    rospy.Subscriber("LOMAS_MachineAbort", std_msgs.msg.Bool, abortCallback)
    rospy.Subscriber("LOMAS_MachineSetIntervall", std_msgs.msg.UInt8, intervallCallback)
    
    print ''
    print "Starting up machine node"
    print ''

    rospy.init_node('machine', anonymous=False)

    loadParameters()
    connectToMachine()
    pubMachineStatus.publish(status)

    print ''
    print 'Machine is waiting for command..'
    print ''

    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():

        rate.sleep()


    if IsInSimMode == False:
        s.close()
        f.close()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
	pass