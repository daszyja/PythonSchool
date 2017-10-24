def one_a(n, suma=0):
    '''Suma wszystkich wyrazow tego ciagu'''
    for i in range(0, n):
        suma = i + suma
    return suma
# print one_a(10)


def one_b(n, suma=1):
    '''Iloczyn wszystkich wyrazow tego ciagu'''
    for i in range(1, n):
        suma = i * suma
    return suma

# print one_b(5)


def one_c(n, srednia=0):
    '''Srednia arytm. wszystkich wyrazaow w ciagu'''
    for i in range(1, n + 1):
        srednia += i
    return srednia / n

# print one_c(9)


def one_d(n, k, srednia_p=0, licz=0):
    '''Srednia arytm. wszystkich dodatnich wyrazow'''
    for i in range(n, k + 1):
        if i > 0:
            licz += 1
            srednia_p += i
    return srednia_p / licz

# print one_d(-2, 3)


def one_e(n, tab=[]):
    ''' a1 + a1a2 + a1a2a3 '''
    for i in range(0, n):
        for j in range(1, i):
            print j

# print one_e(5)


def one_f(Wiel=[], liczba=0):
    ''' a0 + a1 + a2x + a3x^2 + a4x^3
        f(x) = 7x^3 - 5x^2 + x -2'''
    zerowy = Wiel[0]
    for i in range(1, len(Wiel)):
        przemno = liczba * zerowy
        zerowy = Wiel[i] + przemno
    print zerowy

# one_f([5, 4, 3, 2, 1], 2)


def two_one(tab):
    '''wystarczy znac najw i najmniejszy element'''
    maxi = tab[0]
    mini = tab[0]
    for i in range(0, len(tab) - 1):
        if maxi < tab[i + 1]:
            maxi = tab[i + 1]
        if mini > tab[i + 1]:
            mini = tab[i + 1]

    print maxi, mini
    return maxi - mini


tablica = [-1, 5, -3, 200, 7, 8, -2, -4, 3, 6, 8, 9, 1]
tab = [200, 2, 3, 1, 101, 3, 300]

print two_one(tab)
