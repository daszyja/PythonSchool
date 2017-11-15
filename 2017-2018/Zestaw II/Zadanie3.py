# Napisz funkcję w języku Python, która w oparciu o stos przekształca wyrażenie zapisane w notacji infik-
# sowe w wyrażenie zapisane w notacji postfiksowej. Zakładamy, że korzystamy z 4 klasycznych operacji
#
# arytmetycznych +, -, * oraz / oraz każde działanie dwuargumentowe jest obłożone nawiasami.
# Przykładowo dla danych wejściowych ”((20 + 10) * (75 - 45))” wynik powinien wynosić ”20 10 + 75 45
# -*”.
# Funkcję proszę nazwać Infix to Postfix nawiasy().

from stack import Stack

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

print (infix_to_postfix('((20 + 10) * (75 - 45))'))
