from suica_refactored import Suica 

# Step2 ジュースは名前と値段の情報をもつ
class Juice:
  def __init__(self, name, price):
    self.name = name
    self.price = price

# Step2 自動販売機はジュースを１種類格納できる
# 🌟 Step4 ジュースを 3 種類管理できるようにする。
class VendingMachine:
  def __init__(self):
    self._sales_money = 0

    # Step2 初期状態で、ペプシ(150 円)を 5 本格納している。
    # self.stock_pepsi = []
    # for _ in range(5):
    #   self.stock_pepsi.append(Juice("ペプシ", 150))

    # 🌟 Step4 初期在庫にモンスター(230 円)5 本を追加する。
    # self.stock_monster = []
    # for _ in range(5):
    #   self.stock_monster.append(Juice("モンスター", 230))

    # 🌟 Step4 初期在庫にいろはす(120 円)5 本を追加する。
    # self.stock_irohas = []
    # for _ in range(5):
    #   self.stock_irohas.append(Juice("いろはす", 120))

    juice_data = [
      ("pepsi", "ペプシ", 150),
      ("monster", "モンスター", 230),
      ("irohas", "いろはす", 120),
    ]

    self.stock = {}

    for key, name, price in juice_data:
      juice_list = []
      for _ in range(5):
        juice = Juice(name, price)
        juice_list.append(juice)
      self.stock[key] = juice_list
  
  # Step2 自動販売機は在庫を取得できる　# VendingMachineの中でnameを定義していないので、self.nameは使えない
  # 🌟 → Step4 自動販売機は在庫を取得できる

  # def now_stock(self):
  #   for key in self.stock:
  #     drinks = self.stock[key]
  #     if drinks:
  #       name = drinks[0].name
  #       amount = len(drinks)
  #       # print(f"{name}が{amount}本あります")
  #       return name, amount
  #     else:
  #       # print(f"{key}は売り切れです")
  #       return key

  def now_stock(self):
    stock_list = []
    for key, drinks in self.stock.items():
      if drinks:
        name = drinks[0].name
        amount = len(drinks)
        stock_list.append((name, amount))
      else:
        stock_list.append((key, 0))
    return stock_list

# Step3 自動販売機はペプシが購入できるかどうかを取得できる。
  def buy_pepsi(self, suica):
    # Step3 チャージ残高が足りない場合もしくは在庫がない場合、購入操作を行った場合は例外を発生させる
    if not self.stock:
      raise Exception("在庫がありません")
    
    if suica._deposit < 150:
      raise ValueError("チャージ金額が足りません")

    # Step3 ジュース値段以上のチャージ残高がある条件下で購入操作を行うと以下の動作をする

    # Step3 自動販売機はジュースの在庫を減らす
    # self.stock.remove(0)
    self.stock["pepsi"].pop(0)

    # Step3 売り上げ金額を増やす
    self._sales_money += 150

    # Step3 Suica のチャージ残高を減らす
    suica._deposit -= 150
    # print("ペプシを購入しました")
    return "ペプシを購入しました"

# 🌟 → Step4 ステップ 3 と同様の方法でモンスターといろはすを購入できる
  def buy_juice(self, suica, drink_key):
    drinks = self.stock[drink_key]
    # if len(drinks) == 0:
      # raise Exception(f"{drinks[0].name}の在庫がありません")
    if not drinks:
      raise Exception(f"{drink_key}の在庫がありません")
    

    price = drinks[0].price

    if suica.deposit < price:
      raise ValueError("チャージ金額が足りません")

    # juice = self.stock[drink_key].pop(0)
    juice = drinks.pop(0)
    self._sales_money += price
    suica._deposit -= price

    # print(f"{juice.name}を購入しました")
    return juice.name

  # Step3 自動販売機は現在の売上金額を取得できる
  def sales_money(self):
    # print(f"現在の売上は{self.sales_money}円です")
    return self._sales_money

# 🌟 Step4 自動販売機は購入可能なドリンクのリストを取得できる
  def drink_list(self, suica):
    available_list = []
    for key in self.stock:
      drinks = self.stock[key]

      if len(drinks) == 0:
        continue

      price = drinks[0].price

      if suica._deposit >= price:
        available_list.append(drinks[0].name)

    if available_list:
      # print(f"購入可能なドリンクのリストは{available_list}です")
      return available_list
    else:
      # print("購入可能なドリンクはありません")
      return "購入可能なドリンクはありません"

# 🌟 Step4 自動販売機に在庫を補充できるようにする
  def append_stock(self, drink_key, amount):
    name = self.stock[drink_key][0].name
    price = self.stock[drink_key][0].price
  
    for _ in range(amount):
      self.stock[drink_key].append(Juice(name, price))
  
    # print(f"{name}を{amount}本補充しました")
    return name, amount

# 📚
# try-exceptかraiseに統一
# 標準入力と標準出力を排除したコードに修正☑️
# セッターメソッド、ゲッターメソッドを定義☑️
# 残高や売上金額は外部から書き換えられないように☑️


if __name__ == "__main__":
  # pepsi = Juice("pepsi", 150)
  # print(pepsi)

  ven = VendingMachine()
  print(ven.now_stock())

  haruka_suica = Suica()
  print(ven.drink_list(haruka_suica))
  print(ven.buy_pepsi(haruka_suica))
  # ven.buy_pepsi(haruka_suica)
  # ven.buy_pepsi(haruka_suica)
  # ven.buy_pepsi(haruka_suica)

  haruka_suica.deposit = 300
  print(ven.buy_juice(haruka_suica, "irohas"))
  print(ven.buy_juice(haruka_suica, "pepsi"))
  print(ven.buy_juice(haruka_suica, "monster"))

  print(ven.sales_money())
  print(ven.drink_list(haruka_suica))
  print(ven.buy_juice(haruka_suica, "irohas"))
  print(ven.drink_list(haruka_suica))

  print(ven.now_stock())
  print(ven.append_stock("irohas", 3))
  print(ven.now_stock())