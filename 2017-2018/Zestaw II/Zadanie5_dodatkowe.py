'''Zadanie4 Napisz funkcję w języku Python, która oblicza wartość wyrażenia zapisanego w notacji infiksowej. Za-
kładamy, że korzystamy z 4 klasycznych operacji arytmetycznych +, -, * oraz / oraz każde działanie

dwuargumentowe jest obłożone nawiasami.
Przykładowo dla danych wejściowych ”(11 + ((22 + 3) * (44 - 52)))” wynik powinien wynosić −189.
Funkcję proszę nazwać Infix nawiasy Eval() '''
from stack import Stack
stos=Stack()

def infix_to_postfix(infix_word):
    wyjscie=''
    for i in infix_word:
        if i.isalnum():
            wyjscie+=i
        elif i in '*/+-':
            stos.push(i)
        elif i == ')':
            wyjscie += stos.pop()
    return wyjscie

def to_postfiks(tekst):
    b = Stack()
    wynik = ''
    tmp = ''
    for char in tekst:
        if char == ')':
            wynik = wynik + " " + b.pop()
        elif char.isalnum() and char+1 != " ":
            wynik = wynik + " " + char
        elif char.isalnum
        elif char in '-+/*':
            b.push(char)
    return wynik

def compute_postfix_real(text):
    stos=Stack()
    tempdig = ''
    i = 0
    while i != len(text):
        c = text[i]
        cn = text[i +1] if i+1 < len(text) else ''
        if c.isdigit() or c=='.':
            tempdig += c
        elif c in '/*-+':
            if not cn.isdigit():
                temp = str(stos.pop())
                stos.push(eval(str(stos.pop())+c+temp))
            else:
                tempdig += c

        elif c == ' ' and tempdig != '':
            stos.push(tempdig)
            tempdig = ''
        i += 1
    return stos.pop()


print (compute_postfix_real('0.5 15 -5 - *'))
print (to_postfiks('(11 + ((22 + 3) * (44 - 52)))'))
