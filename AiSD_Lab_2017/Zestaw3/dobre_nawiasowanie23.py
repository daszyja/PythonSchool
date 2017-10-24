''''Zadanie 2 i 3'''

from stack import Stack


def dobre_nawiasowanie(slowo):
    s = Stack()
    for i in slowo:
        if i == '(':
            s.push(i)
        elif i == ')':
            if s.isEmpty() or s.top() == ')':
                return False
            if s.top() == '(':
                s.pop()

    if s.isEmpty():
        return True
    return False


# print dobre_nawiasowanie("(fdsad(())())))")

def dobre_nawiasowanie_ex(slowo):
    s = Stack()
    import pdb
    pdb.set_trace()
    for i in slowo:
        if i in '({[':
            s.push(i)

        elif i in '})]':
            if i == '}':
                if s.isEmpty() or s.top() != '{':
                    return False
                else:
                    s.pop()
            elif i == ')':
                if s.isEmpty() or s.top() != '(':
                    return False
                else:
                    s.pop()
            else:
                if s.isEmpty() or s.top() != '[':
                    return False
                else:
                    s.pop()
    if s.isEmpty():
        return True
    return False

print dobre_nawiasowanie_ex('[({})]')
