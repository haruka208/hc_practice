class Pokemon:
  name = "リザードン"
  type1 = "ほのお"
  typw2 = "ひこう"
  hp = 100
  mp = 10

  def attack(self):
    print(f"{self.name}のこうげき！")

def main():
    poke = Pokemon()

    print(poke.name)
    print(poke.type1)
    print(poke.mp)
    poke.attack()

main()

