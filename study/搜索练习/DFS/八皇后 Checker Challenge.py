import sys
input = lambda : sys.stdin.readline().strip()
n = int(input())
cols = [False] *n
add = [False] * (2*n)
sub = [False] * (2*n)
ans = 0
path = []
def dfs(r):
    global ans
    if r == n:
        ans+=1
        if ans <=3:
            print(*path)
        
        return
    for c in range(n):
        if cols[c]== False and add[r+c] == False and sub[r-c+n] == False:
            cols[c] = True
            add[r+c] = True
            sub[r-c+n] = True
            path.append(c+1)
            dfs(r+1)
            cols[c] = False
            add[r+c] = False
            sub[r-c+n] = False
            path.pop()
dfs(0)
print(ans)


        
    