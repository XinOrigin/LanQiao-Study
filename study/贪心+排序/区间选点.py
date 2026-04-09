import sys
input =lambda : sys.stdin.readline().strip()
N = int(input())
da = [list(map(int,input().split()))  for _ in range(N)]
da.sort(key = lambda x : x[1] )

def solve():
    last = -float('inf')
    res =0
    for i in da:
    if  i[0] > last:
        last = i[1]
        res +=1
    else:
        continue
solve()






'''
题目 15：区间选点 (经典贪心)描述： 给定 $N$ 个闭区间 $[a_i, b_i]$。请在数轴上选择尽量少的点，使得每个区间内至少包含一个你选择的点。任务： 输出最少需要选择的点数。
'''