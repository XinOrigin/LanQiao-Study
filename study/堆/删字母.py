import sys
from heapq import *
input = lambda : sys.stdin.readline().strip()
n,m = map(int,input().split())
s = input()

hq = []
res = ''
L=0
for i in range(m):
  heappush(hq,(s[i],i))
for R in range(m,n):
  heappush(hq,(s[R],R))
  mn,mni = heappop(hq)
  while mni<L:
    mn,mni = heappop(hq)
  res += mn
  L = mni +1
print(res)


'''
问题描述
给定一个由大写字母组成的长度为 
n
n 的字符串，请在字符串中删除 
m
m 个字符，使得剩下的字符串的字典序最小。

输入格式
输入的第一行包含两个整数 
n
,
m
n,m ，用一个空格分隔。

第二行包含一个长度为 
n
n 的字符串。

输出格式
输出一行包含一个长为 
n
−
m
n−m 的字符串，表示答案。

样例输入
7 3
LANQIAO
copy
样例输出
AIAO

'''