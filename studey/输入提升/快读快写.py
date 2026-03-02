import sys
sys.setrecursionlimit(1000000)#优化深度
input = lambda:sys.stdin.readline().strip()#快读
write = lambda x:sys.stdout.write(str(x)+"\n")#快写
n = int(input())#读入个数
nums = list(map(int,input().split()))#读入数据
res = sum(x for x in nums if x>10)#筛选加求和
write(res)#打印