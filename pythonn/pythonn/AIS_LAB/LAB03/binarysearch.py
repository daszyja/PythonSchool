1	def binarySearch(alist, item):
2	    first = 0
3	    last = len(alist)-1
4	    found = False
5
6	    while first<=last and not found:
7	        midpoint = (first + last)//2
8	        if alist[midpoint] == item:
9	            found = True
10	        else:
11	            if item < alist[midpoint]:
12	                last = midpoint-1
13	            else:
14	                first = midpoint+1
15
16	    return found


plik = open('Bialka.txt')
text = plik.read()
tablicaplik=[]
j=0
plik.close()
for i in range(0,len(text)):
    if text[i]=="\n":
        tablicaplik.append(text[j:i+1])
        j=i+1
listaPosortowana = sorted(list)
plik = open('plik', 'w')
plik.writelines(listaPosortowana)``
plik.close()
