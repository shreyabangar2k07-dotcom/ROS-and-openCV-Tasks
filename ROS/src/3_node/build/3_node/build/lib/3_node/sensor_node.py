import rclpy
import random
from rclpy.node import Node
from geometry_msgs.msg import Vector3

class SensorNode(Node):
    def __init__(self):
        super().__init__('Sensor_Node')
        self.publisher_ = self.create_publisher(Vector3, 'vector_topic', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
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

