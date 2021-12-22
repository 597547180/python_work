user = {
    'name': 'lufeiwang',
    'number': 11,
    'level': 4,
}

# 字典的items(),keys(),values()分别是键值对、键、值
# 遍历所有键值对
for key,value in user.items():
    print(f'\nKey:{key}')
    print(f'Value:{value}')

# 遍历所有键
for k in user.keys():
    print(k)

# 遍历所有值
for v in user.values():
    print(v)

# 循环例1
favorite_food= {
    '张三':'饺子',
    '李四':'面',
    '王二':'火锅',
    '孟三':'寿司',
}
friend = ['李四','王二']

for name in favorite_food.keys():
    print(f'{name}你好')
    if name in friend:
        food = favorite_food[name]
        print(f'{name},我记得你喜欢吃{food}')
# 循环例2
favorite_food= {
    '张三':'饺子',
    '李四':'面',
    '王二':'火锅',
    '孟三':'寿司',
}
friend = ['李四','王二']

for name in favorite_food.keys():
    if name in friend:
        food = favorite_food[name]
        print(f'{name},好久不见，我记得你喜欢吃{food}')
    else:
        print(f'{name}初次见面，你好')


# 按特定顺序遍历字典
favorite_food = {
        '张三': '饺子',
        '李四': '面',
        '王二': '火锅',
        '孟三': '寿司',
 }
for name in sorted(favorite_food.keys()):
    print(name)
