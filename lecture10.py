# 练习 定义一个类， 描述学生这类对象的特征和行为
# 特征  姓名  年龄  性别
# 行为  学习  自我介绍   吃  睡
class Student:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def study(self):
        print(f'学习使{self.name}快乐，{self.name}学习发自真心')

    def introduce(self):
        print(f'{self.name}到河北省来~')

    def eat(self):
        print(f'{self.name}在吃数一数二的烧鸡')

    def sleep(self):
        a = f"""
            ***  
          *******
         * R.I.P *
         *       * 
         *{self.name} *
         *       *
         *       *
         *********
        ***********
        """
        print(a)


# 练习  电脑类
# 特征  品牌  型号   颜色   CPU   内存  硬盘
# 行为  开机 关机  读数据   存数据
class Computer:
    slogan = '初始化系统中'

    def __init__(self, brand, model, color, cpu, ram, disk):
        self.brand = brand
        self.model = model
        self.color = color
        self.cpu = cpu
        self.ram = ram
        self.disk = disk

    @classmethod
    def boot(cls):
        print('booting...')

    @classmethod
    def shutdown(cls):
        print('shutting down...')

    @classmethod
    def read(cls):
        print('loading...')

    @classmethod
    def write(cls):
        print('saving...')

    @staticmethod
    def welcome():
        print(Computer.slogan)

    def showinfo(self):
        print(self.__dict__)


# 定义一个动物类  属性 名称  年龄  行为 跑  叫
# 定义一个子类小狗  继承 动物类   扩展一个行为  看门
# 定义一个子类小猫  继承 动物类   扩展一个行为  捉老鼠
class Animal:

    def __init__(self, name, age, voice):
        self.name = name
        self.age = age
        self.voice = voice

    @classmethod
    def run(cls):
        print('你给路达哟~润啦！')

    def shout(self):
        print(f'{self.name}：{self.voice}')


class Doggy(Animal):

    def __init__(self, name, age, voice):
        super().__init__(name, age, voice)

    def guard(self):
        print(f'{self.name}的绝活是看门')


class Pussy(Animal):

    def __init__(self, name, age, voice):
        super().__init__(name, age, voice)

    def hunt(self):
        print(f'{self.name}的绝活是抓老鼠')


if __name__ == '__main__':
    # fuhrer = Student('hitler', 35, 'male')
    # print(fuhrer.__dict__)
    # fuhrer.study()
    # fuhrer.introduce()
    # fuhrer.eat()
    # fuhrer.sleep()
    # stalin = Student('stalin', 48, 'male')
    # print(fuhrer.__dict__)
    # stalin.study()
    # stalin.introduce()
    # stalin.eat()
    # stalin.sleep()
    # 使用类  创建  2台具体的电脑对象
    # computer1 = Computer('alienware', 'k2000', 'cyan', 'core-i13', '64G', '10T SSD')
    # computer2 = Computer('alienware', 'W1', 'magenta', 'core-i13', '64G', '10T SSD')
    # Computer.welcome()
    # Computer.boot()
    # Computer.read()
    # computer1.showinfo()
    # Computer.write()
    # Computer.shutdown()

    hitler = Doggy('狗沟', 3, '汪汪！')
    gaffield = Pussy('喵星人', 4, 'nya~nya~')

    hitler.run()
    hitler.shout()
    hitler.guard()

    gaffield.run()
    gaffield.shout()
    gaffield.hunt()

    def shout(obj):
        obj.shout()
    shout(hitler)
    shout(gaffield)
