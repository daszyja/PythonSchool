'''Zad3 warunek stopu, niezmiennej petli'''


def max_dif_geq(T):
    mini = T[0]
    maxi = T[0]
    idmax = 0
    idmin = 0
    for i in xrange(1, len(T)):
        if T[i] > maxi and i >= idmin:
            maxi = T[i]
            idmax = i
        elif T[i] < mini and idmin >= idmax:
            mini = T[i]
            idmin = i
    return maxi - mini


print max_dif_geq([1, 2, 3, 1, 5, 6])


def lider(tab):
    ''' lider to taki ktory wystepuje wiecej razy niz polowa listy'''

    pass


tab = [1, 2, 3, 1, 5, 6]
tab_str = []

tab_str.append('%d %d' % (tab[0], ))
