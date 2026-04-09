import sys
input = lambda : sys.stdin.readline().strip()
n = int(input())
t = list(map(int,input().split()))
t.sort

tot =0
for i in range(n):
    tot +=t[i]*(n-i-1)

avg = tot/n
print(f'{avg:2f}')
  




'''
描述： 有 $n$ 个人排队到 1 个水龙头打水，第 $i$ 个人装满水桶的时间是 $t_i$。
任务： 请问如何安排他们的排队顺序，使得所有人的平均等待时间最小？
'''