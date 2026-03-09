import sys
input = lambda : sys.stdin.readline().strip()
write = lambda x : sys.stdout.write(str(x)+'\n')
data = list(map(str,input().split()))
res = {} 
for i,ip in enumerate(data):
    if ip not in res :
        res[ip] = []
    res[ip].append(i)
write(res)


















'''
背景：在维护局域网或服务器集群时，我们需要快速定位哪些设备正在使用相同的 IP 地址，以及它们在日志文件中的具体位置。

任务：给定一个包含 IP 地址（字符串）的列表 ips，请输出一个字典。

Key (键)：IP 地址。

Value (值)：一个列表，存放该 IP 在原始列表中出现的所有下标（索引）。
'''