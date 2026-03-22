import sys
input = lambda : sys.stdin.readline().strip()
write = lambda x : sys.stdout.write(str(x)+'\n')

N = int(input())

data = [list(map(int,input().split())) for _ in range(N) ]

for i in range(N):
    res = []
    for j in range(N):
        res.append(data[j][i])
    res.reverse()
    print(*(res))



'''输入一个 $N \times N$ 的方阵，输出它顺时针旋转 90 度后的结果。
逻辑审计提示：观察一个 $3 \times 3$
 的矩阵旋转：(0, 0) 搬到了 (0, 2)(0, 1) 搬到了 (1, 2)(0, 2) 
 搬到了 (2, 2)规律：原矩阵的第 $i$ 行，变成了新矩阵的第 $N-1-i$ 列。
 或者更简单的写法：原矩阵的第 $j$ 列，倒序过来，变成了新矩阵的第 $j$ 行。'''