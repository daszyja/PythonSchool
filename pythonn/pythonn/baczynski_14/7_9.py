import stos_tablica
def postfix_to_infix(postfix_word):
    Stos = stos_tablica.Stack_01
    for li in postfix_word:
        if li>='0' and li<='9':
            print li
            stos.push(li)
        elif li in'+-/*':
            print li
            slowo2 = stos.top()
            print slowo2
            stos.pop()
            print stos, "aa"
            slowo1 = stos.top()
            stos.pop()
            wynik= '('+slowo1+li+slowo2+')'
            stos.push(wynik)
    return stos.top()



def infix_to_postfix(infix_word):
    Stos = stos_tablica.stack
    stos =Stos()

    wyjscie=''
    for i in infix_word:
        if i in '(':
            stos.push(i)
        elif i ==')':
            while (stos.top() != '(') :
                wyjscie+=stos.top()
                stos.pop()
            stos.pop()
        wyjscie+=stos.top()
        stos.pop()
    return wyjscie

tekst = "((((1 + 7) * 3) + ((5 + 6) * 4)) * 2)"
print infix_to_postfix(tekst)
