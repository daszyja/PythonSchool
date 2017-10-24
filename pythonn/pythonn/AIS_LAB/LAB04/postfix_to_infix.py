from stos_tablica import Stack_01
def postfix_to_infix1(word):
    stos=Stack_01()
    wynik = ''
    for i in word:
        if i.isdigit():
            stos.push(i)
        else:
            wynik += stos.pop()
            stos.push('(',str(wynik)+i+stos.pop(),')')
    return stos.pop()




def postfix_to_infix(postfix_word):
    stos=Stack_01()
    for li in postfix_word:
        if li.isdigit:
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
print postfix_to_infix1('2010+7545-*')
