from abc import ABC, abstractmethod
class Pokemon(ABC):
  def __init__(self, type1, type2, hp):
    self.__name = "" # private変数
    self.type1 = type1
    self.type2 = type2
    self.hp = hp
  
  @abstractmethod
  def attack(self):
    pass

  def change_name(self, new_name):
    if new_name == "うんこ":
      print("不適切な名前です")
      return
    self.__name = new_name

  def get_name(self):
    return self.__name



class Pikachu(Pokemon):
  def attack(self):
    print(f"{super().get_name()}の10万ボルト!") # protected変数にしておけば、self._nameで子クラスからはアクセス可


def main():
  pika = Pikachu("でんき", "", 100)
  pika.attack()

main()

pokemon = Pikachu("でんき", "", 100)
pokemon.change_name("テキセツ")
print(pokemon.get_name())
pokemon.change_name("うんこ")
print(pokemon.get_name())