from abc import ABC, abstractmethod
class NameService(ABC):
  @abstractmethod
  def change_name(self, new_name):
    pass
  
  @abstractmethod
  def get_name(self):
    pass
  

class Pokemon(NameService):
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
  
class Player(NameService):
  def __init__(self):
    self.__name = ""

  def change_name(self, new_name):
    if new_name == "うんこ":
      print("不適切な名前です")
      return
    self.__name = new_name

  def get_name(self):
    return self.__name