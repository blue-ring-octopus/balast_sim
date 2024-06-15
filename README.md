# gazebo similation of ballast tank 
## Depandencies
Install all turtlebot packages
```
sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy \
  ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc \
  ros-noetic-rgbd-launch ros-noetic-rosserial-arduino \
  ros-noetic-rosserial-python ros-noetic-rosserial-client \
  ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server \
  ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
  ros-noetic-compressed-image-transport ros-noetic-rqt* ros-noetic-rviz \
  ros-noetic-gmapping ros-noetic-navigation ros-noetic-interactive-markers
```
```
 sudo apt install ros-noetic-dynamixel-sdk
```
```
 sudo apt install ros-noetic-turtlebot3-msgs
```
```
 sudo apt install ros-noetic-turtlebot3
```
```
cd ~/catkin_ws/src/
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/catkin_ws && catkin_make
```

## Configure Simulation
1. Go to your catkin_ws/src
 ```
 git clone https://github.com/blue-ringed-octopus/ballast_sim.git 
 ``` 
2. navigate to home/.gazebo
3. create a folder called models if it does not already exist.
4. Go to ballast_sim/meshes/world, copy everything into the .gazebo/models folder
5. launch the simulation
``` 
roslaunch ballast_sim ballast_world.launch 
```