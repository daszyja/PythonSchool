'''Zaimplementowac klasy Stack oraz StackBack - obie maja miec te sama funkcjonalnosc

klasycznego stosu (metody: push(item), pop(), top(), is empty(), size()), obie maja byc za-
implementowane za pomoca list. Dodanie elementu do obiektu klasy Stack ma byc zaimple-
mentowane poprzez dodanie elementu na koniec listy, natomiast dodanie elementu do obiektu

klasy StackBack ma byc zaimplementowane poprzez dodanie lementu na poczatek listy (ap-
pend()/insert(0,..)).

Podac zlozonosc operacji push(item) i pop() przy obu implementacjach.'''

class Stack:
    """docstring for Stack."""
    def __init__(self):
        self.items = []
    def isEmpty(self):

        return self.items == []
    def push(self,item):
        '''wrzucenie elementu na stos'''
        self.items.append(item) #o1
        return
    def pop(self):
        '''sciagniecie elemtu z stosu'''
        self.items.pop()
        return
    def top(self):
        '''zwracam element z gory stosu'''
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

class StackBack:
    """docstring for Stack."""
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        '''wrzucenie elementu na stos'''
        self.items.insert(0,item)
        return
    def pop(self):
        '''sciagniecie elemtu z stosu'''
        self.items.pop(0)
        return
    def top(self):
        '''zwracam element z gory stosu'''
        return self.items[0]
    def size(self):
        return len(self.items)
    def wypisz(self):
        print self.items
