'''Matura PR 2008'''

'''Zadanie 1'''


def potegi(k):
    '''Zwraca reszte z dzielenia przez 10 liczby 2 ** k'''
    return 2 ** k % 10 if k >= 0 else "Invalid input [k], must be above 0."

# print potegi(15)


def liczba_a_do_n(a, k):
    '''a ** n, gdzie n = 2 ** k'''
    return a ** (2 ** k) if k >= 0 else "Invalid input [k], must be above 0."

# print liczba_a_do_n(2, -2)

'''Zadanie 2'''


def reg_2(wyraz, liczba_wyw=0):
    '''Sprawdzanie czy wyrazenie jest wyrazeniem 2-regularnym'''
    print "zajmujemy sie wyrazem %s, a jest to %d wywolanie rek" % (wyraz, liczba_wyw)
    len_wyraz = len(wyraz)
    if len_wyraz == 1:
        print "%s jest wyrazeniem 2-regularnym" % (wyraz)
        return "TAK"
    elif len_wyraz > 1 and len_wyraz % 2 != 0:
        return "NIE"
    elif len_wyraz > 1 and len_wyraz % 2 == 0:
        wyraz1, wyraz2 = wyraz[:len(wyraz) / 2], wyraz[len(wyraz) / 2:]
        if wyraz1 != wyraz2:
            return "NIE"
        else:
            liczba_wyw += 1
            return reg_2(wyraz1, liczba_wyw)

a4 = 'abab'
a1 = 'aabbaabb'
a2 = 'aaaaaaaa'
a3 = 'bbbbbbbbbbbbbbbbbbbb'
print len(a3)
print reg_2(a3)
