from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package = 'service_client',
            executable = 'service',
            name = 'service',
            output = 'screen'
        ),

        Node(
            package = 'service_client',
            executable = 'client',
            name = 'client',
            output = 'screen',
            arguments = ['3', '7']
        )
    ])
