import math
import random

#sortowanie - operacja scalania
def merge(L,start, center,finish):
"""Operacja scalania"""
i = start
j = center + 1

L2 = [] #lista pomocnicza
 
#wybieraj odpowiednie elementy z dwoch tablic
while (i <= center) and (j <= finish):
if L[j] < L[i]:
L2.append(L[j])
j = j + 1
else:
L2.append(L[i])
i = i + 1

#jedna z tablic skonczyla sie przepisz reszte z pozostalej
if i <= center:
while i <= center:
L2.append(L[i])
i = i + 1
else:
while j <= finish:
L2.append(L[j])
j = j + 1

#przepisz wyniki z tablicy tymczasowej
s = finish - start + 1
i = 0
while i < s:
L[start + i] = L2[i]
i = i + 1

return L

#sortowanie przez scalanie
def merge_sort(L, start, finish):
"""sortowanie merge sort"""
if start != finish:

#dzielimy dablice do konca
center = int(math.floor((start + finish)/2))
#na lewo
merge_sort(L, start, center)
#na prawo
merge_sort(L,center+1,finish)

#operacja scalania
merge(L,start, center,finish)
return L

#generuje dane wejsciowe w porzadku malejacym
def malejaco(n):
L = []
for i in range(0,n):
L.append(n-i-1)
return L

#generuje dane wejsciowe w porzadku losowym
def losowe(n):
L = []
a = range(0,n)
for i in range(0,n):
L.append(random.choice(a))
return L

#przyklad uzycia
n = input('Podaj ilosc danych: ')
w = input('Dane wjsciowe: Losowo/Malejaco [1/2]: ')

if int(w) == 1:
L = losowe(int(n))
print(L)
elif int(w) == 2:
L = malejaco(int(n))
print(L)
else:
print('napisales bzdure')

L = merge_sort(L,0,len(L)-1)

print('Po posortowaniu:')
print(L)
