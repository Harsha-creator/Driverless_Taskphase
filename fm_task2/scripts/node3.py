#!/usr/bin/env python
import rospy
from fm_task2.msg import eligibility

def callback(message):
    print("name: "+message.name) 
    if(message.eligible == 1):  
        print("eligible")
    else:
        print("not eligible")

def display():
    rospy.init_node('node3', anonymous=True)
    rospy.Subscriber("checking_eligibility", eligibility, callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        display()
    except:
        print("error")