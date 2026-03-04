import sys
input = lambda:sys.stdin.readline().strip()
write = lambda x : sys.stdout.write(str(x)+"\n")
n=int(input())
a=list(map(int,input().split()))
diff_list=[]
for i in range(n//2):
    gap=a[i]-a[n-i-1]
    diff_list.append(gap)
ans=0
if not diff_list:
    write(0)
    sys.eixt()
ans = abs(diff_list[0])
for i in range(0,len(diff_list)-1):
    if diff_list[i]*diff_list[i+1]>0:
        ans+=max(0,abs(diff_list[i+1])-abs(diff_list[i]))
    else:
        ans+=abs(diff_list[i+1])
write(str(ans))










r'''
给你一个长度为 $n$ 的数组。你可以执行两种操作：批量补丁（范围操作）：指定相邻的两个数，
同时加 1 或减 1。单机热更（单点操作）：指定一个数加 1 或减 1。目标：用最少的操作次数，
把数组变成“回文数组”（即首尾对应相等：$a_1 = a_n, a_2 = a_{n-1} \dots$）。
'''