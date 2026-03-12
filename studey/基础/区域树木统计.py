import sys
input = lambda : sys.stdin.readline().strip()
write = lambda x : sys.stdout.write(str(x)+'\n')
L,M= map(int,input().split())

data = [True] * (L+1)
for _ in range(M) :
    u,v= map(int,input().split())
    for i in range(u,v+1):
        data[i] = False
        

trees = data.count(True)
write(trees)








'''

题目描述：某校门口有一条马路，长度为 $L$。
马路的一侧从起点（$0$ 点）到终点（$L$ 点）每隔 $1$ 
米有一棵树，即一共有 $L+1$ 棵树。现在马路上有 $M$ 
个区域要修地铁。每个区域由起始点 $u$ 和终止点 $v$ 组成
（$0 \le u \le v \le L$）。这些区域可能会互相重叠。
凡是在这些区域内的树（包括区域的端点），都要被砍掉。请你计算，
最后马路上还剩多少棵树？
输入格式：第一行两个整数 $L$（马路长度）和 $M$（区域个数）。
接下来的 $M$ 行，每行两个整数 $u$ 和 $v$，
代表一个要砍树的闭区间 $[u, v]$。输出格式：一个整数，代表剩余树的数量。

'''