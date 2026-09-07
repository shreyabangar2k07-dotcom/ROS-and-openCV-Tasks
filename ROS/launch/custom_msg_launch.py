from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package = 'custom_msg_pubsub',
            executable = 'publisher',
            name = 'publisher',
            output = 'screen'
        ),
        Node(
            package = 'custom_msg_pubsub',
            executable = 'subscriber',
            name = 'subscriber',
            output = 'screen'
        )
    ])
