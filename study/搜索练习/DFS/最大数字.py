import sys
input = lambda : sys.stdin.readline().strip()
N,A,B = map(int,input().split())
sN = str(N)
res = 0
def dfs(i,n,a,b):
  global res
  if i == len(sN):
    res = max(res,n)
    return
  x = int(sN[i])
  d = min(9-x,a)
  dfs(i+1,n*10+(x+d),(a-d),b)
  if b >= x+1:
    dfs(i+1,n*10+9,a,b-(x+1))
dfs(0,0,A,B)
print(res)











'''给定一个正整数 
N
N 。你可以对 
N
N 的任意一位数字执行任意次以下 2 种操 作：

将该位数字加 1 。如果该位数字已经是 9 , 加 1 之后变成 0 。

将该位数字减 1 。如果该位数字已经是 0 , 减 1 之后变成 9 。

你现在总共可以执行 1 号操作不超过 
A
A 次, 2 号操作不超过 
B
B 次。 请问你最大可以将 
N
N 变成多少?

输入格式'''