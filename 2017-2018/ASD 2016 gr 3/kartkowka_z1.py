# coding: utf-8
'''
1). Napisać MergeSort3(), która dzieli listę na 3 części, rekurencyjnie sortuje, a następnie scala.
* Porównać czasy działania tej funkcji oraz Państwa funkcji z ostatniej pracy domowej dla listy złożonej z 10000 elementów.



zalozenie ze n = 3^k
'''

def merge_sort(tab):
    n = len(tab)
    if(n > 1):
        tl = merge_sort(tab[:n // 3])
        tm = merge_sort(tab[n // 3:(n // 3)*2])
        tr = merge_sort(tab[(n // 3)*2:])
        i, j, k = 0, 0, 0

        while i < len(tl) and j < len(tm) and k < len(tr):
            if tl[i] < tm[j] and tl[i] < tr[k]:
                tab[i + j + k] = tl[i]
                i += 1
            elif  tm[j] < tl[i] and tm[j] < tr[k]:
                tab[i + j + k] = tm[j]
                j += 1
            else:
                tab[i + j + k] = tr[k]
                k += 1
        while i < len(tl):
            tab[i + j + k] = tl[i]
            i += 1
        while j < len(tm):
            tab[i + j + k] = tm[j]
            j += 1
        while k < len(tr):
            tab[i + j + k] = tr[k]
            k += 1
        return tab
    return tab

def merge_sort_2(tab):
    n = len(tab)
    if(n > 1):
        tl = merge_sort(tab[:n // 2])
        tr = merge_sort(tab[n // 2:])
        i, j = 0, 0
        while i < len(tl) and j < len(tr):
            if tl[i] < tr[j]:
                tab[i + j] = tl[i]
                i += 1
            else:
                tab[i + j] = tr[j]
                j += 1
        while i < len(tl):
            tab[i + j] = tl[i]
            i += 1
        while j < len(tr):
            tab[i + j] = tr[j]
            j += 1
        return tab
    return tab


    '''

    porownanie dla 729 bialek (9^3)
    '''

# f = open("Bialka.txt")
# lines = f.readlines()
#
# import time
# ts = time.time()
#
# for i in range(10000):
#     lines_sorted = merge_sort(lines)
#
# print 'mergesort3', time.time()-ts
#
#
# import time
# ts = time.time()
#
# for i in range(10000):
#     lines_sorted = merge_sort_2(lines)
#
# print 'mergesort2', time.time()-ts
