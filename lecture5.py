# 电影院1号厅座位5排7列，请使用循环打印每排的座位号
# 1-1		1-2		1-3		1-4		1-5		1-6		1-7
# 2-1		2-2		2-3		2-4		2-5		2-6		2-7
# 3-1		3-2		3-3		3-4		3-5		3-6		3-7
# 4-1		4-2		4-3		4-4		4-5		4-6		4-7
# 5-1		5-2		5-3		5-4		5-5		5-6		5-7

for j in range(1, 6):
    for i in range(1, 8):
        print(f"{j}-{i}", end=' ')
    print()

for i in range(10):
    for j in range(10):
        print('*', end='')
    print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}X{i}={i * j}', end='\t\t')
    print()


# 1.  定义一个函数  使用*打印5行的三角形
def triangle_5():
    for i in range(1, 6):
        print('*' * i)


# 2.  定义一个函数，使用*打印N行三角形，   N由调用时确定
def triangle_n(n):
    for i in range(1, n + 1):
        print('*' * i)


# 3.  定义一个函数， 计算 两个数相加的结果并返回
def plus_2(a, b):
    plus = a + b
    return plus


# 4.  定义一个函数， 计算两个数，加，减，乘，除的结果并返回
def calculate(a, b):
    plus = a + b
    minus = a - b
    times = a * b
    divide = a / b
    return plus, minus, times, divide


# 练习， 定义一个函数 输出 学生的信息：姓名，年龄，性别， 多个成绩， 计算总分和平均成绩
# 其中 性别默认男， 成绩是一个可变参数
def student_info(name, age, *args, sex='男'):
    name = name
    age = age
    sex = sex
    score = args
    total = sum(args)
    avg = total / len(args)
    return name, age, sex, avg


print(student_info('onikage', 17, 50, 60, 70, sex='女'))

# 声明一个全局变量total保存班级总人数，声明一个字典students保存学生信息（用学号作为键，值为列表，保存学生信息）。
# 声明一个函数用于录入学生信息，每录入一个学生则在students中新增一个键值对，total的值+1。
total = 2
students = {'st_101': ['张三', '男', '17712345678'], 'st_102': ['杨一一', '女', '15812345678']}


def input_info(identity, name, sex, tel):
    key = identity
    value = [name, sex, tel]
    global students, total
    students[key] = value
    total += 1


input_info('st_103', 'onikage', '男', '15623568954')
print(students, '\n', total)
