from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    sensor_node = Node(
        package = '3_node',
        executable = 'sensor',
        name = 'sensor_node'
    )
    processor_node = Node(
        package = '3_node',
        executable = 'processor',
        name = 'processor_node'
    )
    logger_node = Node(
        package = '3_node',
        executable = 'logger',
        name = 'logger_node'
    )
    
    return LaunchDescription([
        sensor_node,
        processor_node,
        logger_node
    ])
    
