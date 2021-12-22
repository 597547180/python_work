responses ={}

polling_active = True

while polling_active:
    name = input("请输入您的名字：")
    sport = input("请输入你最喜欢的运动:")

    responses[name] = sport         #输入字典
    repeat = input("是否继续:(是/否)")
    if repeat == "否":
        polling_active = False
    # elif repeat !="是":
    #      print("请输入正确的指示！")



for name,sport in responses.items():
    print(f"{name}喜欢{sport}")
