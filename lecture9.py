import pymysql


class DbLink:
    def __init__(self, host='127.0.0.1', user='root', password='123456', port=3306, database='school_db',
                 charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.charset = charset
        self.operation = {'新增': 'insert into', '修改': 'update', '删除': 'delete from'}

        self.link = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            database=self.database,
            charset=self.charset
        )

        self.cursor = self.link.cursor()

    def execution(self, statement):
        if statement:
            try:
                self.cursor.execute(statement)
                self.link.commit()
                print('操作成功')
            except:
                self.link.rollback()
                print('未完成操作，数据回滚')

    def end(self):
        self.link.close()

    def adjust(self):
        combination = ''
        require = input('请输入想执行的操作(新增，修改，删除),其它任意内容退出')
        if require in self.operation:
            operation = self.operation[require]
            condition = ' ' + input('请输入条件,无条件直接回车跳过')
            table = input('请输入表名')
            if operation == 'insert into':
                name = input('请输入新的姓名')
                sex = input('请输入新的性别')
                tel = input('请输入新的手机号')
                combination = f"{operation} {table} (name, sex, tel) values('{name}', '{sex}', '{tel}'){condition};"
            elif operation == 'delete from':
                combination = f"{operation} {table}{condition};"
            elif operation == 'update':
                name = input('请输入新的姓名')
                sex = input('请输入新的性别')
                tel = input('请输入新的手机号')
                combination = f"{operation} {table} set name='{name}', sex='{sex}', tel='{tel}'{condition};"
        else:
            pass
        return combination

    def query(self):
        name = input('请输入要查询的项目用逗号隔开(*代表所有项)')
        table = input('请输入要查询的表名')
        condition = input('请输入条件,无条件直接回车跳过')
        combination = f"select {name} from {table} {condition};"
        print(combination)
        try:
            self.cursor.execute(combination)
            data = self.cursor.fetchall()
            print('操作成功,以下为查询内容:')
            print(data)
        except:
            print('未完成操作，请检查sql语句')


if __name__ == '__main__':
    my_link = DbLink()
    my_link.__init__(user='root', password='123456', database='school_db')
    # 重置表格数据
    # sql_list = [
    #     '''insert into students (name, sex, tel) values('Shermie', 'female','13569865484');''',
    #     '''insert into students (name, sex, tel) values('Marry', 'female','13256986548');''',
    #     '''insert into students (name, sex, tel) values('Angel', 'female','13256985468');''',
    #     '''insert into students (name, sex, tel) values('Yuri', 'female','13256985485');''',
    #     '''insert into students (name, sex, tel) values('kagura', 'female','13356985458');''',
    #     '''update students set name='shiranui', sex='female', tel='13269658458' where id = 2;''',
    #     '''delete from students where id =4;'''
    # ]
    # for sql in sql_list[0:-2]:
    #     my_link.execution(sql)
    #  数据管理
    # sql = True
    # while sql:
    #     sql = my_link.adjust()
    #     print(sql)
    #     my_link.execution(sql)
    # 数据查询
    my_link.query()
    my_link.end()
