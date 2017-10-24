from random import randint as RANDOM
import time

# tab = []
# for i in range(10 ** 6):
#     tab.append(RANDOM(-100, 100))
#
# print len(tab)

# start_time = time.time()
# insertion_sort(tab)
# print("--- %s seconds ---" % (time.time() - start_time))

'''Zadanie nr 3.'''


def insertion_sort(A, order):
    if order == 'ascending':
        return insertion_sort_ascending(A)
    elif order == 'descending':
        return insertion_sort_descending(A)
    else:
        return "[%s] is unknown order type, type: 'ascending' or 'descending'." % (inn)


def insertion_sort_ascending(A):
    for i in xrange(1, len(A)):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j - 1], A[j] = A[j], A[j - 1]
            j -= 1
    return A


def insertion_sort_descending(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j - 1] < A[j]:
            A[j - 1], A[j] = A[j], A[j - 1]
            j = j - 1
    return A

A = [1, 2, 3, 4, 5]
B = [1, 52, 3, -2, 77, 2, 7, 8, 9]
dsc = 'descending'
asc = 'ascending'
inn = 'chomik'
print insertion_sort(A, dsc)
