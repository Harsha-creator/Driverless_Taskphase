#!/usr/bin/env python
# license removed for brevity
import sys
import rospy
from fm_task1.msg import numbers

def input_call(pub):
    rate = rospy.Rate(10) 
    num = numbers()
    while not rospy.is_shutdown():
        num.a = input("enter first number")
        num.b = input("enter second number")
        rospy.loginfo("input")
        pub.publish(num)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('numbers_input', anonymous=True)
        pub = rospy.Publisher('number_addition', numbers, queue_size=10)
        input_call(pub)
    except rospy.ROSInterruptException:
        pass