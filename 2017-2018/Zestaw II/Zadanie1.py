'''Zadanie1 Napisz funkcję w języku Python (lub wykorzystaj funkcję z poprzednich zajęć), który w oparciu o stos
oblicza wartość wyrażenia zapisanego w notacji postfiksowej. Zakładamy, że korzystamy z 4 klasycznych
operacji arytmetycznych +, -, * oraz /. Przykładowo dla danych wejściowych ”20 10 + 75 45 - * ” wynik
powinien wynosić 900.
Funkcję proszę nazwać Postfix Eval().'''
from stack import Stack

stos = Stack()
def Postfix_Eval(word):
    tempdig = ''
    for c in word:
        if c.isdigit():
            tempdig += c
        elif c in '/*-+':
            temp = str(stos.pop())
            stos.push(eval(str(stos.pop())+c+temp))
        elif c == ' ' and tempdig != '':
            stos.push(tempdig)
            tempdig = ''
    return stos.pop()



print(Postfix_Eval('20 10 + 75 45 - *'))
