from stack import Stack

def dobre_nawiasowanie_ex(slowo):
    s = Stack()
    # import pdb
    # pdb.set_trace()
    k = 0
    for i in slowo:
        if i in 'ABCDEFGHIJKLHMNOPRSTUWXYZabcdefghijklmnoprstuwyxz':
            k += 1
        if i in '({[':
            s.push(i)
            k += 1

        elif i in '})]':
            if i == '}':
                if s.isEmpty() or s.top() != '{':
                    print  (k+1)
                    return False
                else:
                    s.pop()
            elif i == ')':
                if s.isEmpty() or s.top() != '(':
                    print (k+1)
                    return False
                else:
                    s.pop()
            else:
                if s.isEmpty() or s.top() != '[':
                    print (k+1)
                    return False
                else:
                    s.pop()
    if s.isEmpty():
        return True
    return False

print (dobre_nawiasowanie_ex('foo(bar[i)'))
