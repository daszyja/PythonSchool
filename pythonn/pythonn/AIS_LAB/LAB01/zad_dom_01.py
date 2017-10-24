def licznik_operacji_hornera(wiel=[], liczba=0):
    ''' a0 + a1 + a2x + a3x^2 + a4x^3
        f(x) = 7x^3 - 5x^2 + x -2'''
    zer = wiel[0]
    for i in range(1, len(wiel)):
        przemno = liczba * zer
        zer = wiel[i] + przemno
    print zer

licznik_operacji_hornera([5, 4, 3, 2, 1], 1)


def last_index(T, e):
    '''Returns index of last occurence of elte e in list'''
    for i in range(len(T) - 1, 0, -1):
        if T[i] == e:
            return "alte e founded [%s]: on position [%d]" % (e, i)


print last_index([1, 2, 3, 4, 'Sgm', 4], 'Sgm')


def max_diff(arg):
    '''Looks for the biggest difference of 2 elements where it doesn't
       matter where i,j are'''
