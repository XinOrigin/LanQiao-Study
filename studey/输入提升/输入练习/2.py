import sys
input = lambda : sys.stdin.readline().strip()
write = lambda x : sys.stdout.write(str(x)+"\n")
n = int(input())
nums = list(map(int, input().split()))
count = 0
for x in nums:
    if x>0 and (x & (x-1))==0:
        count+=1
write(str(count))

'''
小蓝认为一个数字如果能表示为 若干个（至少两个）连续正整数相加，它就是“有诗意的”。
比如：$6 = 1 + 2 + 3$（有诗意）$3 = 1 + 2$（有诗意）$8$（无法表示，缺乏诗意）现在给你 $n$ 个数字，请问最少删除多少个数字，才能让剩下的数字都有诗意？（其实就是问：这 $n$ 个数里，有多少个是不满足条件的数字？） 

输入
3
3 6 8

输出
1 


'''