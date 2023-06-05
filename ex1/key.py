import rclpy
import time


from geometry_msgs.msg import Twist

import sys, select, termios, tty

settings = termios.tcgetattr(sys.stdin)


def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def main(args=None):	

    rclpy.init(args=args)
    node = rclpy.create_node('cmd')
        
    pub = node.create_publisher(Twist, 'cmd', 3)

    speed=0
    angle=0

    
    while(1):
        key = getKey()
    if key == "1":
        print(key)
        if speed == 360:
            speed = 360
        elif speed < 360:
            speed = speed + 10
        print(speed)
        delay(2)
    else:
        angle = angle - 10
        print(angle)

        if key =="s":
            print(key)
            if speed ==-360:
                speed=360
            else:
                speed=speed-10
            print(speed)

        if key=="a":
            print(key)
            speed=0
            angle=angle-10
            print(angle)

        if key=="d":
            print(key)
            speed=0
            angle=angle+10
            print(angle)

        if key=="q":
            print(key)
            angle=0.0
            speed=0.0
            print(speed)
            print(angle)
             break
        print(1)


       

        twist = Twist()
        speed=float(speed)
        twist.linear.x = speed; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = float(angle)
        pub.publish(twist)


        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

main()
