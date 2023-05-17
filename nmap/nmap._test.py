# import nmap

# # 初始化端口掃描器
# nm = nmap.PortScanner()

# # 設置掃描參數
# scan_arguments = '-F -sV -O'
# target_host = '192.168.70.124'

# # 執行綜合掃描
# scan_results = nm.scan(target_host, arguments=scan_arguments)

# # 輸出掃描結果
# for host, result in scan_results['scan'].items():
#     print(f"主機: {host}")
#     print(f"狀態: {result['status']['state']}")
    
#     if 'osmatch' in result:
#         os_info = result['osmatch'][0]
#         print(f"操作系統: {os_info['name']} ({os_info['accuracy']}%準確度)")
    
#     if 'tcp' in result:
#         for port, port_data in result['tcp'].items():
#             print(f"端口: {port}")
#             print(f"服務: {port_data['name']}")
#             print(f"狀態: {port_data['state']}")
#             print(f"版本: {port_data['version']}")
    
#     print("------------------------------")


import nmap

# 初始化端口掃描器
nm = nmap.PortScanner()

# 設置掃描參數
scan_arguments = '-p- -sV -O'
target_host = '192.168.70.124'

# 執行綜合掃描
scan_results = nm.scan(target_host, arguments=scan_arguments)

# 輸出掃描結果
for host, result in scan_results['scan'].items():
    print(f"主機: {host}")
    print(f"狀態: {result['status']['state']}")
    
    if 'osmatch' in result:
        os_info = result['osmatch'][0]
        print(f"操作系統: {os_info['name']} ({os_info['accuracy']}%準確度)")
    
    if 'tcp' in result:
        for port, port_data in result['tcp'].items():
            print(f"端口: {port}")
            print(f"服務: {port_data['name']}")
            print(f"狀態: {port_data['state']}")
            print(f"版本: {port_data['version']}")
            print("------------------------------")
    
    # print("------------------------------")
