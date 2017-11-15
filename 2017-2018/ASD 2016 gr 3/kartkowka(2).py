class StackBack(object):
    """stos z insertem"""

    def __init__(self): #O(1)
        super(StackBack, self).__init__()
        self.l = []

    def push(self, o): #O(n)
        self.l.insert(0, o)

    def pop(self): #O(n)
        self.pop(0)

    def top(self): #O(1)
        return self.l[0]

    def is_empty(self): #O(1)
        return len(self.l) == 0

    def size(self): #O(1)
        return len(self.l)

    def __str__(self): #O(n)
        w = ""
        dlugosc = len(max(map(str, self.l), key=len))
        for i in range(len(self.l)):
            w += str(self.l[i]).center(dlugosc) + '\n'
        return w + '=' * dlugosc


SB = StackBack()
SB.push(1)
SB.push('zima!')
SB.push('23')
print SB
