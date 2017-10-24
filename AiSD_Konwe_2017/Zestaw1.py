'''Algorytmy i struktury danych - Zestaw 1 semestr zimowy 2017/2018 - Zestaw 1'''

'''Zadanie 1'''
def HornerNewton(B,X,c):
    iloczyn = 1
    wynik = B[0]
    for i in range(1,len(B)):
        iloczyn *= B[i] c-X[i-1]
        wynik += B[i] * iloczyn
    return wynik
#print (HornerNewton([1,-5,3,2],[0,1,2],-2))


'''Zadanie 2'''

def HornerPochodne(n,A,c):
    for j in range(n-1.-1,-1):
        for i in range(j,-1,-1):
            A[I] = A[i+1] * c + A[i]
        print (A[1:], A[0])
        A = A[1:]

# A = [1, -2, -5, 7]
# n = len(A) - 1
# c = -1
# HornerPochodne(n, A, c)

def HornerPochodneRek(n,A,c):
    if n == 0:
        pass
    else:
        for i in range(0,n):
            if i == 0:
                pass
            else:
                A[i] = A[i-1] * c +A[i]
        print (A[:n], A[n])
        return HornerPochodneRek(n-1,A[:n],c)
# A = [1, -2, -5, 7]
# n = len(A) - 1
# c = -1
# HornerPochodneRek(n, A, c)

'''Zadanie 3'''

def HornerPochodneIteracja(n,A,c):
    while n != 0:
        for i in range(0,n):
            if i !=0:
                A[i] = A[i-1] * c + A[i]
    n -=1


def HornerPochodneRekurencja(n,A,c):
    if n != 0:
        for i in range(0,n):
            if i !=0:
                A[i] = A[i-1] * c + A[i]
        return HornerPochodneRekurencja(n-1,A[:n],c)
