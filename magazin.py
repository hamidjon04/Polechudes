class Magazin:
    def Magazin(self, player):
        if player.ball == 0:
            print("Ishtirokingiz uchun rahmat. Kayfiyatni tushirmang.")
            return "30 ta kitob + 5.000.000 so'mlik ta'lim granti"
        elif player.ball <= 100:
            print("Ishtirokingiz uchun rahmat.")
            return "30 ta kitob + 10.000.000 so'mlik ta'lim granti"
        elif player.ball <= 500:
            print("Ishtirokingiz uchun rahmat.")
            return "50 ta hitob + 20.000.000 so'mlik ta'lim granti"
        elif player.ball <= 1000:
            print("Ishtirokingiz uchun rahmat.")
            return "100 ta kitob + 30.000.000 so'mlik ta'lim granti"
        elif player.ball < 5000:
            print("Ishtirokingiz uchun rahmat.")
            return "200 ta kitob + 50.000.000 so'mlik ta'lim granti"
        elif player.ball >= 5000:
            print("Ishtirokingiz uchun rahmat.")
            return "500 ta kitob + 100.000.000 so'mlik ta'lim granti"
