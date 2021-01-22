# Kvaser CAN
sudo ip link set can0 down
sudo ip link set can0 type can bitrate 500000
sudo ip link set can0 up

sudo ip link set can1 down
sudo ip link set can1 type can bitrate 500000
sudo ip link set can1 up


sudo ip link delete vcan0
sudo rmmod vcan
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set vcan0 up

#reszie TX Queue
sudo ifconfig can0 txqueuelen 2000
sudo ifconfig can1 txqueuelen 2000

