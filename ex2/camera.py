import rclpy
import cv2
import numpy as np
from std_msgs.msg import Float32

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('publisher_node')
    publisher = node.create_publisher(Float32, 'camera', 10)
    
    # 카메라 초기화
    cap = cv2.VideoCapture(2)

    while True:
        # 프레임 읽기
        ret, frame = cap.read()
        frame_ori=frame.copy()
        

        # 이미지 이진화
        blur = cv2.GaussianBlur(frame,(15,15),0)
        gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 15, 15)

        # 직선 검출
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=1000)

        # 가장 긴 직선 추출
        longest_line = None
        longest_length = 0

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                angle = np.abs(np.arctan2(y2-y1, x2-x1)*180/np.pi)
                
                length = np.sqrt((x2-x1)**2 + (y2-y1)**2)
                if length > longest_length:
                    if 30 <= angle <= 90:

                        longest_line = line
                        longest_length = length

            # 가장 긴 직선 그리기
            if longest_line is not None:
                x1, y1, x2, y2 = longest_line[0]
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cen=(x1+x2)/2
                print(cen)
                if cen>320:
                    data=1.0
                else:
                    data=0.0

                
                msg = Float32()
                msg.data = float(data)
                print(msg)
                publisher.publish(msg)

        # 화면 출력
        cv2.imshow('origine', frame_ori)
        cv2.imshow('blur', blur)
        cv2.imshow('frame', frame)
        cv2.imshow('edges', edges)

        # 종료 조건
        if cv2.waitKey(1) == ord('q'):
            break

    # 종료
    cap.release()
    cv2.destroyAllWindows()

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
