from player import Player
from magazin import Magazin
from polechudes import Polechudes 

# o'yinning functionlari joylashgan class
p = Polechudes()

# o'yinchilar 
p1 = Player("Sardor")
p2 = Player("Komil")
p3 = Player("Davron")

# magazin
m = Magazin()

p.savoll()
players = [p1, p2, p3]
while "|_|" in p.katak:
    if len(players) == 0:
        players = [p1, p2, p3]
    p.polechudes(players.pop(0))



max = max([p1.ball, p2.ball, p3.ball])
print("G'olib(lar)imiz: ")
for i in [p1, p2, p3]:
    if max == i.ball:
        print(i.name)

print("Sovg'alar: ")
for i in [p1, p2, p3]:
    print(f"{i.name} => {m.Magazin(i)}")
        
    

    