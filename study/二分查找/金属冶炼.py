import sys
input = lambda :sys.stdin.readline().strip()
n = int(input())
a,b = zip (* [map(int,input().split()) for _ in range(n)])


def bisect(lo, hi , check):
  while lo < hi :
    i = lo +hi >> 1
    if check(i):
      hi = i
    else:
      lo = i+1
  return lo


m = bisect(1 , 10**10,lambda v:all(A/v <= B for A,B in zip(a,b)))
M = bisect(1 , 10**10,lambda v:any(A/v < B for A,B in zip(a,b)))
print(m,M)








'''
问题描述
小蓝有一个神奇的炉子用于将普通金属 
O
O 冶炼成为一种特殊金属 
X
X。这个炉子有一个称作转换率的属性 
V
V，
V
V 是一个正整数，这意味着消耗 
V
V 个普通金属 
O
O 恰好可以冶炼出一个特殊金属 
X
X，当普通金属 
O
O 的数目不足 
V
V 时，无法继续冶炼。

现在给出了 
N
N 条冶炼记录，每条记录中包含两个整数 
A
A 和 
B
B，这表示本次投入了 
A
A 个普通金属 
O
O，最终冶炼出了 
B
B 个特殊金属 
X
X。每条记录都是独立的，这意味着上一次没消耗完的普通金属 
O
O 不会累加到下一次的冶炼当中。

根据这 
N
N 条冶炼记录，请你推测出转换率 
V
V 的最小值和最大值分别可能是多少，题目保证评测数据不存在无解的情况。

输入格式
第一行一个整数 
N
N，表示冶炼记录的数目。

接下来输入 
N
N 行，每行两个整数 
A
A、
B
B，含义如题目所述。

输出格式
输出两个整数，分别表示 
V
V 可能的最小值和最大值，中间用空格分开。
'''