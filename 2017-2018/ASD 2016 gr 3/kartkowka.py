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


# zadanie 4
def infix_to_postfix(text=''):
    stos = Stack()
    wynik = ''
    for c in text:
        if c.isalnum() or c == '.':
            wynik += c
        elif c == ')':
            wynik += ' ' + stos.pop()
        elif c in '/*-+':
            wynik += ' '
            stos.push(c)
    return wynik


# zadanie 6
def compute_postfix(text=''):
    s = Stack()
    was_digit = False
    for c in text:
        if c.isdigit():
            if was_digit:
                temp_digit = int(s.pop())*10 + int(c)
            else:
                temp_digit = c
            s.push(temp_digit)
            was_digit = True
        elif c in '/*-+':
            temp = s.pop()
            result = 0
            if c == '/':
                result = int(s.pop()) / int(temp)
            elif c == '*':
                result = int(s.pop()) * int(temp)
            elif c == '-':
                result = int(s.pop()) - int(temp)
            else:
                result = int(s.pop()) + int(temp)
            s.push(result)
            was_digit = False
        elif c == ' ':
            was_digit = False
    return s.pop()


def compute_infix(text):
    return compute_postfix(infix_to_postfix(text))


def test_compute_infix():
    assert compute_infix("(4*(12+3))") == 60
