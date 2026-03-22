import sys
input = lambda:sys.stdin.readline().strip()
write = lambda x:sys.stdout.write(str(x)+"\n")
n = int(input())
# data = [[-int(line[1]),line[0]] for line in (input().split() for _ in range(n))]#利用迭代器一行流
data = []
for _ in range(n):
    line = input().split()
    a = [-int(line[1]),line[0]]
    data.append(a)
data.sort()
for socre,name in data:
    socre = -socre
    write(name+' '+str(socre))