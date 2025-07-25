from abc import ABC, abstractmethod
class Pokemon(ABC):
  def __init__(self, name, type1, type2, hp):
    self.name = name
    self.type1 = type1
    self.type2 = type2
    self.hp = hp
  
  @abstractmethod
  def attack(self):
    pass

class Pikachu(Pokemon):
  def attack(self):
    print(f"{self.name}の10万ボルト!")

def main():
  pika = Pikachu("ピカチュウ", "でんき", "", 100)
  pika.attack()

main()

poke = Pokemon()
# print(poke) # TypeError: Can't instantiate abstract class Pokemon without an implementation for abstract method 'attack'