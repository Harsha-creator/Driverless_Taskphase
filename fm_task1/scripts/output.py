#!/usr/bin/env python
import rospy
from fm_task1.msg import numbers

def callback(message):
    rospy.loginfo("sum of the numbers %s",(message.a + message.b) )
    
def output_call():
    rospy.init_node('output', anonymous=True)
    rospy.Subscriber("number_addition", numbers, callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        output_call()
    except:
        print("error")
    