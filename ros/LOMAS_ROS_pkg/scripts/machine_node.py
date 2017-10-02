#!/usr/bin/env python
# license removed for brevit
import rospy

from LOMAS_ROS_pkg.msg import machine_status

status = machine_status()
last_status = machine_status()

status.ErrorNr = 0
last_status.ErrorNr = 99

pubMachineStatus = rospy.Publisher('LOMAS_MachineState', machine_status, queue_size=1)

def main():
    global status
    global last_status

    # Subscribe for teleoperations
    #rospy.Subscriber("joy", Joy, joyCallback)
    rospy.loginfo("Starting up machine node")

    rospy.init_node('machine', anonymous=False)

    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        if status != last_status:
            pubMachineStatus.publish(status)
            last_status = status

        rate.sleep()
        #print("been here!")


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
	pass