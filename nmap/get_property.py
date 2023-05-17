import nmap

def asset_scan(target_subnet):
    # 初始化 nmap.PortScanner
    nm = nmap.PortScanner()

    # 設置掃描參數
    scan_arguments = '-sn'  # -sn 表示僅掃描主機存活狀態，不掃描端口

    # 執行資產掃描
    nm.scan(target_subnet, arguments=scan_arguments)

    # 獲取掃描結果
    scan_results = nm.all_hosts()

    # 輸出掃描結果
    for host in scan_results:
        print(f"主機: {host}")
        print(f"狀態: {nm[host].state()}")
        print("------")

# 目標子網段
target_subnet = '192.168.70.124'  # 替換成你想要掃描的子網段

# 執行資產掃描
asset_scan(target_subnet)
