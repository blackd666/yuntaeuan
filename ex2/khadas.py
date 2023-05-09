import rclpy
import serial

from rclpy.node import Node
from std_msgs.msg import Float32
from geometry_msgs.msg import Vector3
import time

class serial_node(Node):
    def __init__(self,port_name):
        super().__init__('serial_node')

        self.subscription_camera = self.create_subscription(
            Float32,
            'camera',
            self.listener_callback_camera,
            10)

        self.subscription = self.create_subscription(
            Float32,
            'To_khedas',
            self.listener_callback,
            10)
        
        self.subscription
        self.subscription_camera

        self.Serial_ = serial.Serial(
            port=port_name,
            baudrate=115200
        )

        # Publisher init
        self.publisher_ = self.create_publisher(Vector3, 'khadas', 10)


    def listener_callback_camera(self, msg):
        self.pos=msg.data


    def listener_callback(self, msg):
        key = Float32()
        enco=Vector3()

        self.key=msg.data


        print("pos",self.pos)
        #print("x",self.key)

        if self.key==1.0:
            if self.pos==1.0:
                left=50
                right=10
            else:
                left=10
                right=50
            #print(left,right) 

            self.serial_write(left,right)
        elif self.key==0.0:
            left=1000
            right=10
            #print(left,right) 
            self.serial_write(left,right)

        elif self.key==2.0:
            left=2000
           
            right=125
            #print(left,right) 
            self.serial_write(left,right)

        else:
            self.serial_write(0,0)

        data=self.serial_read()
        #print(data)

        if data!= -1:
            enco.x=float(data[0])
            enco.y=float(data[1])
            #print(enco)
            self.publisher_.publish(enco)
        else:
            print("err")
    
    def serial_write(self,data1,data2):
        datafame = '$'+str(data1)+','+str(data2)
        #print(datafame)
        self.Serial_.write(datafame.encode())

    def serial_read(self):
        response = self.Serial_.readline()
        data = response[:len(response)-2].decode('utf-8')
        #print(data)
        data = data.split(',')
        return data

def main(args=None):
    rclpy.init(args=args)
    Test_node = serial_node("/dev/ttyUSB1")
    rclpy.spin(Test_node)
    Test_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
