
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class MyPublisher(Node):
    def __init__(self):
        super().__init__('my_publisher')
        self.publisher_ = self.create_publisher(Float32, 'khadas', 10)
        self.timer_ = self.create_timer(0.5, self.publish_message)

    def publish_message(self):
        msg = Float32()
        # 여기에 데이터를 설정합니다.
        msg.data = 3.14
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
