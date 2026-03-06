def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True # 明确告诉系统：这是质数！

# 1. 扩充工具箱 (生成所有 pk)
move_set = set()
for i in range(2, 2001):
    if is_prime(i):
        curr = i
        while curr < 2000:
            move_set.add(curr)
            curr *= i
move = sorted(list(move_set))

# 2. 状态推导 (博弈核心)
win = [False] * 2001
for i in range(2, 2001):
    for m in move:
        if m > i: break
        # 如果能一步到达必败态(False)，那当前就是必胜态(True)
        if not win[i - m]:
            win[i] = True
            break

# 3. 提取并打印必败点
losing_points = [idx for idx, state in enumerate(win) if not state]
print("真正的必败点 (L) 名单：", losing_points)