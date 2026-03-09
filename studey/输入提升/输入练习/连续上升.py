import sys
input = lambda : sys.stdin.readline().strip()
write = lambda x : sys.stdout.write(str(x)+"\n")

temps = list(map(int,input().split()))
n=len(temps)
res=[]
a=1
for i in range(n-1):
    if temps[i+1]>temps[i]:
        a+=1
    else:
        res.append(a)
        a=1
res.append(a)
result = max(res)
write(result) 









'''
给定一个整数列表 temps，请找出连续上升最长的一段是多少天

'''