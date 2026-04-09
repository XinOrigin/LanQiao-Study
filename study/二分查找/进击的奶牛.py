import sys
input = lambda : sys.stdin.readline().strip()

def solve():
    n,c = map(int,input().split())

    stalls = list(map(int,input().split()))
    stalls.sort()
    def check(d):
        count =1
        l = stalls[0]
        for i in range(1,n):
            if stalls[i] - l >=d:
                count+=1
                l = stalls[i]
        return count>=c
    
    lo =1
    hi =stalls[-1] -stalls[0]
    ans = 0
    while lo<=hi:
        i = (lo+hi)>>1
        if check(i):
            ans = i
            lo = i+1
        else:
            hi = i-1
    print(ans)
solve()









'''
题目 14：进击的奶牛 (经典二分答案)
描述： 农夫约翰有 $N$ 个牛栏，坐标在 $x_1, \dots, x_N$。他有 $C$ 头牛，要放进这些牛栏里。为了不让牛打架，他希望任意两头牛之间的最近距离尽可能大。
任务： 求这个最大的最近距离。
'''