# 练习1： 定义一个函数 将自己最喜欢的名言名句写入a.txt文本文件中
def f_write():
    content = '在祂的神殿拉莱耶中，伟大的克苏鲁候汝入梦！'
    with open(r'../materials/a.txt', 'w', encoding='utf-8') as file:
        file.write(content)


# 练习2： 定义一个函数 读取a.txt文本文件的内容
def f_read():
    with open(r'../materials/a.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        return content


# f_write()
# print(f_read())

with open(r'../materials/student.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    # print(text)
    title = text[0].strip() + '    总和'
    print(title)
    result = title.replace(' ', '      ')
    for stu in text[1:]:
        info = stu.strip().split()
        scores = info.copy()
        scores.pop(0)
        total = str(eval('+'.join(scores)))
        info.append(total)
        res = '\t\t '.join(info)
        print(res)
        result += '\n'+res

with open(r'../materials/student_total.txt', 'w', encoding='utf-8') as f:
    f.write(result)
