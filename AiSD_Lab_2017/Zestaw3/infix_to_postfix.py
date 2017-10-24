from stack import Stack

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
