#!/usr/bin/env python3

import os
import rospy
from duckietown.dtros import DTROS,NodeType
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage

# import picamera
# import picamera.array
#import cv2_to_compressed_imgmsg
import cv2
import numpy as np
from cv_bridge import CvBridge

class MyNode(DTROS):

    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(MyNode, self).__init__(node_name=node_name, node_type=NodeType.GENERIC)
        # construct publisher
        self.pub = rospy.Publisher('/jcdgo/camera_node/image/compressed', CompressedImage, queue_size=10)

        
    def run(self):
        # publish message every 1 second
        rate = rospy.Rate(30) # 200Hz
        width = 640
        height = 480
        
        cap = cv2.VideoCapture(2)

        while not rospy.is_shutdown():
            # Capture frame-by-frame
            # cap.read() read the video by frame
            # return ret and frame:
            # ret is bool type, get true if read successful, otherwise false
            # frame: 3D matrix,  the everyframe you read
            ret, frame = cap.read()

            # you can now treat output as a normal numpy array
            if ret:
                # print("frame.shape",frame.shape)
                compressed_img_msg = br.cv2_to_compressed_imgmsg(frame, dst_format='jpg')
                rospy.loginfo("Publishing image from Duckiebot camera")
                self.pub.publish(compressed_img_msg)
            else:
                rospy.loginfo("No image published from Duckiebot camera")

            rate.sleep()



if __name__ == '__main__':
    # create the node
    br = CvBridge()
    print("launching node..")
    node = MyNode(node_name='jcdgo_node')
    
    # run node
    node.run()
    # keep spinning
    rospy.spin()
