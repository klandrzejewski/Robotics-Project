from setuptools import find_packages, setup

package_name = 'webots_ros2_project2_python'

data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/f23_robotics_2_launch.py']))

data_files.append(('share/' + package_name + '/worlds', [
    'worlds/tuscaloosa.wbt', 
]))
data_files.append(('share/' + package_name, ['package.xml']))
# data_files.append(('share/' + package_name + '/resource', [
#     'resource/turtlebot_webots.urdf',
#     'resource/ros2control.yml',
# ]))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    maintainer='Kaleigh Andrzejewski-UA',
    maintainer_email='klandrzejewski@crimson.ua.edu',
    description='Simulation for cs460/560 Project 2',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'launch.frontend.launch_extension': ['launch_ros = launch_ros']
    },

)
