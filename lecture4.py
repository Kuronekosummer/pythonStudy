# # while 循环  20-100的数字
# n = 20
# while n <= 100:
#     print(n)
#     n += 1
# # while 循环  10+11+12..。+20的和
# res = 0
# n = 1
# while n < 12:
#     res += (n + 9)
#     n += 1
# print(res)
#
# # 使用 循环 询问 “我爱你，嫁给我吧.你喜欢我吗？（y/n）”
# #  如果回答为 y 则打印“我们形影不离”停止询问，若回答为其它内容，继续询问
# reply = input("我爱你，嫁给我吧.你喜欢我吗？（y/n）").lower()
# while reply != 'y':
#     reply = input("我爱你，嫁给我吧.你喜欢我吗？（y/n）").lower()
# else:
#     print('我们形影不离')
#
# # 1. 找出下面列表中年龄大于17岁的学员，打印出他们在列表中的索引
# studentAges = ['小王:17', '小赵:16', '小李:17', '小孙:16', '小徐:18']
# n = 0
# while n < len(studentAges):
#     age = eval("小王18")
#     if age > 17:
#         print(f"索引{n},{studentAges[n]}")
#     n += 1

# 3. while 循环   输出1-20之间的偶数
# n = 1
# while n < 21:
#     if n % 2 == 0:
#         print(n)
#     n += 1
# # 4. while 循环   统计 1-100之间能被6整除的数有多少个？
# n = 1
# cnt = 0
# while n < 101:
#     if n % 6 == 0:
#         cnt += 1
#     n += 1
# print(f"1-100之间能被6整除的数有{cnt}个")
# # 6. while 循环  输入一个数，判断是否是素数，素数是指在大于1的自然数中，只能被1和它本身整除。
# flag = False
# num = int(input("请输入一个整数"))
# prime = 2
# while prime < num:
#     if num % prime == 0:
#         print(f"{num}不是素数")
#         flag = True
#         break
#     prime += 1
# if not flag:
#     print(f"{num}是素数")
#
# # 7. while 循环  产生一个能被10整除的随机数 （当随机数能被10整除 结束）
# import random
#
# num_random = random.randint(0, 9999999)
# while num_random % 10 != 0:
#     num_random = random.randint(0, 9999999)
# print(num_random)
# # 8. while 循环  用户输入一个整数，如果输入的是正整数，计算这个数的平方，如果输入的是负数，继续再次输入，当 输入 0 时 结束操作
# instance = int(input("请输入一个整数"))
# while instance != 0:
#     if instance > 0:
#         print(instance ** 2)
#         break
#     elif instance < 0:
#         instance = int(input("请再次输入一个整数"))
# print('结束')
#
# # 9. 猜数游戏. 系统产生一个随机数，用户去猜(输入一个数),如果猜的数比被猜数大 ，输出：大了,如果猜的数比被猜数小,输出：小了.直到猜对为止 .
#
# answer = random.randint(0, 100)
# guess = int(input("请猜数字"))
# while guess != answer:
#     if guess > answer:
#         print("猜大了")
#         guess = int(input("请再猜数字"))
#     elif guess < answer:
#         print("猜小了")
#         guess = int(input("请再猜数字"))
# print("哇哦~猜对了！")


# 示例1 列表[12, 34, 15, 27]  for 找出列表中的偶数
for i in [12, 34, 15, 27]:
    if i % 2 == 0:
        print(i)
# 示例2： 元组(98,32,45,76)#输出大于80的分数
for i in (98, 32, 45, 76):
    if i > 80:
        print(i)
# 示例3:  找出年龄最大的学生studentAges = ['小王:17', '小赵:16', '小李:17', '小孙:16', '小徐:18']

studentAges = ['小王:17', '小赵:16', '小李:17', '小孙:16', '小徐:18']
stu = ['name', 0]
max_stu = []
for i in studentAges:
    if int(i.split(":")[1]) > stu[1]:
        max_stu = i
print(f'最大年龄学生为{max_stu}岁')

# 取出字符串s='as1d3f1r456g&*3409'中的数字，将获取的数字保存到列表中，获取完成后将列表中的数字排序
s = 'as1d3f1r456g&*3409'
l_num = []
for i in s:
    if i.isnumeric():
        l_num.append(int(i))
l_num.sort()
print(l_num)

# 1. 打印输出 30-50的数字
for i in range(30, 51):
    print(i)

# 2.  统计100-500之间能被7整除的数 共有多少个
res = 500 // 7 - 100 // 7
print(f"统计100-500之间能被7整除的数共有{res}个")

cnt = 0
for i in range(100, 501):
    if i % 7 == 0:
        cnt += 1
print(f"统计100-500之间能被7整除的数共有{cnt}个")

# 3.for 使用索引读取列表中的元素list1=[13, 45, 36, 109, 88]
list1 = [13, 45, 36, 109, 88]
for i in range(len(list1)):
    print(list1[i])
