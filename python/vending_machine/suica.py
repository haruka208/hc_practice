class Suica:
  # Step1 預かり金(デポジット)として 500 円がデフォルトでチャージされているものとする
  def __init__(self):
    self._deposit = 500

  # Step1 Suica には 100 円以上の任意の金額をチャージできる
  def charge(self, money):
    # money = input("チャージする金額を入力してください(例：120) :")
    try:
      money = int(money)
    except(ValueError):
      # print("整数で入力してください(例：120)")
      raise ValueError("整数で入力してください(例：120)")
    
    # Step1 100 円未満をチャージしようとした場合は例外を発生させる
    if money < 100:
      # print("整数で入力してください(例：120)")
      raise ValueError("100円以上の金額を入力してください(例：120)")
    
    self._deposit += money
    # print(f"{money}円チャージしました")
    return money

  # Step1 Suica は現在のチャージ残高を取得できる  
  def now_deposit(self):
    # print(f"現在のチャージ残高は{self._deposit}円です")
    return self._deposit
    
if __name__ == "__main__":
  haruka_suica = Suica()
  print(haruka_suica.now_deposit())
  print(haruka_suica.charge(80))
  print(haruka_suica.now_deposit())
  print(haruka_suica.charge(150))
  print(haruka_suica.now_deposit())

# 📝
  # 階層深いver try-except
  # try:
    # money = int(money)
    # if money < 100:
      # print("100円以上の金額を入力してください(例：120)")
      # return
    # self._deposit += money
    # print(f"{money}円チャージしました")
  # except(ValueError):
    # print("整数で入力してください(例：120)")
    # return