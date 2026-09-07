import rclpy
import time
from rclpy.action import ActionServer
from rclpy.node import Node

from custom_action_pkg.action import CountDown


class CountDownActionServer(Node):

    def __init__(self):
        super().__init__('countdown_action_server')
        self._action_server = ActionServer(
            self,
            CountDown,
            'countdown',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        feedback_msg = CountDown.Feedback()
        for count in range(goal_handle.request.target, -1, -1):
            feedback_msg.current_count = count
            self.get_logger().info(f"current count: {count}")
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)
        goal_handle.succeed()
        result = CountDown.Result()
        result.status = "Done"
        return result

def main(args=None):
    rclpy.init(args=args)

    countdown_action_server = CountDownActionServer()

    rclpy.spin(countdown_action_server)


if __name__ == '__main__':
    main()
