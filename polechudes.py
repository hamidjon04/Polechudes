from random import choice
from time import sleep
class Polechudes:
    def __init__(self):
        self.savollar = ["Hozirgi kunda dunyodagi eng ommabop dasturlash tillari qaysilar?",
                         "1984 asarining muallifi kim?",
                         "Mark Sukkerberk nimani yaratgan?",
                         "Marakana stadioni qaysi davlatda joylashgan?"]
        self.javoblar = ["JAVAPYTHON", "JORJORUEL", "FACEBOOK", "BRAZILIYA"]
        self.savol = ""
        self.javob = ""
        self.katak = "|_|"
        self.harflar = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    def savoll(self):
        self.savol = choice(self.savollar)
        self.javob = self.javoblar[self.savollar.index(self.savol)]
        self.katak = ["|_|" for i in range(len(self.javob))]

    def ball(self):
        ballar = ["Bankrot", 0, 50, 100, 200, 350, 500, 750, 1000, 400, 850, "2x"]
        ball = choice(ballar)
        return ball
    

    def polechudes(self, player):
        print(self.savol)
        print(self.katak)
        if "|_|" not in self.katak:
            return
        spin = input(f"{player.name} barabanni aylantirishga tayyormisiz? ")
        while spin.lower() != "ha":
            sleep(2)
            spin = input(f"{player.name} barabanni aylantirishga tayyormisiz? ")
        print("Ball =", ball := self.ball())
        if ball == "Bankrot":
            player.ball = 0
            return
        elif ball == 0:
            return
        print(self.harflar)
        harf = input("Harf: ").upper()
        self.harflar.remove(harf)
        if harf in self.javob:
            while harf in self.javob:
                self.katak[self.javob.index(harf)] = harf
                self.javob = self.javob.replace(harf, " ", 1)
                if ball == "2x":
                    player.ball *= 2
                else:
                    player.ball += ball
            print("Barakalla topdingiz.")
            self.polechudes(player)
        else:
            print("Bu harf mavjud emas!")
        print(f"{player.name} => ball = {player.ball}")
