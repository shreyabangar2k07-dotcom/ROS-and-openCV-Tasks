import rclpy
import random
from rclpy.node import Node
from geometry_msgs.msg import Vector3

class SensorNode(Node):
    def __init__(self):
        super().__init__('Sensor_Node')
        self.publisher_ = self.create_publisher(Vector3, 'topic', 10)
        self.declare_parameter('publish_rate', 2.0)
        self.publish_rate = self.get_parameter('publish_rate').value
        self.timer = self.create_timer(1.0/self.publish_rate, self.timer_callback)
        self.i = 0
    
    def timer_callback(self):
        msg = Vector3()
        msg.x = random.uniform(0, 50)
        msg.y = random.uniform(0, 50)
        msg.z = random.uniform(0, 50)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publihing: x={msg.x} y={msg.y} z={msg.z}')
        self.i += 1
        
            
def main(args=None):
    rclpy.init(args=args)
    Sensor_Node = SensorNode()
    rclpy.spin(Sensor_Node)
    Sensor_Node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

