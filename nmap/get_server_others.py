import nmap

def discover_services(target_host):
    # 初始化nmap端口掃描器
    nm = nmap.PortScanner()

    # 執行版本探測
    nm.scan(target_host, arguments='-sV')

    # 獲取主機的版本探測結果
    services = []
    for host in nm.all_hosts():
        for port in nm[host]['tcp']:
            service = nm[host]['tcp'][port]
            services.append({
                'port': port,
                'protocol': service['name'],
                'state': service['state'],
                'product': service['product'],
                'version': service['version']
            })

    # 返回服務探測結果
    return services

# 主機地址
target_host = '192.168.70.124'

# 執行服務探測
discovered_services = discover_services(target_host)

# 輸出服務探測結果
print(f"主機 {target_host} 的服務探測結果：")
for service in discovered_services:
    print(f"Port: {service['port']}")
    print(f"Protocol: {service['protocol']}")
    print(f"State: {service['state']}")
    print(f"Product: {service['product']}")
    print(f"Version: {service['version']}")
    print("---")
