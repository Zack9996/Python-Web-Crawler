import nmap

def discover_os(target_host):
    # 初始化nmap端口掃描器
    nm = nmap.PortScanner()

    # 執行操作系統探測
    nm.scan(target_host, arguments='-O')

    # 獲取主機的操作系統探測結果
    os_match = nm[target_host]['osmatch']
    if os_match:
        best_os_match = os_match[0]
        os_family = best_os_match['osclass'][0]['osfamily']
        os_gen = best_os_match['osclass'][0]['osgen']
        os_accuracy = best_os_match['accuracy']
        os_vendor = best_os_match['osclass'][0]['vendor']
        os_type = best_os_match['osclass'][0]['type']
        os_version = best_os_match['osclass'][0].get('osversion', 'Unknown')
        
        return {
            'os_family': os_family,
            'os_gen': os_gen,
            'os_accuracy': os_accuracy,
            'os_vendor': os_vendor,
            'os_type': os_type,
            'os_version': os_version
        }
    
    return None

# 主機地址
target_host = '192.168.70.124'

# 執行操作系統探測
os_info = discover_os(target_host)

# 輸出操作系統探測結果
if os_info:
    print(f"主機 {target_host} 的操作系統探測結果：")
    print(f"Family: {os_info['os_family']}")
    print(f"Generation: {os_info['os_gen']}")
    print(f"Accuracy: {os_info['os_accuracy']}")
    print(f"Vendor: {os_info['os_vendor']}")
    print(f"Type: {os_info['os_type']}")
    print(f"Version: {os_info['os_version']}")
else:
    print(f"無法識別主機 {target_host} 的操作系統。")
