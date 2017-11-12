# ros_socketcan
create at 2016.11.3
# 实现的功能是rk3288通过can通信来控制电机
## catkin_ws是ROS的包，基于socketcan和can4python库开发,通过接口CAN0传输CAN消息的功能
## tool_can是用于CAN0的测试工具，编译的canutils工具和CAN0初始化脚本
# Ref:
## 1:can4python库　https://github.com/caran/can4python
## 2:canutils库(基于libsocketcan编译)　http://public.pengutronix.de/software/socket-can/canutils/v4.0/
## 3:libsocketcan库　http://public.pengutronix.de/software/libsocketcan/
