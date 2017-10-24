# Implementacja stosu jako Abstrakcyjnej Struktury Danych (ADT-Abstract Data Type)

class Node:
    """klasa wezel"""
    def __init__(self, element):
        self.dane = element
        self.next = None

class Stack:
    """Implementacja stosu z apomoca listy dowiazanej z wykorzystaniem klasy wezel"""
    def __init__(self):
        """iicjalizacja"""
        self.head = None
        self.lb_el = 0

    def isEmpty(self):
        """sprawdzenie czy stos jest pusty"""
        return self.lb_el == 0

    def push(self, element):
        """wlozenie elementu na stos"""
        n = Node(element)
        n.next = self.head
        self.head = n
        self.lb_el += 1
        return

    def pop(self):
        """sciagniecie eleemntu ze stosu"""
        if self.isEmpty():
            return False #ewentualnie wywolaj wyjatek
        n = self.head
        self.head = self.head.next
        self.lb_el -= 1
        return

    def top(self):
        """zwrocenie eleemntu ze szczytu stosu"""
        if self.isEmpty():
            return False  #ewentualnie wywolaj wyjatek
        return self.head.dane

    def size(self):
        """zwraca rozmiar stosu"""
        return self.lb_el

s = Stack()
print "rozmiar", s.size()
s.push(1)
s.push(2)
print "rozmiar", s.size()
s.pop()
print "rozmiar", s.size()
s.push(3)
print s.top()
s.pop()
print s.top()
print "rozmiar", s.size()
