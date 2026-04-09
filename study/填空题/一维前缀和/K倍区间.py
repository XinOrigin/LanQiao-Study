# n**2
import sys
input = lambda : sys.stdin.readline().strip()
n = int(input())
a = [0] + list(map(int,input().split()))
k = int(input())
s= [0] * (n+1)
for i in range(1,n+1):
    s[i] = s[i-1] + a[i-1]
ans=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if s[j]-s[i-1]  % k ==0 :
            ans+=1
print(ans)

#o(n)
import sys
input = lambda : sys.stdin.readline().strip()
n = int(input())
a = [0] + list(map(int,input().split()))
k = int(input())
cnt = [0] * k
cnt[0] =1
s= 0
ans= 0
for i in range(1,n+1):
    s=(s+a[i])%k
    ans += cnt[s]
    cnt[s] +=1
print(ans)


import sys
input = lambda: sys.stdin.readline().strip()
def qwe():
    n,k = map(int,input().split())
    cnt = [0]*k
    cnt[0] = 1
    s=0
    ans=0
    for _ in range(n):
        val = int(input())
        s = (s+val) %k
        ans += cnt[s]
        cnt[s] +=1
    print(ans)
qwe()