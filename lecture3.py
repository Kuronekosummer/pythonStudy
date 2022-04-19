# 练习：使用字典 保存   数字与中文 对应关系的星期
# （1）定义字典  初始值为{ 0:"星期天" }
# （2）添加键值对   星期一到星期六
#  （3）输入 键   显示对应的值
# （4） 修改  键为0的值”周日“
#  （5） 删除 键为5的  键值对

# week = {0: "星期天"}
# week[1] = "星期一"
# week[2] = "星期二"
# week[3] = "星期三"
# week[4] = "星期四"
# week[5] = "星期五"
# week[6] = "星期六"
# print(week[5])
# week.pop(5)
# print(week)

# week = {}
# keys = [0, 1, 2, 3, 4, 5, 6]
# values = ["星期天", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六", ]
# # 当键为整型，简便方法
# for i in range(7):
#     week[i] = values[i]
# # print(week)
# # 当键不为整型
# for i in range(7):
#     week[keys[i]] = values[values[i]]


# print(week.keys())
# print(week.values())
# print(week.items())
#
# for key in week:
#     print(f'key:{key},value:{week[key]},item:{key}:{week[key]}')

# 集合对纯数字有自动的排序功能
# l_alpha = ['a', 'b', 'c', 'd', 'e']
# l_num = [5, 2, 4, 1, 3]
# l_str_numeric = ['5', '2', '4', '1', '3']
# set_alpha = set(l_alpha)
# print(set_alpha)
# l_alpha = list(set_alpha)
# print(l_alpha)
# print('*'*15)
# set_num = set(l_num)
# print(set_num)
# l_num = list(set_num)
# print(l_num)
# print('*'*15)
# set_str_numeric = set(l_str_numeric)
# print(set_str_numeric)
# l_str_numeric = list(set_str_numeric)
# print(l_str_numeric)

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.symmetric_difference(set2))
# print(set1.difference(set2))

# list_num = [35, 67, 3, 5, 35, 78, 5, 35]
# set_num = set(list_num)
# print(set_num)
# list_num = list(set_num)
# print(list_num)

# 练习2：使用字典存储中国五岳，输入岳名，显示对应的山名
mountain = {"东岳": "泰山", "西岳": "华山", "南岳": "衡山", "北岳": "恒山", "中岳": "嵩山"}
name = input("请输入岳名")
print(mountain[name])

# 练习3： 使用字典保存语文，数学，英语的成绩。
# (1) 依次输入语文，数学，英语的成绩，保存到字典中 格式如下 {"语文":95, "数学"：88, "英语": 90}
# score = {}
# chinese = int(input("请输入语文成绩"))
# math = int(input("请输入数学成绩"))
# english = int(input("请输入英语成绩"))
# score["语文"] = chinese
# score["数学"] = math
# score["英语"] = english
# total = 0
# # (2) 输出成绩的信息，输出格式如下：
# # 语文：95
# # 数学：88
# # 英语：90
# # 总分：273
# for item in score.items():
#     total += item[1]
#     print(f'{item[0]}:{item[1]}')
# print(f'总分：{total}')
# # (3)找出最高成绩和科目
# highest = ('name', 0)
# for item in score.items():
#     if item[1] > highest[1]:
#         highest = item
# print(f'最高成绩为{highest[0]}:{highest[1]}分')

# ---------------------------------------------------------------使用单分支IF语句完成
# 1 ：输入星期几，  如果是星期六，输出"吃大餐"
# 2 ：输入一个整数，如果大于0，计算这个数的平方
# 3： 输入一个整数，如果是偶数，输出这个数
# 偶数是指 能被2整除的数 即 这个数除以2 余数为0
# 4：输入两个不相等的数，比较大小，将大数放在a中, 小数放在b中
# 5：输入手机号，如果尾数为5,输出：免费用餐
# 6：输入手机号， 输入一个手机号，如果长度不是11位，输出”无效的手机号码“
# day = input("请输入星期几")
# if day == '星期六':
#     print("吃大餐")
#
# num1 = int(input("请输入整数"))
# if num1 > 0:
#     print(num1 ** 2)
#
# num2 = int(input("请输入整数"))
# if num1 % 2 == 0:
#     print(num2)
#
# a = eval(input("请输入第一个数"))
# b = eval(input("请输入第二个数，要与第一个是不同"))
# if a != b:
#     if a < b:
#         a, b = b, a
#
# tel = int(input("请输入手机号"))
# if tel % 10 == 5:
#     print("免费用餐")
#
# tel = input("请输入手机号")
# if len(tel) != 11:
#     print("无效的手机号码")

# ---------------------------------------------------------------使用双分支IF语句完成
'''
1. 请编写一个判断小明爱好的程序,要求如下：
输入字符串，表示一项运动
如果输入的是"篮球"，则打印输出："小明喜欢打篮球."
如果输入的是其他运动，则打印输出："小明不喜欢XX." XX表示输入的运动

'''
'''
2. 小胖口袋有3块钱，输入一个数表法示饮料的价格，
如果饮料价格大于3块，则打印"太穷了，买不起"
否则打印"哈哈，一瓶饮料还是买得起的"
'''

sport = input("请输入运动")
if sport == '篮球':
    print("小明喜欢打篮球")
else:
    print(f'小明不喜欢{sport}')

price = int(input("请输入饮料价格"))
if price > 3:
    print("太穷了，买不起")
else:
    print("哈哈，一瓶饮料还是买得起的")

# #---------------------------------------------------------------使用多分支IF语句完成
# 1. 输入一个正整数，如果此数为0，输出“石头”，
# 如果此数为1，输出“剪刀”， 如果此数为2，输出“布”
# 如果为其它，则输出“错误”

choice = int(input("输入一个正整数"))
if choice == 0:
    print("石头")
elif choice == 1:
    print("剪刀")
elif choice == 2:
    print("布")
else:
    print("错误")

# # 2.女朋友的节日
# # 如果是情人节 买玫瑰/看电影
# # 如果是平安夜 买苹果/吃大餐
# # 如是是生日   买蛋糕
# # 其它日子     每天都是节日

festival = input("请输入节日")
if festival == '情人节':
    print("买玫瑰/看电影")
elif festival == '平安夜':
    print("买苹果/吃大餐")
elif festival == '生日':
    print("买蛋糕")
else:
    print("每天都是节日")

'''
3. 编写程序实现猜U盘价格，设定U盘价格为80，
当输入价格比设定的U盘价格大时，显示"猜大了"
当输入价格比设定的U盘价格小时，显示"猜小了"
当输入价格等于设定的U盘价格时，显示"恭喜你，猜对了"
'''

set_price = 80
guess = int(input("请猜测价格"))
if guess > set_price:
    print("猜大了")
elif guess < set_price:
    print("猜小了")
else:
    print("恭喜你，猜对了")
