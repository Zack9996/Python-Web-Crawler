import nmap

def 漏洞掃描(目標主機):
    nm = nmap.PortScanner()

    # 掃描所有端口
    nm.scan(目標主機, arguments='-p-')

    # 遍歷每個端口進行漏洞掃描
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            print(f"主機: {host}")
            for port in nm[host]['tcp']:
                port_info = nm[host]['tcp'][port]
                if port_info['state'] == 'open':
                    print(f"掃描到開放端口: {port}")
                    print(f"端口狀態: {port_info['state']}")
                    print(f"服務信息: {port_info['name']}")

                    # 檢查是否存在漏洞腳本
                    if 'script' in nm[host]['tcp'][port]:
                        print("進行漏洞掃描：")
                        for script_result in nm[host]['tcp'][port]['script']:
                            print(f"漏洞名稱: {script_result['id']}")
                            print(f"漏洞描述: {script_result['output']}")
                            print()
                    else:
                        print("未找到與該端口相關的漏洞腳本")
                    print()

# 指定目標主機進行掃描和漏洞掃描
目標主機 = '192.168.70.124'
漏洞掃描(目標主機)


