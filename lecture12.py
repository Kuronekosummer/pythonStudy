"""=========================题目========================="""

# 练习1：定义函数， 使用键访问字典中的元素，处理异常：访问字典中不存在键

# 练习2：定义函数计算两个数的除法 ，函数有两个参数， 处理所有的异常

# 练习3：定义函数：读取文件 ，处理异常：没有找到文件或读取文件失败

person = {"陈坤": "优秀演员", "谢娜": "著名主持人", "张杰": "实力歌手"}


def who(name):
    try:
        job = person[name]
    except KeyError:
        print(f"Key Error: can't find '{name}'")


def divides(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        print(f'Divide By 0 Error, check your values')


def rd_file(file):
    try:
        f = open('file', 'r', encoding='utf-8')
    except FileNotFoundError:
        print(f"Directory Error can't find '{file}'")
    except IsADirectoryError:
        print(f"'{file}' is a directory")


who('奈亚拉托提普')
divides(5, 0)
rd_file('不存在的')
