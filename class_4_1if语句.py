cars =['bWm','audi','ducati','toyota']

for car in cars:
    if car.lower() == 'bwm':                                                                             # 4行的==代表发问，用于判断。判断行不会修改变量的赋值（大小写）
        print(car.upper())
    else:
        print(car.title())
print(cars)

# 不等号 ！=

# if-elif-else结构
# 4岁以下免费，4~18岁25元，18岁以上40元
age = 12
if age < 4:
    cost = 0
elif age < 19:
    cost = 25
else:
    cost = 40
print(f'你需要花费{cost}元')
# elif 可多次使用

# 多条件检查：and 和 or （同VBA）
age_1 = 21
age_2 = 21
if age_1<=25 and age_2 > 20:
    print('nice')

# 列表包含判断： 包含——in，不包含——not in
# 列表结合if
# 循环中判断
lists = [1,2,3]
for number in lists:
    if number == 1:
        print('true')
    else:
        print('false')

# 确定列表不是为空
lists = []
if lists:             #有内容则为true
    print('列表不为空')
else:
    print('列表为空')

# 判断A列表元素是否在B列表中
have =[1,2,3]
need = [1,5]

for number in need:
    if number in have:
        print(f'有{number}')
    else:
        print(f'没有{number}')