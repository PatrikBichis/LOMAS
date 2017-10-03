#!/usr/bin/env python
# license removed for brevit
import rospy
import roslib
import time

from pyfirmata import Arduino, util
from LOMAS_ROS_pkg.msg import watering_status
from std_msgs.msg import *


# Global var
status = watering_status()
status.ErrorNr = 99

# Defining publisher
pubWateringStatus = rospy.Publisher('LOMAS_WateringState', watering_status, queue_size=10)

def loadParameters():
    """
    Get parameters from ROS param server
    """

    global IsInSimMode
    global Status
    global port
    
    IsInSimMode = rospy.get_param('~sim_port', True)
    port = rospy.get_param('~port', "/dev/ttyACM0")
    status.Interval = rospy.get_param('~watering_interval', 120)
    status.Duration = rospy.get_param('~watering_time', 120)

    print 'Watering param values'
    print IsInSimMode
    print port
    print status.Interval
    print status.Duration
    pubWateringStatus.publish(status)


def abortCallback(data):
    """
    Handling abort comd for watering
    """

    global abort

    print 'Abort'
    abort = data.data


def intervalCallback(data):
    """
    Handling an update of interval parameter
    """

    global status

    print 'Set interval'
    print data.data

    status.Interval = data.data
    rospy.set_param('~watering_interval', data.data)

    pubWateringStatus.publish(status)


def durationCallback(data):
    """
    Handling an update of watering duration parameter
    """

    global status

    print 'Set duration'
    print data.data

    status.Duration = data.data
    rospy.set_param('~watering_time', data.data)

    pubWateringStatus.publish(status)


def cmdCallback(data):
    """
    Handling watering cmd
    """
    global status

    status.Watering = bool(data.data==1)

    board.digital[13].write(data.data)

    pubWateringStatus.publish(status)


def connectToTelemetry(port):
    """
    Connect to telemetry controller (Arduino board)
    """

    global board

    board = Arduino(port)
    
    ctrlValue = int(status.Watering==True)

    # Turn of watering
    board.digital[13].write(ctrlValue)
    print 'Connected to telemetry control board'


def main():
    global port

    # Subscribe to topics
    rospy.Subscriber("LOMAS_WateringCmd", std_msgs.msg.UInt8, cmdCallback)
    rospy.Subscriber("LOMAS_WateringAbort", std_msgs.msg.Bool, abortCallback)
    rospy.Subscriber("LOMAS_WateringSetInterval", std_msgs.msg.UInt8, intervalCallback)
    rospy.Subscriber("LOMAS_WateringSetDuration", std_msgs.msg.UInt8, durationCallback)
    rospy.loginfo("Starting up watering node")

    rospy.init_node('watering', anonymous=False)

    loadParameters()
    connectToTelemetry(port)
    pubWateringStatus.publish(status)

    print 'Watering is waiting for command..'

    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():

        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
	pass