import sys
input = lambda :sys.stdin.readline().strip()
T,M = map(int,input().split())
dp =[0] *(T+1)
for _ in range(M):
    w,v=map(int,input().split())
    for j in range(T,w-1,-1):
        if dp[j-w] + v > dp[j]:
            dp[j] = dp[j-w]+v
    print(dp[T])