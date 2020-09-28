#!/usr/bin/env python

import rospy
# Adding roslib:
import roslib
import time
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback
# Adding these messages:
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

nImage = 1

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received
"""
def feedback_callback(feedback):
    global nImage
    print('[Feedback] image n.%d received'%nImage)
    nImage += 1
"""

# initializes the action client node
rospy.init_node('action_client')
pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
pub2 = rospy.Publisher('drone/takeoff', Empty, queue_size = 1)
pub3 = rospy.Publisher('drone/land', Empty, queue_size = 1)
empty_msg = Empty()

twist = Twist()
twist.linear.x = 2; twist.linear.y = 0; twist.linear.z = 0
twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0

print("Publishing!")
pub3.publish(empty_msg) # Land if already in the air
pub2.publish(empty_msg) # Take off again
pub.publish(twist) # Move in a direction
print("Done!")


# create the connection to the action server
#client = actionlib.SimpleActionClient('/ardrone_action_server', ArdroneAction)

# waits until the action server is up and running
#client.wait_for_server()

# creates a goal to send to the action server
#goal = ArdroneGoal()
#goal.nseconds = 10 # indicates, take pictures along 10 seconds

# sends the goal to the action server, specifying which feedback function
# to call when feedback received
#client.send_goal(goal, feedback_cb=feedback_callback)

