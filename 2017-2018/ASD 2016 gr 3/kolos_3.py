# coding: utf-8
'''Napisz funkcję najczęściej(L), która dla
podanej jako argument listy L tworzy i zwraca nową listę, w której są te same
elementy co w L, ale się nie powtarzają i są ustawione w kolejności od tych,
które w L występują najczęściej.

Np. najczęściej([2,5,1,1,1,5]) powinno zwrócić
[1,5,2].'''


def najczesciej(L):
    m = max(L) + 1
    county = [0] * m
    for i in L:
        county[i] += 1
    i = 0
    for a in range(m):
        L[i] = a
        i += county[a]
    return L

print najczesciej([5,1,1,2,2,2,2,2,5,4,4,4,19])
