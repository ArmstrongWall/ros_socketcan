#!/bin/bash
sudo ifconfig can0 down
sudo ip link set can0 type can bitrate 250000
sudo ifconfig can0 up
ip -d link show can0
