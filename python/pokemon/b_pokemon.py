class Pokemon:
  def __init__(self, name, type1, type2, hp):
    self.name = name
    self.type1 = type1
    self.type2 = type2
    self.hp = hp

  def attack(self):
    print(f"{self.name}のこうげき！")

class Pikachu(Pokemon):
  def attack(self):
    super().attack()
    print(f"{self.name}の10万ボルト!")

class Zenigame:
  def attack(self):
    print(f"{self.name}のみずでっぽう!")

def main():
  pika = Pikachu("ピカチュウ", "でんき", "", 100)

  print(pika.name)
  pika.attack()


poke = Pokemon("ピカチュウ")
print(poke.name)

main()


