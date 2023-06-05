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
    if key == "w":
        print(key)
        speed += 10
        print(speed)
   
        twist = Twist()
        twist.linear.x = speed
        pub.publish(twist)
        time.sleep(3)

        angle = 90  # 회전 각도 설정
        twist.angular.z = angle
        pub.publish(twist)
        time.sleep(3)  # 회전 시간 설정

    # 다시 속도가 10인 상태로 전진
        twist.angular.z = 0  # 각속도를 0으로 설정하여 회전 중지
        twist.linear.x = speed
        pub.publish(twist)
        
      print(1)
       


       

        twist = Twist()
        speed=float(speed)
        twist.linear.x = speed; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = float(angle)
        pub.publish(twist)


        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

main()
