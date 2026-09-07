import rclpy
import random
from rclpy.node import Node
from custom_msg_pkg.msg import Custom 

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Custom, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Custom()
        msg.name = 'Robot: bot_1' 
        msg.battery_level = random.uniform(0, 100)
        msg.is_moving = random.choice([True, False])
        msg.error = random.randint(0, 10)
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: {msg.name} |  Battery: {msg.battery_level}% | Moving: {msg.is_moving} | Error: {msg.error}")


def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
