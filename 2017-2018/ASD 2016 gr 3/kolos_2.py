# coding: utf-8
'''
Zaimplementuj sortowanie przez kopcowanie, które będzie służyło do
sortowania napisów począwszy od tych, które zawierają najwięcej liter "a".

Następnie wczytaj plik o nazwie podanej przez użytkownika, posortuj
jego wiersze wg powyższej reguły i zapisz posortowane do pliku o tej samej
nazwie.
'''
from math import floor

def parent(k):
    return int(floor(k / 2))


def left(k):
    return 2 * k


def right(k):
    return 2 * k + 1


class HeapMin(object):
    """docstring for Heap."""

    def __init__(self, L=None):
        if isinstance(L, list):  # Czy pod ta zmienna stoi lista
            self.L = [0] + L
            self.size = len(self.L) - 1
            self.buildheap()
        else:
            self.L = [0]
            self.size = 0

    def __str__(self):
        '''printuje bez pierwszego 0'''
        return str(self.L[1:])

    def insert(self, n):
        self.L.append(n)
        self.size += 1
        self.fixup(self.size)

    def buildheap(self):
        '''Buduje kopiec na calej liscie od srodka wezlow'''
        for i in range(int(floor(self.size / 2)), 0, -1):
            self.fixdown(i)

    def fixup(self, k):
        if k > 1 and self.L[k].count("a") > self.L[parent(k)].count("a"):
            self.L[k], self.L[parent(k)] = self.L[parent(k)], self.L[k]
            self.k = parent(k)
            self.fixup(k)

    def fixdown(self, k):
        '''Jezeli ktores z dzieci rodzica sa wieksze od niego to zamienia'''
        l = left(k)
        r = right(k)
        largest = k
        if l <= self.size and self.L[l].count('a') < self.L[k].count('a'):
            largest = l
        if r <= self.size and self.L[r].count('a') < self.L[largest].count('a'):
            largest = r
        if largest != k:
            self.L[k], self.L[largest] = self.L[largest], self.L[k]
            self.fixdown(largest)
        return self

    def extractmax(self):
        ''' nlgn '''
        self.L[1], self.L[self.size] = self.L[self.size], self.L[1]
        a = self.L.pop()
        self.size -= 1
        self.fixdown(1)
        return a

    def heapsort(self):
        ''' T(heapsort, n) = theta (nlgn), wynikiem koncowy bedzie posortowana
            tablica, dlatego tez psuje wlasnosc kopca i musimy od poczatku'''
        for i in range(self.size):
            self.L[1], self.L[self.size] = self.L[self.size], self.L[1]
            self.size -= 1
            self.fixdown(1)
        return self.L[1:]




def test_sort():
    hm = HeapMin(["aaa", "aaaaaaa", "aa", "aabbaaa", "aaaaaaaaaaaaaaaabbbbbbbb"])
    assert hm.heapsort() == ['aaaaaaaaaaaaaaaabbbbbbbb', 'aaaaaaa', 'aabbaaa', 'aaa', 'aa']
