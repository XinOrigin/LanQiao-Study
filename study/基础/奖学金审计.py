import sys
input = lambda : sys.stdin.readline().strip()
write = lambda x : sys.stdout.write(str(x)+'\n')

N=int(input())

data = [list(map(int,input().split())) for _ in range(N)]
res1 = []
res2 = []
for i in range(N):
    res1 = []
    res1.append(i+1)
    res1.append(-(data[i][0]+data[i][1]+data[i][2]))
    res1.append(-(data[i][0]))
    res2.append(res1)
res2.sort()
for rank_info in res2:
    # 取反恢复成正数
    total_score = -rank_info[1]
    f_score = -rank_info[2]
    student_id = rank_info[0]
    print(f"学号: {student_id}, 总分: {total_score}, 首科: {f_score}")







'''

某校发放奖学金，评定标准如下：先按总分从高到低排序。如果总分相同，
按语文成绩从高到低排序。如果总分和语文成绩都相同，
按学号从低到高排序。任务：输入 $N$ 个学生的学号、语文成绩、数学成绩、
英语成绩，输出前 5 名学生的学号和总分。输入格式：第一行一个整数 $N$。
接下来 $N$ 行，每行三个整数，依次是语文、数学、英语成绩。
（学号按照输入顺序从 1 开始自动编号）。输出格式：5 行，每行两个整数：学号 和 总分。

'''