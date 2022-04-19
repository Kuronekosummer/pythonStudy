# a = '大家好，我的名字叫：倩紫飘飘'
# a1 = a[-4:]
# a2 = a[0::4]
# a3 = a[-1:-5:-1]
# print(a1, a2, a3)

# 练习1："文能提笔安天下,武能上马定乾坤.心存谋略何人胜,古今英雄唯世君."
# 1. 求字符串最大长度
# 2. 求字符串最大索引号
# 1. 取出数据: 文能提笔安天下
# 2. 取出数据：武定心何古
# 3. 取出最后7个字符

text = "文能提笔安天下,武能上马定乾坤.心存谋略何人胜,古今英雄唯世君."
length = len(text)
index_max = length - 1
initial = text[0:7]
ins = text[8:25:4]
last = text[-7:]
# print(length, index_max, initial, ins, last)

text2 = "一看桃花自悠然，几重烟雨渡青山"
# print(text2[::-1])

# 练习3 字符串"\t\t hello word，hello python \n"
# 1：  统计字符串出了多少次o
# 2：  查找 "python" 出现的位置  查找 "hello" 出现的位置
# 3 ： 去除前后的空白字符
# 4：  把hello 替换为 hi
# 5：  按，号拆分字符串 生成列表

# 练习3  列表[1,‘天王’,‘刘德华’]     转换为 ’1_天王_刘德华’
string = "\t\t hello word，hello python \n"
cnt = string.count('o')
pos_python = string.find('python')
pos_hello = string.find('hello')
string_clear = string.strip()
string_re = string.replace('hello', 'hi')
string_sp = string.split('，')
# print(cnt, pos_python, pos_hello, string_clear, string_re, string_sp)
list_str = ['1', '天王', '刘德华']
string_2 = ''.join(list_str)
# print(string_2)

# 练习6  输入手机号 检测手机是否正确
# (1) 长度11位
# (2) 全是数字
# (3) 第一位只能是1
# (4)第二位只能是3、5、7、8

# tel = input("please enter phone number")
# cond_1 = len(tel) == 11
# cond_2 = tel.isnumeric()
# cond_3 = tel.startswith('1')
# cond_4 = tel[1] in '3578'
# print(cond_1, cond_2, cond_3, cond_4)

# 练习5：一部电影的信息按名称，类型，主演,上映时间存储在一个字符串中，
# 请提取出 名称 和主演 的内容
# 全部内容如下：
movie_info = '''
名称：乌海
类型：剧情
主演：黄轩/杨子姗/涂们
上映时间：2011-10-29 08：00
'''
l_str = movie_info.split('\n')
# print(l_str[1], l_str[3], sep='\n')

# 练习1： list1 = ['张三','男','33','江苏','硕士','已婚',['身高178','体重72']]
# (1).正向索引 取出列表中第3-6元素
# (2).负向索引 取出列表中3-6元素
# (3). 取出”身高178“
#
# 练习2: 有如下的代码，定义了一个Python列表
# var1 = [ 33, ['我的名字', '倩紫飘飘'], 'hello world!']
# (1)打印出var1这个列表变量里面的 字符串 hello world!
# (2)打印出var1这个列表变量里面的 人名字 倩紫飘飘
# (3)修改var1这个列表变量里面的 hello world！ 为 Oh my God!
# (4)修改var1这个列表变量里面的 人名字 倩紫飘飘 为 拜月仙子)

# 练习3：
# 列表保存10个评委的分数，求平均分数(去掉一个最高分，去掉一个最低分，求最后得分)

list1 = ['张三', '男', '33', '江苏', '硕士', '已婚', ['身高178', '体重72']]
var1 = [33, ['我的名字', '倩紫飘飘'], 'hello world!']
print(list1[3:7])
print(list1[-4:])
print(list1[-1][0])

print(var1[-1])
print(var1[1][1])
var1[-1] = 'Oh my God!'
var1[1][1] = '拜月仙子'
print(var1)

score = [44, 15, 45, 15, 15, 9, 95, 32, 54, 25]
score.remove(min(score))
score.remove(max(score))
total = 0
for sc in score:
    total += sc
print(total / 8)

# 使用列表存储3个学生的信息（姓名，性别，手机号）
# 输出每个学生的信息：格式如下：
'''
第1个学生：
姓名：XX
性别：XX
手机：XX
第3个学生：
姓名：XX
性别：XX
手机：XX
第3个学生：
姓名：XX
性别：XX
手机：XX
'''
info = [
    ['onikage', 'male', '12546523589'],
    ['natsuna', 'female', '12596548512'],
    ['kaijin', 'male', '15632568452']
]
# for i in range(3):
#     print(f'第{i+1}个学生:')
#     print(f'姓名:{info[i][0]}')
#     print(f'性别:{info[i][1]}')
#     print(f'手机:{info[i][2]}')

# for i in range(3):
#     print("\t\t\t姓名\t\t性别\t\t手机")
#     print(f'第{i + 1}个学生:\t{info[i][0]}\t{info[i][1]}\t{info[i][2]}')


# 有一家自助式餐馆，只提供五种简单的食品。请想出五种简单的食品，并将其存储在一个元组中。
# 使用一个for将该餐馆提供的五种食品都打印出来。

# menu = ('sashimi', 'sushi', 'misoshiru', 'takoyaki', 'sukinabe')
# for food in menu:
#     print(food)

# warehouse = []
# state = True
# while state:
#     item = ['', 0, 0, 0]
#     item[0] = input("please enter item name")
#     item[1] = int(input("please enter item price"))
#     item[2] = int(input("please enter item number"))
#     item[3] = item[1] * item[2]
#     warehouse.append(item)
#     state = int(input("pleas enter 1 for continue or 0 for exit"))
# # print(warehouse)
#
# for i in warehouse:
#     print(f'名称:{i[0]}')
#     print(f'价格:{i[1]}')
#     print(f'折后价:{i[1]*0.8}')
#     print(f'库存量:{i[2]}')
#     print(f'总价:{i[3]}\n')
#
# for i in warehouse:
#     print("名称\t\t价格\t\t折后价\t\t库存量\t\t总价")
#     print(f'{i[0]}\t\t{i[1]}\t{i[1]*0.8}\t\t{i[2]}\t\t\t{i[3]}')

