n=4
cols = [False] *n
add = [False] * (2*n)
sub = [False] * (2*n)
res = []
board = [['.' for _ in range(n)] for _ in range(n)]

def dfs(r):
    if r == n:
        res.append([''.join(row) for row in board])
        return
    for c in range(n):
        if cols[c] == False and add[r+c]==False and  sub[r-c+n]==False:

            board[r][c] = 'Q'
            cols[c] = True
            add[r+c]=True
            sub[r-c+n]=True
            dfs(r+1)
            cols[c] = False
            add[r+c]=False
            sub[r-c+n]=False
            board[r][c] = '.'
dfs(0)
for ros in res:
    for i in ros:
        print(i)















'''

在之前的数字搜索里，你只需要检查“和”够不够。
但在 N 皇后问题中，你每放一个棋子，
都会在地图上拉起好几道“警戒线”：同行、同列、同对角线、
同反对角线都不能再放棋子。
1. 核心心法：上帝视角与降维打击如果是 $N \times N$ 的棋盘，
我们要放 $N$ 个皇后。上帝视角：每一行必须且只能放一个皇后
。所以我们不需要二维搜索，只需要按“行”深度搜索。降维打击：
列约束：用一个 used_cols 数组记录哪一列被占了。对角线约束
：这是最巧妙的地方！主对角线：在同一条主对角线上的点，其坐标
满足 $row - col = constant$。为了防止负数，我们通常记为 $
row - col + n$。反对角线：在同一条反对角线上的点，其坐标
满足 $row + col = constant$。




'''