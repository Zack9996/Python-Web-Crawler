import nmap

def scan_router_firewall(target_host):
    # 初始化端口掃描器
    nm = nmap.PortScanner()

    # 設置掃描參數
    scan_arguments = '-p 1-65535'  # 指定要掃描的全部端口範圍

    # 執行掃描
    nm.scan(target_host, arguments=scan_arguments)

    # 獲取掃描結果
    scan_results = nm[target_host]

    # 輸出路由器和防火牆掃描結果
    for port in scan_results['tcp']:
        port_info = scan_results['tcp'][port]
        print(f"Port: {port}")
        print(f"Service: {port_info['name']}")
        print(f"State: {port_info['state']}")
        print(f"Product: {port_info['product']}")
        print(f"Version: {port_info['version']}")
        print("------")

# 主機地址
target_host = '192.168.70.124'  # 替換成實際的路由器或防火牆的IP地址

# 執行掃描
scan_router_firewall(target_host)
