#!/usr/bin/env python
import rospy
from fm_task2.msg import eligibility
from fm_task2.msg import inputs
global rate

def callback(message):
    e = eligibility()
    e.name = message.name
    if(message.age < 18):
        e.eligible = 0
    else:
        e.eligible = 1
    pub2 = rospy.Publisher('checking_eligibility', eligibility, queue_size=10)
    while not rospy.is_shutdown():
        rospy.loginfo("checking")
        pub2.publish(e)
        rate.sleep()
    
def node2_call():
    rospy.init_node('node2', anonymous=True)
    rospy.Subscriber('taking_inputs', inputs, callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        node2_call()
    except :
        print("error")