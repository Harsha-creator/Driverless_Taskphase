#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys
bridge = CvBridge()


def display(img):
    try:
        cv_image = bridge.imgmsg_to_cv2(img)
    except CvBridgeError as e:
        print(e)
    cv2.imshow("RVIZ image",cv_image)
    cv2.waitKey(3)
    

if __name__ == "__main__":
    rospy.init_node('depthcamera_Subscriber', anonymous=True)
    subscriber = rospy.Subscriber('/camera/depth/image_raw', Image, display)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()