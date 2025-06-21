import random

group = ["A", "B", "C", "D", "E", "F"]
# sub_group = []

# num = random.randint(1, 2)

# if num == 1:
# # 3人と3人にランダムに分けるプログラム
#   for count in [0, 1, 2]: # range(3)
#     selected = random.choice(group)
#     sub_group.append(selected)
#     group.remove(selected)
    
# else:
# # 2人と4人にランダムに分けるプログラム
#   for count in [0, 1]: # range(2)
#     selected = random.choice(group)
#     sub_group.append(selected)
#     group.remove(selected)

num = random.choice([2, 3])
sub_group_1 = random.sample(group, num)
sub_group_2 = list(set(group) - set(sub_group_1))

# group.sort()
# sub_group.sort()
# print(group)
# print(sub_group)

# sub_group_1.sort()
# sub_group_2.sort()
print(sub_group_1)
print(sub_group_2)
