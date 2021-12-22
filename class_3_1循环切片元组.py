# 操作列表

# 1、循环遍历 + 2、 缩进问题
killers = ['Lee', '士郎', 'David']
for killer in killers:  # ：冒号提示下行开始循环
    print(f'{killer}成功刺杀伏地魔\n')  # 循环内过程需要缩进

killer = 1
print(killer)
# ************Python根据缩进关系来判断代码与前一行的关系*************

# 3、数值列表
# 3.1 range(x,y,z) 创建数集
# range(x,y) 从x数到y-1 。
# range(y)参数只有一时，从0开始至y-1
# 参数z代表指定“步长”,小于不等于y停止
for number in range(1, 0,-1):  # range 无法进行常规运算
    print(number)



    # 3.2 list() 输出数字列表
    # 参数
number = list(range(1, 6))
print(number)

# 例：创建1-10的平方列表
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

numbers = []
for value in range(11, 21):
    numbers.append(value ** 2)
print(numbers)

# 3.3、数值列表统计
# 3.31、min(列表名) max(列表名) sum(列表名)

# 3.4、列表解析                                                                              *********
homes = [value ** 2 for value in range(21, 31)]
print(homes)

# 练习
numbers = list(range(3, 31, 3))
for value in range(1, len(numbers)+1):
    print(numbers[value-1])

numbers = []
for value in range(3, 31, 3):
    numbers.append(value)
    print(numbers)

# 4、列表部分使用
# 4.1、切片 → 区域访问
players =['a', 'b', 'c', 'd', 'e']
print(players[1:3])               # 切取的列表[起始:末尾, 间隔参数]，起始没注明，默认为0（第一个元素）,末尾没注明，默认到最后
                                                   # 间隔参数为切片间隔
print(players[:2])
print(players[-2:])                    # [-2：] 含义为切片列表最后两个元素
print(players[:])                       #备份列表


# 5、元组
# 5.1、定义元组：元组是不能修改的列表
foods = ('饺子', '拉面', '螺蛳粉', '蟹黄', '沙拉')
print(foods)

# 5.2、元组本质上由逗号定义，一个元素的元组也需要逗号
food = ('天妇罗', )

# 5.3、 元组不能修改元素，但可以重新赋值
foods = ('饺子', '拉面', '螺蛳粉', '蟹黄', '沙拉')
# foods[0] = "牛排"
foods = ('饺子', '拉面', '螺蛳粉', '蟹黄')
print(foods)