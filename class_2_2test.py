# 邀请
names = ['Ada', 'やまた', 'lilith']
print(f'邀请：尊敬的{names[0].title()},请于本周五下午光临寒舍，参加聚会！')
print(f'邀请：尊敬的{names[1].title()},请于本周五下午光临寒舍，参加聚会！')
print(f'邀请：尊敬的{names[2].title()},请于本周五下午光临寒舍，参加聚会！')
# print(f'通知：{names[1].title()}因故无法出席')
out = names.pop(1).title()
names.append("ミラさん")
print(f'通知：{out}先生因故无法出席，故我们新邀请了{names[2].title()}先生的加入！')
print(f'邀请：尊敬的{names[0].title()},请于本周五下午光临寒舍，参加聚会！')
print(f'邀请：尊敬的{names[1].title()},请于本周五下午光临寒舍，参加聚会！')
print(f'邀请：尊敬的{names[2].title()},请于本周五下午光临寒舍，参加聚会！')
names.insert(0, "张三")
names.insert(1, "李四")
names.append("Messi")
print(f"通知：现在有更大的餐桌，可额外邀请三位嘉宾！让我们欢迎{names[0]}，{names[1]}，{names[-1]}!")
print(f'邀请：尊敬的{names[0].title()},请于本周五下午光临寒舍，参加聚会！')
print(f'邀请：尊敬的{names[1].title()},请于本周五下午光临寒舍，参加聚会！')
print(f'邀请：尊敬的{names[2].title()},请于本周五下午光临寒舍，参加聚会！')
print(f'邀请：尊敬的{names[3].title()},请于本周五下午光临寒舍，参加聚会！')
print(f'邀请：尊敬的{names[4].title()},请于本周五下午光临寒舍，参加聚会！')
print(f'邀请：尊敬的{names[5].title()},请于本周五下午光临寒舍，参加聚会！')
out = names.pop()
print(f'通知：由于只能邀请两位嘉宾，故对{out}先生/女士表示歉意')
out = names.pop()
print(f'通知：由于只能邀请两位嘉宾，故对{out}先生/女士表示歉意')
out = names.pop()
print(f'通知：由于只能邀请两位嘉宾，故对{out}先生/女士表示歉意')
out = names.pop()
print(f'通知：由于只能邀请两位嘉宾，故对{out}先生/女士表示歉意')
print(f'邀请：尊敬的{names[0].title()},请于本周五下午光临寒舍，参加聚会！')
print(f'邀请：尊敬的{names[1].title()},请于本周五下午光临寒舍，参加聚会！')
print(names)