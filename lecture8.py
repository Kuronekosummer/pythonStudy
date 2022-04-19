import xlrd, xlwt

# 练习： msg.txt文件已有内容：天行键，君子以自强不息地势坤，君子以厚德载物
# 向msg.txt中写入以下内容：
# 然后再读取 msg.txt文件的所有内容
# 定义3个函数 分别使用 r+   w+    a+  3种方式读写内容
'天行键，君子以自强不息天行键，君子以自强不息'


def r_plus():
    with open(r'../materials/msg.txt', 'r+', encoding='utf-8') as f:
        content = '\n好雨知时节，当春乃发生.随风潜入夜，润物细无声.'
        f.read()
        f.write(content)
        f.seek(0, 0)
        text = f.read()
        print(text)


def w_plus():
    with open(r'../materials/msg.txt', 'w+', encoding='utf-8') as f:
        content = '好雨知时节，当春乃发生.随风潜入夜，润物细无声.'
        f.write(content)
        f.seek(0, 0)
        text = f.read()
        print(text)


def a_plus():
    with open(r'../materials/msg.txt', 'a+', encoding='utf-8') as f:
        content = '\n好雨知时节，当春乃发生.随风潜入夜，润物细无声.'
        f.write(content)
        f.seek(0, 0)
        text = f.read()
        print(text)


# 练习1： xlrd模块  读取  一笔记账
'''
支出 金额 时间 
日常 356.0 44626.0 
餐饮 588.0 44627.0 
....
'''
# （1）使用 row_values(行号)  方法 读取 sheet表 每行的数据 并显示
table = xlrd.open_workbook(f'../materials/一笔记帐.xls')
sheet = table.sheet_by_index(0)
n = sheet.nrows
for i in range(n):
    row = sheet.row_values(i)
    print(row[0], row[1], row[2])

# （2）使用 cell_value(行号，列号)  方法 读取 sheet表 每行的数据 并显示
table = xlrd.open_workbook(f'../materials/一笔记帐.xls')
sheet = table.sheet_by_index(0)
n = sheet.nrows
for i in range(n):
    for j in range(3):
        cell = sheet.cell_value(i, j)
        print(cell, end=' ')
    print()

# 练习2  xlwt 模块  excel 写 数据

# 第一行 空 不写内容
# 第2行 内容： 平台   金额       件数
# 第3行 内容:  天猫	123853	 1571

text = [
    ['平台', '金额', '件数'],
    ['天猫', '123853', '1571']
]

table = xlwt.Workbook()
sheet = table.add_sheet('sheet01')
for i in range(len(text)):
    for j in range(len(text[i])):
        sheet.write(i, j, text[i][j])
table.save(r'../materials/表格.xls')

# 练习3  xlwt 模块  excel 写 数据
data = [["天猫", "123853", "1571"], ["京东", "7469", "93"], ["凡客", "76409", "945"]]
# 列表中的数据写入 销售年度汇总.xls表中

table = xlwt.Workbook()
sheet = table.add_sheet('sheet01')
for i in range(len(data)):
    for j in range(len(data[i])):
        sheet.write(i, j, data[i][j])
table.save(r'../materials/销售年度汇总.xls')

# if __name__ == '__main__':
# r_plus()
# w_plus()
# a_plus()
