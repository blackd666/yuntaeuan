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
            speed += 50  # 속도를 10 증가시킴
            print(speed)

            # 전진 속도를 유지하는 동안 3초간 대기
            twist = Twist()
            speed = float(speed)
            twist.linear.x = speed
            pub.publish(twist)
            time.sleep(3)

            # 90도 오른쪽으로 회전하는 동작 추가
            angle += 30  # 회전 각도 설정
            angle = float(angle)
            twist.angular.z = angle
            pub.publish(twist)
            time.sleep(3)  # 회전 시간 설정

            # 다시 속도가 10인 상태로 전진
            twist.angular.z = 0.0  # 각속도를 0으로 설정하여 회전 중지
            twist.linear.x = speed
            pub.publish(twist)
          
        
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

        if key =="e":
            print(key)
            angle=0.0
            speed=0.0
            break
        print(1)


        twist = Twist()
        speed=float(speed)
        twist.linear.x = speed; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = float(angle)
        pub.publish(twist)


        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
       
main()
