import sys
input = lambda: sys.stdin.readline().strip()
write = lambda x : sys.stdout.write(str(x)+"\n")
n,m=map(int,input().split())

count = {}

for _ in range(n):
    row = list(map(int,input().split()))
    
    min_rep = row
    for i in range(1,m):
        current = row[i:] + row[:i]
        if current < min_rep:
            min_rep = current 
    identity = tuple(min_rep)
    count[identity]=count.get(identity,0)+1

if count:
    res = max(count.values())
    write(res)
else:
    write(0)














'''
📂 试题 E：吊坠 —— 逻辑拓扑【问题背景】小蓝有 $n$ 个吊坠，
每个吊坠由 $m$ 个宝石组成，宝石排成一个环形。每个宝石有一个颜色编号。
如果两个吊坠通过旋转后，对应位置的宝石颜色完全相同，我们就认为这两个
吊坠是“同款”的。目标：给定 $n$ 个吊坠，请问这堆吊坠中，“同款”吊
坠最多有多少个？【样例输入】Plaintext
3 4
1 2 3 4
4 3 2 1
2 3 4 1
【样例输出】Plaintext2
（解释：1 2 3 4 旋转后可以变成 2 3 4 1，所以它们是同款；
而 4 3 2 1 无论怎么转都变不成它们，所以最多有 2 个同款。）


'''