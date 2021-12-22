# 列表: [ ]表示，逗号间隔

motos = ["ninja", "Yamaha", "cbr"]
print(motos)           # 打印数字，结果包含[ ]

# 访问列表
print(motos[0].title())                                                                                    # 访问结果不含[ ]，且列表从0开始
print(motos[-1].upper())                                                                               # -1访问列表中最后一个元素，-2、-3类推
# 练习例
message = f'   我的第一辆摩托不是 {motos[0].title()}'.strip()
print (message)

# 修改列表元素

# 列表中添加元素
# 1、列表末尾添加元素，方法：append(新增元素)。创建一个空列表xx = []，动态新增
motos.append("ducati")
print(motos)
# 2、列表中途插入元素，方法：insert(插入位置，新增元素)。原有元素右移
motos.insert(0, "suzuki")
print(motos)

# 列表中删除元素
# 1、知道元素位置，方法：del
# *删除不可用
del motos[0]
print(motos)
# 2、“弹出”列表的元素，方法：XXX.pop(索引)     索引默认为-1。
# *弹出的元素还可以使用。
last_one = motos.pop()
print(motos)
print(last_one.upper())
# 3、删除指定值，方法：remove(元素)         remove只删除列表中的第一个指定元素（如重复多个）
# *remove的元素可继续使用
favorite = "cbr"
motos.remove(favorite)
print(motos)


# 列表排序
# 1、永久改变排序（字母顺序），方法：XXX.sort()         默认按字母顺序，逆字母顺序入参数reverse = True
# 2、临时改变排序（字母顺序），方法：sorted(XXX)     默认按字母顺序，逆字母顺序入参数reverse = True
print(sorted(motos, reverse=True))
# 3、永久反转列表，方法：XXX.reverse()    可两次reverse恢复原状
motos.reverse()
print(motos)

# 列表长度获取，len(XXX)