# 大小写存储
love = "MY FAVOTIRE language is 'python'"
print(love.title())            # 首字母大写
print(love.upper())        # 全部大写
print(love.lower())        # 全部小写

# f字符串：引用变量的值                       *变量+常量的组合
# 格式f"{引用变量名}"
first_name = "Ada"
last_name = "Wong"
full_name = f"{first_name} {last_name}"
message = f"Hello,{full_name.upper()}!"         # f字符串赋予变量
print(f"Hello,{full_name.title()}!")
print(message)

# 空格符\t
# 换行符\n
print(f"my favorite\nlanguage\n\tis python".title())

# 字符串空白格剔除
# lstrip()剔除开头空白，rstrip()剔除末尾空白，strip()剔除开头和空白末尾
Lg = ' python  '
print(Lg)
print(Lg.rstrip())        # 临时删除
Lg = Lg.rstrip()          # 永久删除
print(Lg)

# 浮点数:带小数点，无论小数点在何处
# 有浮点数参与的运算，结果始终是浮点