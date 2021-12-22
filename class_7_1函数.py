def greet_user(name):
    """显示简单的问候"""
    print(f"你好，{name}")

#调用函数时输入参数
greet_user("wang")

#实参、形参
def show_pet(pet_name,pet_type):
    """显示宠物信息"""
    print(f"我有一只{pet_type}")
    print(f"它的名字叫做 {pet_name}")

show_pet('狗','花花')

def show_pet1(pet_name,pet_type="狗"):
    """显示宠物信息"""
    print(f"我有一只{pet_type}")
    print(f"它的名字叫做 {pet_name}")

show_pet1(pet_name='小meng')

#返回值
def clean_name(first_name,last_name):
    """返回清洁姓名"""
    full_name = f"{first_name} {last_name}"
    return {full_name}

MyName = clean_name("李","逍遥")            #将返回值赋予
print(MyName)


def clean_name_new(first_name,last_name,mid_name=""):
    """返回清洁姓名"""
    if mid_name:              #如mid_name不为空，则为true
        full_name = f"{first_name} {mid_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return {full_name}

MyName = clean_name_new("李","遥","逍")
print(MyName)


#返回字典（结合字典和while）
def person(first_name,last_name,age=None):
    person = {"first":first_name,"last":last_name}
    if age:
        person["age"]=age
    return person

while True:
    f_name=input("请输入姓：")
    l_name=input("请输入名：")
    age_0 = input("请输入年龄：")
    I = person(f_name,l_name,age_0)
    print(I)

