import os
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess, DeclareLaunchArgument, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch.actions import GroupAction, IncludeLaunchDescription
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource


def generate_launch_description():

    return([

        DeclareLaunchArgument('namespace', default_value='blurov2', description='Namespace of the MAVROS system'),
        DeclareLaunchArgument('navigation_type', default_value='OFFBOARD', description='Type of navigation'),

        Node(package='mavros_control',
                      executable='controller',
                      namespace=LaunchConfiguration('namespace'),
                      name='controller',
                      parameters=[
                        {'xy_tolerance': 0.7,
                         'z_tolerance': 0.3,
                         'use_altitude': False,
                         'navigation_type': LaunchConfiguration('navigation_type'),
                        }]),
            IncludeLaunchDescription(
                XMLLaunchDescriptionSource([
                        PathJoinSubstitution([
                            FindPackageShare('mavros_control'),
                            'launch',
                            'mavros.launch'
                        ])
                    ]),
                    launch_arguments={
                        'fcu_url': 'udp://0.0.0.0:5777@',
                        'fcu_protocol': 'v2.0',
                        'namespace': LaunchConfiguration('namespace'),
                    }.items()
                    ),
   ])

