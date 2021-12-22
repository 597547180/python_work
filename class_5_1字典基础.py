# 定义字典，一组组'键'与'值'的对
alien ={'point': 5, 'color': 'blue'}
print(alien['point'])           # 访问字典

# 变更字典
# 添加键
alien_1 = { }         # 定义空字典
alien_1['hp'] = 100
print(alien_1)

# 修改值
alien_2 = {'hp': 100}
alien_2['hp'] = 1000
print(alien_2['hp'])

# 删除键值对
alien_3 ={'point': 5, 'color': 'blue'}
del alien_3['color']
print(alien_3)


# 字典的定义格式
language ={
    '1班':'中文',
    '2班':'日语',
    '3班':'英语',
}
print(language)

# get()访问：常规 字典名['键名']的访问方式，如键名不存在，则报错
print(language.get('1班','没有1班'))            # get（键名，没有键时显示默认none）

