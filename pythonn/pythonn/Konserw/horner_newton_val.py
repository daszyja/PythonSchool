def horner_newton(B, X, c, wynik=0):
    '''It returns the value of the Newton's polynomal, for example:
       a0 + a1(x - x0) + a2(x - x0)(x - x1) + a3(x - x0)(x - x1)(x - x2)
	a0 + E ai * II (x - xj)
       and so on'''
    for i in range(1, len(B)):
        wynikowy = 1
        for j in range(i):
            wynikowy *= c - X[j]
        wynikowy *= B[i]
        wynik += wynikowy
    return B[0] + wynik

X = [0, 1, 2]
B = [1, -5, 3, 2]
c = -2

print horner_newton(B, X, c)
