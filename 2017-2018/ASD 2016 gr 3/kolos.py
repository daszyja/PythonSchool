# coding: utf-8


class Stack(object):
    """stos z appendem"""

    def __init__(self):
        super(Stack, self).__init__()
        self.l = []

    def push(self, o):  # O(1)
        self.l.append(o)

    def pop(self):  # O(1)
        if self.is_empty():
            return None
        return self.l.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def size(self):
        return len(self.l)

    def __str__(self):  # O(n)
        w = ""
        dlugosc = len(max(map(str, self.l), key=len))
        for i in range(len(self.l)):
            w += str(self.l[i]).center(dlugosc) + '\n'
        return w + '=' * dlugosc


"""
### Z1

Zaimplementowac funkcje compute postfix med, ktora dla podanego stringa skladajace-
go sie z ciagu cyfr oraz znakow dzialan +, −, ∗, /, m (m oznacza mediane z trzech liczb, jest to
zatem operacja trzyargumentowa) oddzielonych spacjami, w ktorym zapisane bedzie wyrazenie
w notacji postfixowej, zwraca wartosc wyrazenia, np.
compute postfix med(’4 5 − 2 ∗ 3 2 m’) == 2 (= med((4 − 5) ∗ 2, 3, 2))
Uwaga nr 1: Wykorzystaj klase Stos zaimplementowana przez siebie na zajeciach.
Uwaga nr 2: Napisz rozwiazanie bez pomocniczych stringow.
"""


def compute_postfix_med(text=''):
    s = Stack()
    for c in text:
        if c.isdigit():
            s.push(c)
        elif c in '/*-+m':
            temp = s.pop()
            if c == 'm':
                temp2 = s.pop()
                templ = sorted([s.pop(), temp2, temp])
                s.push(templ[1])
            else:
                s.push(str(eval(s.pop() + c + temp)))
    return int(s.pop())


def test_compute_postfix_med():
    assert compute_postfix_med('4 5 − 2 ∗ 3 2 m') == 2

"""
### Z2

Dopisz metode str do klasy Queue zaimplementowanej z wykorzystaniem listy dowiaza-
nej (mozesz wykorzystac implementacje wykorzystana przez prof. Baczynskiego na wykladzie).
Przyklad:
» Q=Queue()
» Q.enqueue(3)
» Q.enqueue(5)
» Q.enqueue(2)
» print Q
Tail 2 | 5 | 3 Head
Jaka jest zlozonosc kazdej z metod w tej klasie?






wszystkie operacje oprócz __str__  mają złożoność O(1)
__str__ ma zlozonosc O(n), gdzie n to ilość elementów w liscie
"""

import sys


class Node:

    def __init__(self, dane=None, next_node=None):
        self.dane = dane
        self.next_node = next_node

    def __str__(self):
        return str(self.dane)


class Queue:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
        self.pamiec = 0
        self.max_pamiec = 4294967296  # zalozenie - 4GB wolnej pamieci

    def is_empty(self):
        return self.length == 0

    def enqueue(self, dane):
        self.pamiec += sys.getsizeof(dane) + sys.getsizeof(Node)
        if self.pamiec > self.max_pamiec:
            raise MemoryError("Brak wolnej pamieci!")
        t = self.tail
        self.tail = Node(dane)
        if self.is_empty():
            self.head = self.tail
        else:
            t.next_node = self.tail
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Kolejka FIFO jest pusta!")
        self.pamiec -= sys.getsizeof(self.head.dane) + sys.getsizeof(Node)
        self.head = self.head.next_node
        self.length -= 1

    def first(self):
        if self.is_empty():
            raise ValueError("Kolejka FIFO jest pusta!")
        return self.head.dane

    def size(self):
        return self.length

    def __str__(self):
        output = ""
        if not self.is_empty():
            temp = self.head
            while temp.next_node != None:
                output = ' | ' + str(temp.dane) + output
                temp = temp.next_node
            output = str(temp.dane) + output
        return "Tail " + output + " Head"


def test_queue():
    q = Queue()
    assert str(q) == "Tail  Head"
    q.enqueue(1)
    q.enqueue(2)
    assert str(q) == "Tail 2 | 1 Head"
    q.enqueue(5)
    assert str(q) == "Tail 5 | 2 | 1 Head"
    q.dequeue()
    q.dequeue()
    assert str(q) == "Tail 5 Head"
"""
### Z3

Napisz funkcje taki sam( ), ktora dla dwoch podanych list posortowanych rosnaco (=nie-
malejaco) sprawdzi, czy istnieja w nich choc dwa identyczne elementy. Odpowiedzia powinno
byc True zarowno w przypadku, gdy te dwa rowne elementy znajduja sie w jednej z list, jak
i gdy kazdy z nich jest w innej.
W komentarzu podaj dokladna liczbe porownan wykonanych przez funkcje w przypadku
pesymistycznym oraz optymistycznym - przy zalozeniu, ze rozmiar jednej z list to m, a drugiej n.
"""


def taki_sam(lista_a, lista_b):
    i, j = 0, 0
    while i < len(lista_a) - 1 and j < len(lista_b) - 1:
        if lista_a[i] == lista_b[j]:
            return True
        if i + 1 < len(lista_a) and lista_a[i] == lista_a[i + 1]:
            return True
        if j + 1 < len(lista_b) and lista_b[j] == lista_b[j + 1]:
            return True

        if lista_a[i] < lista_b[j]:
            i += 1
        else:
            j += 1

    while i < len(lista_a) - 1:
        if lista_a[i] == lista_a[i + 1]:
            return True
        i += 1

    while j < len(lista_b) - 1:
        if lista_b[j] == lista_b[j + 1]:
            return True
        j += 1

    return False

"""
ilośc porównań pomiędzy elementami listy ( bez uwzględniania porównań zmiennych iteracyjnych do długości poszczególnych list )

w przypadku pesymistycznym listy są sobie równe długością lecz żaden element nie jest taki sam i elementy listy są na przemian większe w jednej i mniejsze w drugiej:
    m = n = długość listy
    4*m - bo są w każdej iteracji 4 porównania pomiędzy elementami

w przypadku optymistycznym:
    jedno porównanie pomiędzy elementami listy lista_a[0] == lista_b[0]
    1

"""


def test_taki_sam():
    assert taki_sam(sorted([123, 444, 31, 5, 2, 3, 12]), sorted([23, 4142, 5, 1245, 2]))
    assert taki_sam(sorted([123, 444, 31, 5, 2, 5, 12]), sorted([23, 4142, 6, 1245, 2]))
    assert taki_sam(sorted([2, 3, 4, 5, 6]), sorted([-1, -2, -3, -4, -5])) == False
