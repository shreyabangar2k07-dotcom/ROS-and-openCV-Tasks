from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='action_server_client',
            executable='server',
            name='action_server',
            output='screen'
        ),

        Node(
            package='action_server_client',
            executable='client',
            name='action_client',
            output='screen'
        )
    ])
