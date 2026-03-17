import sys
input = lambda:sys.stdin.readline().strip()
write = lambda x : sys.stdout.write(str(x)+'\n')

S = input()
L = len(S)

i_i = True
for i in range(L//2):
    if  S[i] != S(L-i-1):
        i_i = False
        break
write(i_i)













'''输入一个字符串，判断它是不是“回文”（即正着读和反着读都一样，比如 racecar 或 上海自来水来自海上）。
要求：

不要直接用 Python 的 s[::-1]（那个太简单了，练不到基础）。

请使用一个 for 循环，通过索引 i 去对比字符串头部和尾部对应的字符是否相等。

只要有一对不等，就审计失败。'''