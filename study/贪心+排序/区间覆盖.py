import sys
input =lambda : sys.stdin.readline().strip()
S,T = map(int,input().split())
N=int(input())
da = [list(map(int,input().split())) for _ in range(N)]
da.sort(key = lambda x :x[0])
def solve():
    res = 0
    su = False
    i=0
    while i<N:
        
        last = -float('inf')
        while S<T and da[i][0] <=S:
            last = max(last,da[i][1])
            i+=1
        if last <= S:
            break
        res+=1
        S = last
        if S>=T:
            su = True
            break
    if su:
        print(res)
    else:
        print(-1)
solve()

            