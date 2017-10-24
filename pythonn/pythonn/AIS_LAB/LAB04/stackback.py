
class StackBack:
    """docstring for Stack."""
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        '''wrzucenie elementu na stos'''
        self.items.insert(0,item) #n
    def pop(self):
        '''sciagniecie elemtu z stosu'''
        return self.items.pop(0) #
    def top(self):
        '''zwracam element z gory stosu'''
        return self.items[0]
    def size(self):
        return len(self.items)
    def wypisz(self):
        print self.items
    def __str__(self):
        maxlen = 0
        wynik = ''
        maxlen = max([len(str(x)) for x in self.items]) # n+n-1
        for i in self.items:
            wynik += str(i).center(maxlen) + '\n'
        wynik += '=' * maxlen

        return wynik
s = StackBack()
s.push('a')
s.push('bbadasdsa')
s.push(8)
print s
