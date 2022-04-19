import random
import time
import os


# 递归计算Σ0-n
def rec_plus(n):
    if n == 0:
        res = 0
    else:
        res = n + rec_plus(n - 1)
    return res


print(rec_plus(5))

# 定义匿名函数   计算两数的和
func = lambda x, y: x + y
print(func(4, 5))

# 1.导入当前包中某个模块使用该模块中的函数
import lecture5

lecture5.student_info('onikage', 17, 50, 60, 70, sex='女')
# 2.导入其它包中某个模块使用该模块中的函数
from pythonstudy.materials import stilltest

print(stilltest.variable_test)
stilltest.test('materials')


# 2. 定义函数 系统随机生成10道（20以内）加，减，乘，除  四种基本算术运算的题目。例如
#     第1题：12/2=
#     第2题：15/11=
#     第3题：19+5=
#     第4题：20/13=
#     第5题：16-10=
#     第6题：13-11=
#     第7题：15+4=
#     第8题：18+16=
#     第9题：19+14=
#     第10题：14+1=

def generate():
    question_list = []
    for i in range(10):
        a = random.randint(0, 20)
        b = random.randint(1, 20)
        symbol = random.choice(['+', '-', '*', '/'])
        question_list.append(f'{a}{symbol}{b}')
        print(f'第{i + 1}题：{a}{symbol}{b}=')
    return question_list


# 3. 基于第2题完成
# (1)练习者根据显示的题目输入自己的答案，程序自动判断输入的答案是否正确,并记录回答正确的次数
# (2)测试结束 ，显示共10道题，回答正确X个，正确率为X%

def get_answer(question):
    cnt = 0
    for i in range(len(question)):
        answer = float(input(f"输入{question[i]}的答案"))
        if answer == eval(question[i]):
            cnt += 1
    print(f'回答正确{cnt}个，正确率{cnt / len(question):.2%}')


# generate()
# get_answer(generate())

# 1.time 模块 获取系统 时间
# 2. 将当前时间  转换 指定字符串 格式输出
# 3.  输入 一个日期字符串 ， 转换为 time

a = time.localtime()
print(a)
b = time.strftime('%Y年%m月%d日 %X')
print(b)
c = '2022年4月8日 18:31:47'
d = time.strptime(c, '%Y年%m月%d日 %H:%M:%S')
print(d)

# 练习 输入1个目录路径，统计出该目录下有多少个文件和目录
print(os.getcwd())
c_dir = 0
c_file = 0
total = []
dir_name = input("请输入路径名")
if os.path.isdir(dir_name):
    print(os.listdir(dir_name))
    total = os.listdir(dir_name)
for i in total:
    if os.path.isdir(i):
        c_dir += 1
    if os.path.isfile(i):
        c_file += 1
print(f"目录有{c_dir}个，文件有{c_file}个")

