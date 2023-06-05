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
            import serial
            import time

# 시리얼 통신을 위한 포트와 속도 설정
port = '/dev/ttyUSB0'  # 사용하는 시리얼 포트에 맞게 수정해주세요
baudrate = 9600

# 시리얼 통신 객체 생성
serial_connection = serial.Serial(port, baudrate)

# 로봇 이동 함수 정의
def move_robot(steps):
    # 로봇을 지정한 스텝 수만큼 전진시키는 명령 전송
    serial_connection.write(f'steps,{steps}\n'.encode())

    # 로봇이 이동을 완료할 때까지 대기
    while True:
        response = serial_connection.readline().decode().strip()
        if response == 'done':
            break

# 키 입력 대기 함수 정의
def wait_for_key():
    while True:
        key = input("Press '1' to start the robot: ")
        if key == '1':
            break

# 로봇 작동 함수 정의
def run_robot():
    # 로봇 작동 시작 메시지 출력
    print("Robot is starting...")

    # 로봇 작동 순서대로 실행
    move_robot(3)
    print("Robot has moved 3 steps.")
    time.sleep(1)
    serial_connection.write(b'turn,right\n')
    print("Robot is turning right...")
    time.sleep(1)
    move_robot(2)
    print("Robot has moved 2 steps.")

    # 로봇 작동 완료 메시지 출력
    print("Robot has finished.")

# 프로그램 실행 함수 정의
def main():
    # 시리얼 통신 연결 확인
    if not serial_connection.is_open:
        print(f"Failed to connect to serial port {port}")
        return

    # 키 입력 대기
    wait_for_key()

    # 로봇 작동
    run_robot()

    # 프로그램 종료 시 시리얼 포트 연결 닫기
    serial_connection.close()

# 메인 함수 실행
if __name__ == "__main__":
    main()
       

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
