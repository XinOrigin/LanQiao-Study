import sys
input = lambda : sys.stdin.readline().strip()
N,K =map(int,input().split())
c = [list(map(int,input().split())) for _ in range(N)]
def bisect(a,x,lo=0,hi=None,check = lambda y : y ):
    if hi is None:hi = len(a)
    while lo<hi:
        i = (lo+hi) >> 1
        if check(a[i]) < x :
            hi = i
        else:
            lo = i +1
    
    return lo
def check(x):
    res = 0
    for h,w in c:
        res+=(h//x) * (w//x)
    return res
a =range(1,100001)
print(a[bisect(a,K,check=check)-1])