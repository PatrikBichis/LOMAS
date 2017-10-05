#!/usr/bin/env python
# license removed for brevit
import rospy
import roslib


from std_msgs.msg import *

def main():

    rospy.init_node('seq_generation', anonymous=False)

    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():


        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
	pass