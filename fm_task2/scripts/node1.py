#!/usr/bin/env python
import rospy
from fm_task2.msg import inputs
global rate

def input_call(pub):
    rate = rospy.Rate(10) 
    data = inputs()
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        data.name = input("enter name")
        data.age = int(input("enter age"))
        rospy.loginfo("input")
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('node1', anonymous=True)
        pub = rospy.Publisher('taking_inputs', inputs, queue_size=10)
        input_call(pub)
    except rospy.ROSInterruptException:
        pass