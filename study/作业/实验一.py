'''1、 定义变量a = 10, b = 3.14, c = "Hello", d = True,使用type()函数打印每个变量的数据类型。
'''
# a,b,c,d=10,3.14,"Hello",True

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


# '''2、	计算0.1+0.2并直接打印结果，观察是否等于0.3。
# 使用round()函数或格式化字符串，使其输出看起来等于0.3，
# 解释为什么直接比较0.1+0.2==0.3会返回False。'''
# print(0.1+0.2)
# print(round(0.1+0.2,1))
# print('因为十进制小数在二进制形式储存时,无法精确表示有误差')


# '''3、	定义变量name = "小明"、age = 18，使用f-string 输出：我的名字是小明，今年18岁。'''
# name = "小明"
# age = 18
# print(f'我的名字是{name}，今年{age}岁')

# 4、 定义变量 math_score = 95.5、english_score = 88.0，
# 使用f-string输出两门成绩以及平均分（保留 1 位小数），
# 格式：数学95.5分，英语88.0分，平均分91.8分。
# math_score = 95.5
# english_score = 88.0
# print(f'数学分{math_score}，英语{english_score}分，平均{round((math_score+english_score)/2,1)}分')

# 5、	定义变量 price = 129.99、discount = 0.75，计算折后价，
# 用f-string输出：原价：¥129.99，折扣：75折，折后价：¥97.49。
# price = 129.99
# discount = 0.75
# print(f'原价：¥{price}，折扣：{int(discount*100)}折，折后价：¥{round(price*discount,2)}。')

# 6、	定义三个变量name、age、height，为变量赋值，
# 输出：我叫{name}，今年{age}岁，身高{height}米。
# 练习使用%，format，f-string方法实现。
# name='张三'
# age=18
# height=1.81
# print("我叫%s，今年%d岁，身高%.2f米" % (name, age, height))
# print("我叫{}，今年{}岁，身高{}米".format(name, age, height))
# print(f"我叫{name}，今年{age}岁，身高{height}米")

# 7、	用f-string格式化输出：3.14159 保留两位小数。
# num = 3.14159
# print(f"{num:.2f}")  

# 8、	定义变量 pi = 3.1415926，使用格式化字符串输出：
# 1）保留 2 位小数："圆周率保留2位小数是：3.14"；
# 2）保留 4 位小数，且总宽度为 8（不足补空格）："圆周率： 3.1416"；
# 3）用科学计数法表示，保留 2 位小数："圆周率（科学计数法）：3.14e+00"
# pi = 3.1415926
# print(f"圆周率保留2位小数是：{pi:.2f}")
# print(f"圆周率：{pi:8.4f}")
# print(f"圆周率（科学计数法）：{pi:.2e}")

# 9、	定义变量 year=2026, month=3, day=12，格式化输出日期为："2026-03-12"（月份和日期不足 2 位补 0）；
# year = 2026
# month = 3
# day = 12
# print(f"{year:04d}-{month:02d}-{day:02d}")


# 10、	预想15 + 7, 15 - 7, 15 * 7, 15 / 7, 15 // 7, 15 % 7, 15 ** 2的结果，并编写程序验证，打印出结果。
# a = 15
# b = 7
# print(f"15 + 7 = {a + b}")       
# print(f"15 - 7 = {a - b}")      
# print(f"15 * 7 = {a * b}")       
# print(f"15 / 7 = {a / b}")  
# print(f"15 // 7 = {a // b}")    
# print(f"15 % 7 = {a % b}")      
# print(f"15 ** 2 = {a ** b}")    


# 11、	给定一个三位数（如 123），分别提取其百位、十位、个位数字并输出（例如：百位1，十位2，个位3）
# num = 123
# bai = num // 100     
# shi = num // 10 % 10  
# ge = num % 10         
# print(f"百位{bai}，十位{shi}，个位{ge}")

# 12、	给定一个人的身高（单位：米）和体重（单位：千克），
# 计算 BMI 指数（BMI = 体重 / 身高 ²），并输出结果（保留 2 位小数）
# height = 1.81 
# weight = 75    
# bmi = weight / (height ** 2)
# print(f"BMI = {bmi:.2f}")

# 13、	给定两个整数a和b，交换两个变量的值。
# a = 10
# b = 20
# a, b = b, a
# print(f"a = {a}, b = {b}")


# 14、	预想表达式10 > 5 and 3 < 7 or not (6 == 6)的结果，并使用编程验证。
# 预期结果：True and True or False
# True


result = 10 > 5 and 3 < 7 or not (6 == 6)
print(result)  


