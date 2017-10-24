from random import randint as RANDOM
import time


def insertion_sort(A):
    for i in xrange(len(A) - 1):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j] = A[j - 1]
            i = j - 1
    return A


A = [-2, -1, 3, 4, 2, 66]
print insertion_sort(A)
'''liczba operacji elementarntych wzgledem rozmiaru danych'''

'''
Zad 02
'''
start_time = time.time()
A = [-2, -1, 3, 4, 2, 66]
print insertion_sort(A)
print("--- %s seconds ---" % (time.time() - start_time))

t2 = time.time()
A = [-2, -1, 3, 4, 4, 66]
print insertion_sort(A)
print("--- %s seconds ---" % (time.time() - t2))

t3 = time.time()
A = [66, -2, -1, 3, 4, 4]
print insertion_sort(A)
print("--- %s seconds ---" % (time.time() - t3))
tab = []
for i in range(10 ** 2):
    tab.append(RANDOM(-100, 100))
print tab
print len(tab)
start_time = time.time()
insertion_sort(tab)
print("--- %s seconds ---" % (time.time() - start_time))


'''
zad4 porowynanie leksykograficzne
ala < bela
Prawda (zaczynamy od lewej strony)
a jest mniejsze od b
wiec to jest Prawda

gdyby bylo ale > abla
to porownuje a z a (ta sama, wiec idzie do nastepnej liczbr)
isdigit
A[i].isdigit()

w pythonie domyslnie liczba jest mniejsza od znakow alfabetu

do 5 zad
sorted(L, key= cup_to_key(..) (wedlug czego ma porownywac))
'''
