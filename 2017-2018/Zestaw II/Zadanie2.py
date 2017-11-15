# Napisz funkcję w języku Python, która w oparciu o stos przekształca dane wyrażenie zapisane w nota-
# cji postfiksowej w wyrażenie zapisane w notacji infiksowej. Zakładamy, że korzystamy z 4 klasycznych
#
# operacji arytmetycznych +, -, * oraz /.
# Przykładowo dla danych wejściowych ”20 10 + 75 45 - * ” wynik powinien wynosić ”((20 + 10) * (75 -
# 45))”.
# Funkcję proszę nazwać Postfix to Infix().
from stack import Stack

def postfix_to_infix(postfix_word):
    stos = Stack()
    for li in postfix_word:
        if li.isdigit:
            stos.push(li)
        elif li in'+-/*':
            slowo2 = stos.top()
            stos.pop()
            slowo1 = stos.top()
            stos.pop()
            wynik= '('+slowo1+li+slowo2+')'
            stos.push(wynik)
    return stos.top()
print (postfix_to_infix('20 10 + 75 45-*'))
