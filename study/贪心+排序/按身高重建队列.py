import sys
input =lambda : sys.stdin.readline().strip()
n = int(input())
people = [list(map(int,input().split())) for _ in range(n)]
people.sort(key=lambda x:(-x[0],x[1]))
res = []
for i,p in enumerate(people):
    h,k=p[0],p[1]
    if i == k:
        res.append(p)
    elif k<i:
        res.insert(k,p)
print(res)