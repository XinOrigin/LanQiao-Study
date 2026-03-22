# 1、将下列式子写出Python表达式：
# 1)	5+ (2*3)*2；
# 2)	2a(b+5)，其中a=2; b=3。

# print(5 + (2*3)*2)
# a = 2; b = 3
# print(2*a*(b+5))


# 2、先用手工计算下列表达式的值，然后在交互式命令窗口中实验这些表达式的输出结果：
# 1)	1 + 2**3 + 4 % 5 + (6 > 7) + 8 * 9
# 2)	not a <= c or 4 * c == b**2 and b != a + c    #(a=2; b=3; c=4)
# 3)	3 > a * b or a == c and b != c or c > d         #(a=2; b=3; c=4;d=5)

# print(1 + 2**3 + 4 % 5 + (6 > 7) + 8 * 9)    #85
# a=2; b=3; c=4
# print(not a <= c or 4 * c == b**2 and b != a + c)   #False  and>or
# a=2; b=3; c=4;d=5
# print(3 > a * b or a == c and b != c or c > d)   #False

# 3、使用 input() 依次获取用户的姓名、年龄和喜欢的颜色。然后使用 print() 输出一张“卡片”如下格式
# import sys 
# input = lambda : sys.stdin.readline().strip()
# name, age, color = input(), input(), input()
# print('----'*20)
# print(f"姓名: {name}\n年龄: {age}\n喜欢的颜色: {color}")
# print('----'*20)

# 提示用户输入矩形的“长”和“宽”（可能是小数）。
# 将输入的字符串转换为 float 类型，计算面积，
# 并使用 f-string 输出：“长为X，宽为Y的矩形面积是Z”。

# l, w = float(input('输入矩形的长:')), float(input('输入矩形的宽:'))
# print(f"长为{l}，宽为{w}的矩形面积是{l*w}")

# 5、输入两个整数 a 和 b，计算并输出 a+b、a-b、a*b、a/b（保留 2 位小数）、a% b、a**b 的结果
# a, b = int(input()), int(input())
# print(a+b, a-b, a*b, f"{a/b:.2f}", a%b, a**b)

# 6、输入圆的半径，计算圆的面积和周长。
# r = float(input())
# print(f"{3.14159*r*r:.2f}", f"{2*3.14159*r:.2f}")

# 7、输入摄氏温度 C，根据公式F = C * 9/5 + 32 转换为华氏温度 F 并输出，结果保留 1 位小数。
# print(f"{float(input())*9/5+32:.1f}")

# 8、输入一个数字字符串（如 "123.45"），将其转换为浮点数后加 10，再转换为整数输出。
# print(int(float(input())+10))

# 10、输入一个单个字符，使用ord()输出其 ASCII 码；
# print(ord(input()))
# print(chr(int(input())))

# 11、输入一个3位整数，通过算术运算符拆分出百位、十位、个位。
# n = int(input())
# print(n//100, n//10%10, n%10)

# 12、输入一个3位数整数，通过运算符判断其是否为回文数（如 121）。
# c = input()
# if c[::-1] == c:
#     print('是')
# else:
#     print('否')

# 13、BMI 计算：输入身高（米）和体重（千克），计算 BMI 指数（BMI = 体重 / (身高 × 身高)），并输出 “你的BMI指数为： ”。
# h, w = float(input('输入身高（米）')), float(input('输入体重（千克）'))
# print(f"你的BMI指数为：{w/h/h:.1f}")

