import sys
input = lambda: sys.stdin.readline().strip()

def solve():
    n = int(input())
    ka, kb = map(int, input().split())
    
    ministers = []
    for i in range(1, n + 1):
        # 存入：[左手, 右手, 原始编号]
        a, b = map(int, input().split())
        ministers.append([a, b, i])

    # 1. 贪心排序：按 a * b 乘积排
    ministers.sort(key=lambda x: x[0] * x[1])

    current_a = ka
    max_reward = -1
    target_minister_id = -1 # 记录拿最高奖的大臣编号

    for a, b, idx in ministers:
        reward = current_a // b
        
        # 2. 动态更新最大值和对应的 ID
        if reward > max_reward:
            max_reward = reward
            target_minister_id = idx
            
        current_a *= a
        
    print(f"最大奖赏金额: {max_reward}")
    print(f"拿到这个奖赏的大臣原始编号是: {target_minister_id}")

solve()







'''
描述： 国王和大臣排队。国王左右手写着 $a_0, b_0$。每个大臣 $i$ 左右手写着 $a_i, b_i$。
每个大臣领到的奖赏 = 他前面所有人左手数字的乘积 / 他自己右手的数字。
任务： 重新排列大臣的顺序，使得奖赏最高的那个大臣领到的奖赏最少。
'''