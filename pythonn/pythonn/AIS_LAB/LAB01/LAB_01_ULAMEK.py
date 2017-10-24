class Ulamek():
    """docstring for Ulamek."""

    def __init__(self, licznik, mianownik):
        self.licz = licznik
        self.mian = mianownik
        self.ulamek = self.licz / float(self.mian)

    def __str__(self):
        '''Wypisywanie ulamka'''
        return "Wypisanie ulamka: %0.5f" % (self.ulamek)

    def __add__(self, inny_licznik, inny_mianownik):
        '''Nalezy znalezc najwiekszy wspolny dzielni (NWD) aby, moc sprowadzic
           ulamki na wspolny mianownik'''
        przemno = self.nwd(self.mian, inny_mianownik)
        if inny_mianownik != self.mian:
            self.licz *= inny_mianownik
            inny_licznik *= self.mian

            koncowy_mian = self.mian * inny_mianownik
            koncowy_licz = self.licz + inny_licznik
            przemno = self.nwd(koncowy_licz, koncowy_mian)
            while przemno != 1:
                koncowy_licz, koncowy_mian = koncowy_licz / przemno, koncowy_mian / przemno

            return "Dodany ulamek to: %d / %d" % (koncowy_licz, koncowy_mian)
        else:
            return "Dodany ulamek to: %d / %d" % (self.licz + inny_licznik, self.mian)

    def nwd(self, a, b):
        return a if b == 0 else self.nwd(b, a % b)

    def nww(self, a, b):
        return a * b / self.nwd(a, b)

    def __eq__(self, inny_licznik, inny_mianownik):
        '''Czy ulamek jest rowny z innym ulamkeim'''
        innyulamek = inny_licznik / float(inny_mianownik)
        return "%0.2f rowny z %0.2f?: NIE" % (self.ulamek, innyulamek) if self.ulamek != innyulamek else "%0.2f rowny z %0.2f?: TAK" % (self.ulamek, innyulamek)

a = Ulamek(4, 3)
# print a
# print a.__eq__(3, 4)
# print a.nwd(243, 111)
print a.__add__(3, 5)
# print a.nww(2, 3)
