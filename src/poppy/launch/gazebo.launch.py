import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Paths to package files
    package_name = 'poppy'
    urdf_file = os.path.join(get_package_share_directory(package_name), 'urdf', 'Poppy_Humanoid.URDF')
    #rviz_config_file = os.path.join(get_package_share_directory(package_name), 'config', 'rviz.rviz')

    return LaunchDescription([
        # Include the Gazebo launch file
        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource([os.path.join(
        #         get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
        #     launch_arguments={'world': world_file}.items(),
        # ),

        # Publish the robot description (URDF) to the /robot_description topic
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}],
            #remappings=[('/joint_states', '/joint_states')],  # Ensure it listens to the right topic
        ),

        # Launch RViz with the saved configuration file
        # Node(
        #     package='rviz2',
        #     executable='rviz2',
        #     name='rviz2',
        #     output='screen',
        #     arguments=['-d', rviz_config_file],
        # ),

        # Joint state publisher publishing to a different topic
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen',
            #parameters=[{'ignore_joints': ['base_joint', 'shoulder_joint', 'elbow_joint', 'tool_joint']}],
            #remappings=[('/joint_states', '/static_joint_states')],  # Remap to static joint states
        ),

        # Add your joystick joint controller node
        # Node(
        #     package=package_name,
        #     executable='joystick_moveit_controller',  # Ensure this matches your script name
        #     name='joystick_moveit_controller',
        #     output='screen',
        # ),

        # Node(
        #     package='joint_state_publisher_gui',
        #     executable='joint_state_publisher_gui',
        #     name='joint_state_publisher_gui',
        #     output='screen',
        # ),

        # Launch joy_node to read joystick input
        # Node(
        #     package='joy',
        #     executable='joy_node',
        #     name='joy_node',
        #     output='screen',
        # ),
    ])
