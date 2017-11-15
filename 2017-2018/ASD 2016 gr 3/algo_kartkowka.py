# coding: utf-8
'''
Posortuj plik Białka.txt (Bialka2.txt) - tym razem w taki sposób, aby w posortowanym pliku na początku znajdowały się wiersze, w których litera "A" (lub "a") pojawiła się na wcześniejszej
 pozycji (w przypadku "remisu", np. "Lak" i "oAaaaza" <pierwsze "a" na 2. pozycji> czy "goryl" i "1" (brak "a")- kolejność wierszy może być dowolna).

Prześlij posortowany plik wynikowy oraz wykorzystany przez siebie plik z kodem. Tym razem "Kto pierwszy ten lepszy" - ci,
którzy pierwsi prześlą poprawnie posortowane pliki, otrzymają najwięcej punktów :)
'''

f = open("Bialka.txt")
lines = f.readlines()


keys = {}
def compare(a,b):
    if a not in keys:
        try:
            keys[a] = a.lower().index('a')
        except Exception as e:
            keys[a] = 999

    if b not in keys:
        try:
            keys[b] = b.lower().index('a')
        except Exception as e:
            keys[b] = 999
    return cmp(keys[a], keys[b])



lines_sorted = sorted(lines, cmp=compare)

f = open("Bialka_sorted.txt","w+")
f.writelines(lines_sorted)
