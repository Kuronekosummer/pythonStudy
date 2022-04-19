import re

"""
1.  昵称长度3-10位，必须以字母开头
2.  姓名必须是2-4个汉字
3.  密码长度6位的数字
4.  手机号13，15，18开头11位数字
"""
# ^[a-zA-Z]\w{2,9}$
# ^[\u4e00-\u9fa5]{2,4}$
# ^[0-9]{6}$
# ^1[3|5|8][0-9]{9}$

# 练习1： 使用Re模块的正则 检测手机号是否有效(以13，15，18开头11位数字)。输入手机号进行检测，如果正确 输出这个手机号， 如果不正确提示：手机号无效
tel = input("请输入手机号")
rules = '^1[3|5|8][0-9]{9}$'
res = re.search(rules, tel)
if res:
    print(res.group())
else:
    print("手机号不合法")
# 练习2： 使用Re模块的正则 统计一段字符有多少字母，有多少标点符号

lettres = '''
If you were a teardrop; In my eye, 
For fear of losing you, I would never cry. 
And if the golden sun, 
Should cease to shine its light, 
Just one smile from you, 
Would make my whole world bright.
'''

rules_alpha = '[a-zA-Z]'  # 匹配所有字母
res = re.findall(rules_alpha, lettres)
print(len(res))
rules_symbol = '[^A-Za-z\s]'
res = re.findall(rules_symbol, lettres)
print(len(res))

# 练习3：使用Re模块的正则，将每个电子邮件替换为你自己的电子邮件地址
email = '''werksdf@163.com, sdf@sina.com,sf_jsdf@139.com, soifsdfj@134.com，pwoeir423@123.com'''
# 如:taotao@163.com,taotao@sina.com,taotao@139.com,tatao@134.com,taotao@123.com
