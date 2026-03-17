import sys
input = lambda : sys.stdin.readline().strip()
write = lambda x : sys.stdout.write(str(x)+'\n')
N,M=map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N) ]


for i in range(M):
    res = []
    for j in range(N):
        res.append(data[j][i])
    write(res)







'''题目：矩阵转置输入两个整数 $N, M$，
代表一个 $N$ 行 $M$ 列的矩阵。
读入这个矩阵。输出它的转置矩阵（
原本的行变列，列变行，结果是 $M$ 行 $N$ 列）。'''