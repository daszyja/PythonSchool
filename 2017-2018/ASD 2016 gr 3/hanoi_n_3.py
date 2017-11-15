# coding: utf-8
"""
Napisz rekurencyjny program rozwiązujący problem wież Hanoi, jeśli mamy
3n krążków, po 3 w każdym rozmiarze (i krążki w tym samym rozmiarze są
"nierozróżnialne" - mogą być ułożone w dowolnej kolejności).

Jaka jest złożoność Twojego rozwiązania (niech print będzie operacją elementarną) - dokładna i asymptotyczna?

Ile około dni zajęłoby mnichowi przełożenie w ten sposób wieży złożonej ze 150
krążków, przy założeniu, że jest on mistrzem w swoim fachu i przełożenie
1 krążka zajmuje mu 1 sekundę, a pracuje 12 godzin dziennie bez chwili
wytchnienia? (mnich przekłada zawsze po jednym krążku)

"""


def hanoi(n):
    ''' n - liczba krążków ( w sumie )
    wypisuje kolejne ruchy potrzebne do przelozenia wszystkich krążków z pręta A na pręt B
    zwraca None'''

    n_int = 0
    try:
        n_int = int(n)
    except Exception as e:
        return
    assert n_int % 3 == 0
    n_int /= 3

    print("Ilość potrzebnych ruchów: %d." % 3*(2**(n_int) - 1))


    def hanoi_rek(n, a='A', b='B', c='C'):
        ''' funkcja obsługująca rekurencję '''
        if n == 1:
            print("(%s, %s)" % (a, b))
            print("(%s, %s)" % (a, b))
            print("(%s, %s)" % (a, b))
            return
        hanoi_rek(n - 1, a, c, b)
        print("(%s, %s)" % (a, b))
        print("(%s, %s)" % (a, b))
        print("(%s, %s)" % (a, b))
        hanoi_rek(n - 1, c, b, a)
        return

    # if raw_input('Czy chcesz wypisać rozwiązanie? T/N: ') == 'T':
    hanoi_rek(n_int)
    return


hanoi(raw_input())
print("Ilość dni: %d." % 3*(2**(50) - 1))
