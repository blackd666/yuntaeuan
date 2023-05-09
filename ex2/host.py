import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from geometry_msgs.msg import Vector3
import time

class MyNode(Node):

    def __init__(self):
        self.flag=0
        self.save_enco_x=10000000000000
        self.save_enco_y=100000000000000000
        super().__init__('my_node')
        self.publisher = self.create_publisher(Float32, 'To_khedas', 10)

        self.subscription1 = self.create_subscription(
            Float32,
            'cmd',
            self.cmd,
            10)
        self.subscription1
        
        self.subscription2 = self.create_subscription(
            Vector3,
            'khadas',
            self.enco,
            10)
        self.subscription2

    def cmd(self, key_msg): #키
        self.key_msg=key_msg
        self.publisher.publish(self.key_msg)
        

    def enco(self, enco_msg): #엔코더


        if self.key_msg.data==0.0:
            
            if self.flag==0:
                self.save_enco_x=abs(enco_msg.x)-1000
                self.save_enco_y=abs(enco_msg.y)-1000
                self.flag=1
                enco_msg.x=0.0
                enco_msg.y=0.0
        print("enco_msg.x",abs(enco_msg.x))   
        print("enco_msg.y",abs(enco_msg.y))  
        print("save_enco_X",self.save_enco_x)
        print("save_enco_y",self.save_enco_y)

        if abs(enco_msg.x)>self.save_enco_x and abs(enco_msg.y)>self.save_enco_y:
            print("stop")
            self.key_msg.data=2.0
            self.publisher.publish(self.key_msg)



def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
