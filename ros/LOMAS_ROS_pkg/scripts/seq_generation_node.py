#!/usr/bin/env python
# license removed for brevit
import rospy
import roslib


from std_msgs.msg import *

def main():

    print ''
    print "Starting up seq_generation node"
    print ''

    rospy.init_node('seq_generation', anonymous=False)

    #loadParameters()
    #connectToTelemetry(port)
    #pubWateringStatus.publish(status)

    print ''
    print 'Sequence generation is waiting for command..'
    print ''


    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():


        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
	pass