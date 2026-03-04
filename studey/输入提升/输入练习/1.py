import sys
input = lambda : sys.stdin.readline().strip()
write = lambda x : sys.stdout.write(str(x)+"\n")
n = int(input())
data = [[-int(line[1]),line[0]] for line in ((input().split()) for _ in range(n))]
data.sort()
r = 1
for score,name in data[:3]:
    score = -score
    write(str(r)+"."+str(name) +" ("+str(score)+"%)")
    r+=1


'''
4
Node-A 45
Node-C 80
Node-B 80
Gateway 10



输出
1. Node-B (80%)
2. Node-C (80%)
3. Node-A (45%)

'''
