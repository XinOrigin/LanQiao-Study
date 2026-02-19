# import sys
# print('请输入正整数n')
# n = sys.stdin.readline().strip()
# if n:
#     line = int(n) 
# else1:
#     n=0
# i=0
# total_sum=0
# while (i<line):
#     a = int(sys.stdin.readline().strip())
#     total_sum += a
#     i+=1
# print(total_sum)



import sys
import time
import io

# 1. 物理准备：在内存中生成 100 万个数字的模拟输入流
data = "\n".join(map(str, range(1000000))) + "\n"

def test_input():
    # 模拟从 input() 读取
    sys.stdin = io.StringIO(data)
    start = time.time()
    count = 0
    try:
        while True:
            # input() 内部会处理提示词、剥离换行符等，损耗极大
            x = input()
            count += 1
    except EOFError:
        pass
    return time.time() - start

def test_readline():
    # 模拟从 sys.stdin.readline() 读取
    sys.stdin = io.StringIO(data)
    start = time.time()
    count = 0
    while True:
        # readline() 是原始管道读取，效率极高
        line = sys.stdin.readline()
        if not line:
            break
        count += 1
    return time.time() - start

print("正在启动性能审判...")
time_input = test_input()
print(f"input() 耗时: {time_input:.4f} 秒")

time_readline = test_readline()
print(f"sys.stdin.readline() 耗时: {time_readline:.4f} 秒")

print(f"\n结论：sys.stdin.readline() 比 input() 快了 {time_input / time_readline:.2f} 倍")