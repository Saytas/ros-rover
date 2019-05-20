#!/usr/bin/python

"""
Class for low level control of owr car. It assumes ROS-i2cpwmboard has been
installed
"""

import rospy
from i2cpwm_board.msg import Servo, ServoArray
from geometry_msgs.msg import Twist
import time

class ServoConvert():
    """
    Class for handling the servos for the i2c control i2cpwm_board
    The input range is [-1, 1]
    """
    def __init__(self, id = 1, center_value = 333, range = 90, direction = 1):
        self.value = 0.0
        self.value_out = center_value
        self._center = center_value
        self._range = range
        self._half_range = 0.5 * range
        self._dir = direction
        ##self.center_value = center_value
        self.id = id

        ##--- Convert its range in [-1, 1]
        self._sf = 1.0 / self._half_range

    def get_value_out(self, value_in):
        """
        Given an input reference in [-1, 1], it converts it in the
        actual servo range
        """

        ##--- Vaule is in [-1, 1]
        self.value = value_in
        self.value_out = int(self._dir * value_in * self._half_range + self._center)
        print self.id, self.value_out
        return(self.value_out)

class DkLowLevelCtrl():
    """
    Low level control for donkey car in ROS
    """
    def __init__(self):
        rospy.loginfo("Setting up the Node...")

        rospy.init_node('dk_llc')

        ##--- Create an actuator dictionary
        self.actuators = {}
        self.actuators['throttle'] = ServoConvert(id = 1)
        self.actuators['steering'] = ServoConvert(id = 2, direction = 1) ##- Positive left
        rospy.loginfo("> Actuators correctly initialized!")

        ##--- Create the servo array publisher
        ##-- Create the message
        self._servo_msg = ServoArray()
        for i in range(2):
            self._servo_msg.servos.append(Servo())

        ##--- Create the servo array publisher
        self.ros_pub_servo_array = rospy.Publisher("/servo_absolute", ServoArray, queue_size = 1)
        rospy.loginfo("> Publisher correctly initialized!")

        ##--- Create the Subscriber to Twist commands - /cmd_vel topic
        self.ros_sub_twist = rospy.Subscriber("/cmd_vel", Twist, self.set_actuators_from_cmdvel)
        rospy.loginfo("> Subscriber correctly initalized!")

        ##--- Save the last time we got a reference. Stop the vehicle
        self._last_time_cmd_rcv = time.time()
        self._timeout_s = 5 ##-- Stop after 5 seconds
        rospy.loginfo("Initialization complete!")

    def set_actuators_from_cmdvel(self, message):
        """
        Get a Twist message from cmd_vel, assuming max input is 1
        """

        ##--- Save the time
        self._last_time_cmd_rcv = time.time()

        ##--- Convert vel into servo values
        self.actuators['throttle'].get_value_out(message.linear.x)
        self.actuators['steering'].get_value_out(message.angular.z) ##- Positive right
        rospy.loginfo("Got a command v = %2.1f s = %2.1f"%(message.linear.x, message.angular.z))

        ##--- Publish the message using a function
        self.send_servo_msg()

    def set_actuators_idle(self):
        self.actuators['throttle'].get_value_out(0) #- Positive forward
        self.actuators['steering'].get_value_out(0) #- Positive right
        rospy.loginfo("Setting actuators to idle!")

        ##--- Publish the message using a function
        self.send_servo_msg()

    def send_servo_msg(self):
        """
        Publish the current actuators' value to the i2i2cpwm_board
        Servos = array of Servo. Each servo has an id and a value to fill
        """
        for actuator_name, servo_obj in self.actuators.iteritems():
            self._servo_msg.servos[servo_obj.id-1].servo = servo_obj.id
            self._servo_msg.servos[servo_obj.id-1].value = servo_obj.value_out
            rospy.loginfo("Sending to %s command %d"%(actuator_name, servo_obj.value_out))

        self.ros_pub_servo_array.publish(self._servo_msg)

    @property
    def is_controller_connected(self):
        print time.time() - self._last_time_cmd_rcv
        return(time.time() - self._last_time_cmd_rcv < self._timeout_s)

    def run(self):
        ##--- Set the control rate
        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            print self._last_time_cmd_rcv, self.is_controller_connected

            if not is_controller_connected:
                self.set_actuators_idle()

            rate.sleep()

"""
Execute the main file
"""
if __name__ == "__main__":
    dk_llc = DkLowLevelCtrl()
    dk_llc.run()

