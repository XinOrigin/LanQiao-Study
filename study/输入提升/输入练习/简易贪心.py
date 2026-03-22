import sys
input = lambda : sys.stdin.readline().strip()
write = lambda x : sys.stdout.write(str(x)+'\n')

data = list(map(int,input().split()))
reach_max = 0
for i in range(len(data)-1):
    if data[i] >0 and data[i]+i > reach_max and i<=reach_max:
        reach_max = data[i]+i
if reach_max+1 >= len(data):
    print(True)
else:
    print(False)        
        










'''

最后一题：简易版“跳一跳”（逻辑模拟/贪心）

任务描述：
你有一个非负整数列表 steps，你在下标 0 的位置。每个元素代表你在该位置最大能跳跃的步数。
判断你能不能跳到最后一个下标？

输入 A：[2, 3, 1, 1, 4]

过程：在 0 位跳 1 步到 1 位，在 1 位直接跳 3 步到 4 位。成功！

输入 B：[3, 2, 1, 0, 4]

过程：无论你怎么跳，最终都会落在下标 3（值是 0）的地方，再也跳不动了。失败！

'''