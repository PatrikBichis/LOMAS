#!/usr/bin/env python
# license removed for brevit
import rospy

def main():

    # Subscribe for teleoperations
    #rospy.Subscriber("joy", Joy, joyCallback)

    rospy.init_node('watering', anonymous=False)

    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():

        rate.sleep()
        #print("been here!")


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
	pass