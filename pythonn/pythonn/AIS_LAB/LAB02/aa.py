import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Gra():
    """docstring for Gra
    8 mozliwosci do wygrania
    na skos 2x
    pionowo 3x
    poziomo 3x"""

    def __init__(self, operacja):
        self.operacja = operacja
        obszarGry = []
        pomoc = []
        kolejka = 0
        koniecGry = False
        self.koniecGry = koniecGry
        self.obszarGry = obszarGry
        self.pomoc = pomoc
        self.kolejka = kolejka
        pass

    def Obszar(self):
        """Maluje ObszarGry podstawowe"""
        if (self.koniecGry is False):
            if (self.kolejka == 0):
                for j in range(0, 9):
                    self.obszarGry.append("[]")
                self.kolejka += 1
            print "\n"
            print "\t  ", self.obszarGry[0], self.obszarGry[1], self.obszarGry[2], "\n"
            print "\t  ", self.obszarGry[3], self.obszarGry[4], self.obszarGry[5], "\n"
            print "\t  ", self.obszarGry[6], self.obszarGry[7], self.obszarGry[8], "\n"
            print "--" * 20
            print "\t Kolko i Krzyzyk"
            print "--" * 20

    def poczatekGry(self):
        while (self.koniecGry is False):
            operacja.Obszar()
            operacja.ruch("x")
            cls()
            operacja.Obszar()
            operacja.ruch("o")
            cls()
            pass

    def ruch(self, player):
        operacja.CzyWygrana(player)
        """W tej klasie gracz podaje w jakim polu dac znak + sprawdza
           sie czy Dany Gracz Wygral"""
        if (self.koniecGry is False):
            operacja.CzyWygrana(player)
            print "\t> Ruch gracza [", player, "]"
            znak = input("\t> Gdzie chcesz dac znak (0-9): ")
            znak -= 1
            self.obszarGry[znak] = player

    def CzyWygrana(self, znak):
        if self.obszarGry[0] == znak and self.obszarGry[1] == znak and self.obszarGry[2] == znak:
            print "Koniec gry"
            self.koniecGry = True
        elif self.obszarGry[3] == znak and self.obszarGry[4] == znak and self.obszarGry[5] == znak:
            print "Koniec gry"
            self.koniecGry = True
        elif self.obszarGry[6] == znak and self.obszarGry[7] == znak and self.obszarGry[8] == znak:
            print "Koniec gry"
            self.koniecGry = True
        elif self.obszarGry[0] == znak and self.obszarGry[3] == znak and self.obszarGry[6] == znak:
            print "Koniec gry"
            self.koniecGry = True
        elif self.obszarGry[1] == znak and self.obszarGry[4] == znak and self.obszarGry[7] == znak:
            print "Koniec gry"
            self.koniecGry = True
        elif self.obszarGry[2] == znak and self.obszarGry[5] == znak and self.obszarGry[8] == znak:
            print "Koniec gry"
            self.koniecGry = True
        elif self.obszarGry[0] == znak and self.obszarGry[4] == znak and self.obszarGry[8] == znak:
            print "Koniec gry"
            self.koniecGry = True
        elif self.obszarGry[6] == znak and self.obszarGry[4] == znak and self.obszarGry[2] == znak:
            print "Koniec gry"
            self.koniecGry = True


operacja = Gra(1)
cls()
operacja.poczatekGry()
