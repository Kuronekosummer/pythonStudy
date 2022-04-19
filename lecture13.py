# from threading import *
import threading
from time import sleep
from random import random

lock = threading.Thread.Lock()

# 练习：创建一个函数  打印输出5个数

# 创建 两个线程  模拟同时执行这个函数
# 最终结果：两个线程在cpu调度下 交替执行

#  定义一个函数   修改全局变量num的值 ， 加1  再减1  最后输出num
# 然后  创建两个线程  执行这个函数，  观看 全局的变量的值
# 理想状态：线程操作完后，全局变量的数据还是0
# 运行结果：  ？？？？

# 练习  创建 3个线程  模拟 3个窗口 共同出售10张车票

# 练习1： 使用Thread类   创建 3个线程   模拟3个窗口共同出售10张车票

# 练习2： 使用自定义线程类 创建 3个线程    模拟3个窗口共同出售10张车票
'''++++++++++++++++++++多线程并发竞争++++++++++++++++++++'''
# def count(name):
#     for i in range(5):
#         print(name, i**i**2)
#
#
# thr1 = Thread(target=count, args=('thr1',))
# thr2 = Thread(target=count, args=('thr2',))
#
# thr1.start()
# thr2.start()

'''++++++++++++++++++++2.改写Thread中的run()方法++++++++++++++++++++'''
# class MyTread(Thread):
#
#     def __init__(self):
#         super().__init__()
#
#     def run(self):
#         for i in range(5):
#             print(self.name, i)
#             sleep(0.3)

'''++++++++++++++++++++3.验证锁的作用++++++++++++++++++++'''
# num1 = 5
# num2 = 5
#
#
# def locked_change():
#     global num1
#     lock.acquire()
#     num1 -= 1
#     sleep(0.5)
#     num1 += 1
#     print(f'加锁的结果{num1}')
#     lock.release()
#
#
# def change():
#     global num2
#     num2 -= 1
#     sleep(0.5)
#     num2 += 1
#     print(f'不加锁的结果{num2}')

'''++++++++++++++++++++4.三个窗口买票++++++++++++++++++++'''
# tickets = 30
#
#
# def seller(name):
#     global tickets
#     while True:
#         sleep(random() * 2)
#         lock.acquire()
#         if tickets > 0:
#             tickets -= 1
#             print(f'{name}窗口卖出一张票,剩余{tickets}张')
#             lock.release()
#         else:
#             break
#     lock.release()

'''++++++++++++++++++++5.使用自定义线程类买票++++++++++++++++++++'''

if __name__ == '__main__':
    pass
    '''++++++++++++++++++++2.改写后方法的调用++++++++++++++++++++'''
    # thr_count1 = MyTread()
    # thr_count2 = MyTread()
    # thr_count1.start()
    # thr_count2.start()
    '''++++++++++++++++++++3.不加锁并发++++++++++++++++++++'''
    # thr_unlock1 = Thread(target=change)
    # thr_unlock2 = Thread(target=change)
    # thr_unlock1.start()
    # thr_unlock2.start()
    '''++++++++++++++++++++3.加锁并发++++++++++++++++++++'''
    # thr_lock1 = Thread(target=locked_change)
    # thr_lock2 = Thread(target=locked_change)
    # thr_lock1.start()
    # thr_lock2.start()
    '''++++++++++++++++++++4.三个窗口卖车票++++++++++++++++++++'''
    # seller1 = Thread(target=seller, args=('一号',))
    # seller2 = Thread(target=seller, args=('二号',))
    # seller3 = Thread(target=seller, args=('三号',))
    # seller3.start()
    # seller1.start()
    # seller2.start()
    '''++++++++++++++++++++5.使用自定义线程类买票++++++++++++++++++++'''
