"""******************************************题目******************************************"""
# 3 .请定义一个交通工具Vehicle的类
# 属性： 速度(speed)
# 方法： 启动start(）---车速为60
#            移动move() -----------打印当前车速    输出:  正在行驶中，当前车速XX, 请勿疲劳驾驶
#            加速 speedUp( )     ---------- 车速加20      调用move方法  打印当前车速
#            减速 speedDown() ----------- 车速减20 ，调用move方法   打印当前车速
#            停止stop(）---车速为0
#
# 实例化一个交通工具对象，调用 启动，移动，加速、减速 、停止的方法
# ————————————————————————————————
# 4.  定义一个圆类Circle，显示面积和周长
# 实例属性：半径r
#  实例 方 法 ：
#         计算 面积 call_area()
#         计算 周长 call_Perimeter()
#         输出圆半径、面积和周长 show( )
# 实例化一个半径为13的圆对象，显示计算结果
# 实例化一个半径为7的圆对象，  显示计算结果
# ——————————————————————
# 9. 需求：一圆形游泳池，现在需要在其周围建一个圆形过道，并在其四周围上栅栏。
# 栅栏价格为35元/米,过道造价为20元/平方米，过道宽度为3米。游泳池半径由键盘输入。
# 用面向对象的方法设计圆形类Circle，计算并输出过道和栅栏的造价
# 10.  需求： 学生小明正在玩 HUAWEI  MateX2 手机    用面向对象的方法设计
# ————————————————————————————————
# 对象是谁   小明  手机
# 对象 有什么特征
# 小明对象  姓名   手机
# 手机对象  品牌   型号
# 对象 做什么（方法）
# 小明对象  玩手机
# 手机对象  听音乐  刷抖音  打游戏


class Vehicle:
    import time

    def __init__(self, name):
        self.name = name
        self.speed = 0

    def start(self):
        import time
        import random
        self.speed = 60
        print('启动')
        print('自检中...')
        time.sleep(random.random() * 2)
        print(f'全系统正常, 车速:{self.speed}')

    def move(self):
        import time
        import random
        while self.speed > 0:
            print(f'正在行驶中，当前车速{self.speed}, 请勿疲劳驾驶')
            time.sleep(0.5)
            flag = random.choice([1, 2, 3])
            if flag == 1:
                print('加速中...')
                for i in range(4):
                    self.speedUp()
            elif flag == 2:
                print('减速中...')
                for i in range(4):
                    self.speed_down()
            elif flag == 3:
                self.stop()
        print('车辆已停止')

    def speedUp(self):
        import time
        time.sleep(0.3)
        self.speed += 5

    def speed_down(self):
        import time
        time.sleep(0.3)
        self.speed -= 5

    def stop(self):
        self.speed = 0
        print(f'紧急制动！')
        print('车辆已停止')


class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius
        self.area = 0
        self.perimeter = 0

    def call_area(self):
        self.area = self.PI * self.radius ** 2

    def call_perimeter(self):
        self.perimeter = self.PI * self.radius * 2

    def show(self):
        print(f'面积为：{self.area}\n周长为：{self.perimeter}')


class Evaluate:

    def __init__(self):
        self.radius = int(input('请输入需要估算造价的泳池半径'))

    def round_way(self):
        budget_way = ((self.radius + 3) ** 2 - self.radius ** 2) * 3.14 * 20
        print(budget_way)

    def round_fence(self):
        budget_fence = 3.14 * 2 * self.radius * 35
        print(budget_fence)


class Phone:

    def __init__(self, name, model):
        self.name = name
        self.model = model

    @classmethod
    def listen_music(cls):
        print('先听一下歌\n大威天龙！')

    @classmethod
    def browse_douyin(cls):
        print('算了，刷一会抖音\n奥利给，淦啦！')

    @classmethod
    def play_game(cls):
        print('直接开始摆烂\n亚索断开了连接...')


class Person:

    def __init__(self, name):
        self.name = name
        self.phone = ''

    def buy_phone(self):
        self.phone = Phone('HUAWEI', 'MateX2')
        print('买一个手机')

    def play_phone(self):
        print(f'==========我{self.name}现在要开始玩手机啦！==============================')
        self.phone.listen_music()
        self.phone.browse_douyin()
        self.phone.play_game()


if __name__ == '__main__':
    '''================车对象调用================='''
    # AI_car = Vehicle('红旗')
    # AI_car.start()
    # AI_car.move()
    '''================圆对象调用================='''
    # circle1 = Circle(13)
    # circle2 = Circle(7)
    #
    # def pattern(obj):
    #     obj.call_area()
    #     obj.call_perimeter()
    #     obj.show()
    #
    # pattern(circle1)
    # pattern(circle2)
    '''================估算对象调用================'''
    # evaluate = Evaluate()
    # evaluate.round_way()
    # evaluate.round_fence()
    '''================人对象和手机对象调用=========='''
    # xiaoming = Person('小明')
    # xiaoming.buy_phone()
    # xiaoming.play_phone()