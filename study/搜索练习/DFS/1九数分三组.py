data=[1, 2, 3, 4, 5, 6, 7, 8, 9]
res = []
for i in data:
    for j in data:
        for k in data:
            a = i*100+j*10+k
            if a<=333 :
                s = str(a)+str(2*a)+str(3*a)
                if len(s)==9 and '0' not in s and len(set(s))==9:
                    res.append(a)
            
print(res)
'''
res = []
for a in range(123,334):
    b=2*a
    c=3*a
    s=str(a)+str(b)+str(c)
    if len(s)==9 and '0'not in s and len(set(s))==9:
        res.append(a)
print(res)
'''







'''
任务描述：将 $1, 2, 3, 4, 5, 6, 7, 8, 9$
 这九个数字分成三组，每个数字只能用一次，组成三个三位数。
 要求这三个三位数的比例恰好是 $1:2:3$。请输出所有满足条件的三个三位数。
'''