import sys 
input = lambda : sys.stdin.readline().strip()
write = lambda x : sys.stdout.write(str(x)+'\n')
N,M = map(int,input().split())
light = [False] * (N+1)
for i in range(1,M+1):
    for j in range(i,N+1,i):
         light[j] = not  light[j]


ans = light.count(True)
write(ans)


'''
题目：灯的开关状态审计有 $N$ 盏灯，编号 $1 \sim N$，
初始全部是关着的。有 $M$ 个人，第 1 个人把所有编号是 $1$ 的倍数的灯按一下（开变关，关变开）
；第 2 个人把所有编号是 $2$ 的倍数的灯按一下；...第 $M$ 个人把所有编号是 $M$ 的倍数的灯按一下
。请问：最后有多少盏灯是开着的？要求：同样使用列表（数组）来记录灯的状态。
思考一下：灯的编号是从 $1$ 开始的，你的数组打算开多大？not 运算符在这里会非常好用。

'''