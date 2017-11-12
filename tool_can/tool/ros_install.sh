#!/bin/bash
sudo update-locale LANG=C LANGUAGE=C LC_ALL=C LC_MESSAGES=POSIX
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu trusty main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
sudo apt-get update
sudo apt-get install ros-indigo-ros-base
sudo apt-get install python-rosdep
sudo rosdep init
#su firefly
#rosdep update
#echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
#source ~/.bashrc
