class Suica:
  # Step1 預かり金(デポジット)として 500 円がデフォルトでチャージされているものとする
  def __init__(self):
    self._deposit = 500

  # Step1 Suica は現在のチャージ残高を取得できる 
  @property
  def deposit(self):
    return self._deposit
  
  # Step1 Suica には 100 円以上の任意の金額をチャージできる
  @deposit.setter
  def deposit(self, money):
    try:
      money = int(money)
    except ValueError:
      raise ValueError("整数で入力してください(例：120)")
    
    # Step1 100 円未満をチャージしようとした場合は例外を発生させる
    if money < 100:
      raise ValueError("100円以上の金額を入力してください(例：120)")
    
    self._deposit += money

if __name__ == "__main__":
  haruka_suica = Suica()
  print(haruka_suica.deposit)

  try:
    haruka_suica.deposit = 80
  except ValueError as e:
    print(e)

  print(haruka_suica.deposit)

  try:
    haruka_suica.deposit = 150
  except ValueError as e:
    print(e)


  print(haruka_suica.deposit)



