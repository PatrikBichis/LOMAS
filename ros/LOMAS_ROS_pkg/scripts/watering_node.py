#!/usr/bin/env python
# license removed for brevit
import rospy
import roslib
import serial
import time
import argparse

from serial import SerialException
from LOMAS_ROS_pkg.msg import watering_status
from std_msgs.msg import *


# Global var
status = watering_status()
status.ErrorNr = 99

# Defining publisher
pubWateringStatus = rospy.Publisher('LOMAS_WateringState', watering_status, queue_size=10)

def loadParameters():
    global IsInSimMode
    global Status
    global port
    
    IsInSimMode = rospy.get_param('~sim_port', True)
    port = rospy.get_param('~port', "/dev/ttyUSB1")
    status.Interval = rospy.get_param('~watering_interval', 120)
    status.Duration = rospy.get_param('~watering_time', 120)

    print 'Watering param values'
    print IsInSimMode
    print port
    print status.Interval
    print status.Duration
    pubWateringStatus.publish(status)


def abortCallback(data):
    global abort

    print 'Abort'
    abort = data.data


def intervallCallback(data):
    global status

    print 'Set intervall'
    print data.data

    status.Interval = data.data
    rospy.set_param('~watering_interval', data.data)

    pubWateringStatus.publish(status)


def durationCallback(data):
    global status

    print 'Set duration'
    print data.data

    status.Duration = data.data
    rospy.set_param('~watering_time', data.data)

    pubWateringStatus.publish(status)


def cmdCallback(data):
    global status
   

    pubWateringStatus.publish(status)
    print data


def main():

    # Subscribe 
    rospy.Subscriber("LOMAS_WateringCmd", std_msgs.msg.UInt8, cmdCallback)
    rospy.Subscriber("LOMAS_WateringAbort", std_msgs.msg.Bool, abortCallback)
    rospy.Subscriber("LOMAS_WateringSetIntervall", std_msgs.msg.Bool, intervallCallback)
    rospy.Subscriber("LOMAS_WateringSetDuration", std_msgs.msg.Bool, durationCallback)
    rospy.loginfo("Starting up watering node")

    rospy.init_node('watering', anonymous=False)

    loadParameters()
    #connectToWatering()
    pubWateringStatus.publish(status)

    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():

        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
	pass