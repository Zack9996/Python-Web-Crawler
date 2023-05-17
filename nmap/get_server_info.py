import nmap

# 初始化主機掃描器
nm = nmap.PortScanner()

# 掃描主機
target_host = '192.168.70.124'
nm.scan(target_host, arguments='-O')

# 獲取主機訊息
host = nm[target_host]

# 打印主機訊息
print(f"主機: {host.hostname()}")
print(f"狀態: {host.state()}")
os_match_prob = host.get('osmatch', [])
if os_match_prob:
    for os_match in os_match_prob:
        os_family = os_match.get('osclass')[0].get('osfamily')
        os_gen = os_match.get('osclass')[0].get('osgen')
        print(f"操作系統: {os_family} - {os_gen}")
else:
    print("操作系統訊息不可用")
print(f"MAC地址: {host['addresses']['mac']}")