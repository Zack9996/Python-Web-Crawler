import nmap

def scan_host_ports(target_host):
    # 初始化端口掃描器
    nm = nmap.PortScanner()

    # 掃描主機的所有端口
    result = nm.scan(target_host, arguments='-p 1-65535')

    # 獲取主機的掃描結果
    scanned_ports = []
    for port in result['scan'][target_host]['tcp']:
        if result['scan'][target_host]['tcp'][port]['state'] == 'open':
            scanned_ports.append(port)

    # 返回掃描結果
    return scanned_ports

# 主機地址
target_host = '192.168.70.124'

# 掃描主機端口
scanned_ports = scan_host_ports(target_host)

# 輸出掃描結果
print(f"主機 {target_host} 的開放端口：")
for port in scanned_ports:
    print(f"Port {port} is open")
