#!/usr/bin/env python3
import roslib; roslib.load_manifest('socket_can_com')
import rospy
#import tf.transformations
from geometry_msgs.msg import Twist
import time
import can4python as can


def callback(msg):
    rospy.loginfo("Received a /cmd_vel message!")
    rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
    rospy.loginfo("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))
    # Do velocity processing here:
    # Use the kinematics of your robot to map linear and angular velocities into motor commands

    #v_l = ...
    #v_r = ...
    if(msg.linear.x == 0.5 and msg.angular.z == 0):#直行
        bus.send_signals({'testsignal2': 0x0 })
        time.sleep(2)
        bus.send_signals({'testsignal2': 0x00080108 }) 


    elif(msg.linear.x == 0.5 and msg.angular.z == 1):#左转
        bus.send_signals({'testsignal2': 0x0 }) 
        time.sleep(2)
        bus.send_signals({'testsignal2': 0x000f0105 })


    elif(msg.linear.x == 0.5 and msg.angular.z == -1):#右转
        bus.send_signals({'testsignal2': 0x0 }) 
        time.sleep(1)
        bus.send_signals({'testsignal2': 0x0008010f }) 


    elif(msg.linear.x == 0   and msg.angular.z == 1):#原地左转
        bus.send_signals({'testsignal2': 0x0 }) 
        time.sleep(1)
        bus.send_signals({'testsignal2': 0x00080008 }) 


    elif(msg.linear.x == 0   and msg.angular.z == -1):#原地右转
        bus.send_signals({'testsignal2': 0x0 }) 
        time.sleep(1)
        bus.send_signals({'testsignal2': 0x01080108 }) 


    elif(msg.linear.x == -0.5 and msg.angular.z == -1):#后退
        bus.send_signals({'testsignal2': 0x0 }) 
        time.sleep(1)
        bus.send_signals({'testsignal2': 0x01080008 }) 


    else:
        bus.send_signals({'testsignal2': 0x0 }) # Signal value = 5. Start periodic transmission.
    # Then set your wheel speeds (using wheel_left and wheel_right as examples)
    #wheel_left.set_speed(v_l)
    #wheel_right.set_speed(v_r)

def listener():
    rospy.init_node('cmd_vel_listener')
    rospy.Subscriber("cmd_vel", Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    frame_def = can.CanFrameDefinition(1, name='testmessage')#ID is 0x07
    frame_def.producer_ids = ["1"]
    frame_def.cycletime = 250 # milliseconds
  
    signal_def = can.CanSignalDefinition("testsignal2", 0, 32)
    frame_def.signaldefinitions.append(signal_def)
    
    
    config = can.Configuration({1: frame_def}, ego_node_ids=["1"])
    bus = can.CanBus(config, 'can0', use_bcm=True)
    #bus.send_signals({'testsignal2': 0x01080008 }) # Signal value = 5. Start periodic transmission.
    #bus.send_signals({"testsignal2": 8 ,"testsignal3": 10}) # Signal value = 5. Start periodic transmission.
    listener()



