import rclpy
import time

from std_msgs.msg import Float32

import sys, select, termios, tty

settings = termios.tcgetattr(sys.stdin)


def getKey(default_value):
    tty.setraw(sys.stdin.fileno())
    [i, o, e] = select.select([sys.stdin], [], [], 0.1)
    if i:
        key = sys.stdin.read(1)
    else:
        key = default_value
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def main(args=None):	
    rclpy.init(args=args)
    node = rclpy.create_node('teleop_twist_keyboard')
    pub = node.create_publisher(Float32, 'cmd', 3)
    
    cmd = 10.0
    key=""
    while True:
        msg = Float32()
        key = getKey(default_value=key)
        if key == "w":
            print(key)
            cmd = 1.0
            msg.data = float(cmd)
            pub.publish(msg)
        elif key == "s":
            print(key)
            cmd = 0.0

            msg.data = float(cmd)
            pub.publish(msg)

        elif key == "e":
            print(key)
            cmd = 2.0

            msg.data = float(cmd)
            pub.publish(msg)
            break

        else:
            print("read")
        
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
