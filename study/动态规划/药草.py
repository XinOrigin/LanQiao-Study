import sys
input = lambda : sys.stdin.readline().strip()
T,M = map(int,input().split())
t,v = [0]*(M+1),[0]*(M+1)
for i in range(1,M+1):
    t[i],v[i] = map(int,input().split())
f = [[0]*(T+1) for _ in range(M+1)]
for i in range(1,T+1):
    for j in range(1,M+1):
        if i>= t[j]:
            f[j][i] = max(f[j-1][i],f[j-1][i-t[j]]+v[j])
        else:
            f[j][i] = f[j-1][i]
print(f[M][T])