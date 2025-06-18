import random

group = ["A", "B", "C", "D", "E", "F"]
sub_group = []

num = random.randint(1, 2)

if num == 1:
# 3人と3人にランダムに分けるプログラム
  for count in [0, 1, 2]:
    selected = random.choice(group)
    sub_group.append(selected)
    group.remove(selected)
    
else:
# 2人と4人にランダムに分けるプログラム
  for count in [0, 1]:
    selected = random.choice(group)
    sub_group.append(selected)
    group.remove(selected)

group.sort()
sub_group.sort()
print(group)
print(sub_group)