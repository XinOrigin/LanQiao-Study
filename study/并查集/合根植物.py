import sys
input = lambda : sys.stdin.readline().strip()

m,n =map(int,input().split())
k = int(input())
fa = list(range(m*n+1))
def find(x):
  if fa[x]==x:return x
  fa[x]=find(fa[x])
  return fa[x]
def union(u,v):
  if find(v)!= find(u):
    fa[find(u)]=find(v)
for _ in range(k):
  u,v = map(int,input().split())
  union(u,v)
for i in range(1,n*m+1):
  fa[i]=find(i)
print(len(set(fa))-1)

'''
合根植物

题目描述
w
w 星球的一个种植园，被分成 
m
×
n
m×n 个小格子（东西方向 
m
m 行，南北方向 
n
n 列）。每个格子里种了一株合根植物。

这种植物有个特点，它的根可能会沿着南北或东西方向伸展，从而与另一个格子的植物合成为一体。

如果我们告诉你哪些小格子间出现了连根现象，你能说出这个园中一共有多少株合根植物吗？

输入描述
第一行，两个整数 
m
,
n
m,n，用空格分开，表示格子的行数、列数（
1
≤
m
,
n
≤
1000
1≤m,n≤1000）。

接下来一行，一个整数 
k
k (
0
≤
k
≤
1
0
5
0≤k≤10 
5
  )，表示下面还有 
k
k 行数据。

接下来 
k
k 行，每行两个整数 
a
，
b
a，b，表示编号为 
a
a 的小格子和编号为 
b
b 的小格子合根了。

格子的编号一行一行，从上到下，从左到右编号。

比如：
5
×
4
5×4 的小格子，编号：

1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
17 18 19 20
copy
输出描述
输出植物数量。

输入输出样例
示例
输入

5 4
16
2 3
1 5
5 9
4 8
7 8
9 10
10 11
11 12
10 14
12 16
14 18
17 18
15 19
19 20
9 13
13 17
copy
输出

5
copy
样例说明

其合根情况参考下图：



运行限制
最大运行时间：2s
最大运行内存: 256M
'''