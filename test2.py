from xtlsapi import XrayClient


xray = XrayClient("127.0.0.1", 53357)


print(xray.stats_online_ip_list("1"))
