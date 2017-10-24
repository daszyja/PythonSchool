# -*- coding: utf-8 -*-
# Przykład zastosowania struktury stosów do sprawdzenia poprawności wyrażenia nawiasowego

import stos_tablica
#importuje plik z naszą klasa

stos = stos_tablica.Stack_01
# dla ulatienia odwołania się do naszego stosu tworzymy alias

def nawiasy_spr(symbol_string):
    """Program sprawdzajacy poprawnosc prostego wyrazenia nawiasowego"""
    s = stos()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


# poniżej przykładowe wywołania

print(nawiasy_spr('((()))'))
print(nawiasy_spr('(()'))
