import os
import psutil


# 判断进程是否在运行
def judgeprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            return True
    else:
        return False

"""
禁用无线网卡：netsh interface set interface wlan0 disabled

启用无线网卡：netsh interface set interface wlan0 enabled

禁用有线网卡：netsh interface set interface eth0 disabled

启用有线网卡：netsh interface set interface eth0 enabled
"""
# 0 是成功， 1是失败
result = os.system(r"ipconfig")
print(result)

result = os.popen("C:\\Users\\ASUS\\Desktop\\1.txt")
print(result)

result = os.system(r"ipconfig")
print(result)

print(judgeprocess("smartgit.exe"))