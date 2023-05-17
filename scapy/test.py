from scapy.all import *

# 构造Ping请求数据包
ping_packet = IP(dst="192.168.70.124")/ICMP()

# 发送Ping请求并等待响应
response = sr1(ping_packet)

# 打印响应结果
if response:
    print("Ping成功")
else:
    print("Ping失败")
