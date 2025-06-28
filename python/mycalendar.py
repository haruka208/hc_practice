import sys
import datetime

today = datetime.date.today()
year = today.year
month = today.month

# month = 6

if "-m" in sys.argv:
  # try:
  #   month = int(sys.argv[2])
  #   if not 1 <= month <= 12:
  #     print(f"{month} is neither a month number (1..12) nor a name")
  #     sys.exit(1)
  # except(IndexError, ValueError):
  #   print("Please specify 1~12 after the -m option")
  #   sys.exit(1)

  #ネストを浅くする
  if len(sys.argv) < 3:
    print("Please specify 1~12 after the -m option")
    sys.exit(1)
  try:
    month = int(sys.argv[2])
  except ValueError:
    print("Please specify 1~12 after the -m option")
    sys.exit(1)
  if not 1 <= month <= 12:
    print(f"{month} is neither a month number (1..12) nor a name")
    sys.exit(1)

# d = datetime.date(year, month, 1)

# week = [0, 1, 2, 3, 4, 5, 6]
days = []

# 最初の日付の曜日になるまでdaysに空白を入れる（daysの作成）
first_day = datetime.date(year, month, 1)
# for date_of_week in range(7):
#   if date_of_week == first_day.weekday():
#     break
#   else:
#     days.append(" ")
for _ in range(first_day.weekday()):
  days.append(" ")

# daysに日を足していって最後の日付になったら繰り返しをやめる（daysの作成）

# year = d.year
# month = d.month
# day = d.day

day = 1
while True:
  try:
    d = datetime.date(year, month, day)
    days.append(day)
    day += 1
  except ValueError:
    break

# daysの要素の数%7 = 0になったら改行する　を繰り返す（表示方法）

print(f"     {month}月 {year}")
print("月 火 水 木 金 土 日")

for i in range(0, len(days), 7):
  line = []
  for day in days[i:i+7]:
    day = str(day)
    if len(day) == 1:
      day = " " + day
    line.append(day)
  print(" ".join(line))



# 💡 ヒント：datetimeモジュールだけでカレンダーを作る手順
# datetime.date(2022, 2, 1) から始める

# 月が変わるまで1日ずつ増やしながら

# 曜日を確認して並べる（date.weekday() を使う）

# 🧩 どう組むか考えるヒント
# 最初の日まで空白を埋める（2月1日が火曜なので1つ空白）

# 毎日インデント付きで表示して、7日ごとに改行

# 月が変わったら終了（date.month != 2 で判定）


# 📝自分用memo

# import calendar
# print(calendar.month(1993, 12))

# month = int(sys.argv[1])

# d = datetime.date(2025, 6, 19)
# print(d)

# print(datetime.date(1993, 12, 12).weekday())

# print(d.weekday())

# daysに日を足していって最後の日付になったら繰り返しをやめる（daysの作成）
# ⚡️ 常にmonth==2になるからだめ
# day = 1
# while d.month == 2:
#   days.append(day)
#   day += 1

# daysの要素の数%7 = 0になったら改行する　を繰り返す（表示方法）
# ⚡️
# count = 0
# for day in days:
#   if (len(week) - count)% 7 == 0:
#     days.append("\n") # ループ中にリストを変更するとバグのもと 改行は表示時
#     count += 1

# print(sys.argv)