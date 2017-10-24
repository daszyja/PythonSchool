from stos_tablica import Stack_01

def infix_to_postfix_for_digs(infix_word):
    stos=Stack_01()
    wyjscie=''
    for i in infix_word:
        if i.isalnum():
            wyjscie+=i
        elif i in '*/+-':
            stos.push(i)
        elif i == ')':
            wyjscie += stos.pop()
    return wyjscie

#print infix_to_postfix_for_digs('(((a+b)*c)-d)')

def compute_postfix_dig(man):
    stos=Stack_01()
    for n in man:
        if n.isdigit():
            stos.push(n)
        elif n in '/*-+':
            temp = stos.pop()
            if n == '*':
                stos.push(int(stos.pop()) * int(temp))
            elif n == '/':
                stos.push(int(stos.pop()) / int(temp))
            elif n == '-':
                stos.push(int(stos.pop()) - int(temp))
            else:
                stos.push(int(stos.pop()) + int(temp))
    return stos.pop()

#print compute_postfix_dig('23+23*+')


def compute_postfix(text):
    stos=Stack_01()
    tempdig = ''
    for c in text:
        if c.isdigit():
            tempdig += c
        elif c in '/*-+':
            temp = str(stos.pop())
            stos.push(eval(str(stos.pop())+c+temp))
        elif c == ' ' and tempdig != '':
            stos.push(tempdig)
            tempdig = ''
    return stos.pop()

# print compute_postfix('136 4 + 2 * 79 -')

def compute_postfix_real(text):
    #import pdb; pdb.set_trace()
    stos=Stack_01()
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

print compute_postfix_real('0.5 15 -5 - *')


def compute_postfix_real_2(text):
    #import pdb; pdb.set_trace()
    stos=Stack_01()
    tempdig = ''
    i = 0
    while i != len(text):
        c = text[i]
        cn = text[i +1] if i+1 < len(text) else ''
        if c.isdigit() or c == '.':
            tempdig += c
        elif c in '/*-+':

            if not cn.isdigit():
                temp = float(stos.pop())
                if c == '*':
                    stos.push(float(stos.pop()) * temp)
                elif c== '/':
                    stos.push(float(stos.pop()) / temp)
                elif c== '+':
                    stos.push(float(stos.pop()) + temp)
                else:
                    stos.push(float(stos.pop()) - temp)
            else:
                tempdig += c

        elif c == ' ' and tempdig != '':
            stos.push(tempdig)
            tempdig = ''
        i += 1
    return stos.pop()

print compute_postfix_real_2('0.5 15 -5 - *')
