def insertion_sort(A, order):
    if order == 'ascending':
        return insertion_sort_ascending(A)
    elif order == 'descending':
        return insertion_sort_descending(A)
    else:
        return "[%s] is unknown order type, type: 'ascending' or 'descending'." % (inn)


def insertion_sort_ascending(A):
    for i in xrange(1, len(A) - 1):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j], A[j - 1] = A[j - 1], A[j]
            i = j - 1
    return A


def insertion_sort_descending(A):
    for i in xrange(1, len(A)):
        if A[i] > A[i - 1]:
            temp = array[i - 1]
            for j in range(i - 1, 0)
for i = 1 to length - 1
    if array[i] > array[i - 1]
        var temp < -- array[i]
        for j = i - 1 to 0 AND temp > array[j]
            array[j + 1] = array[j]
        array[j] < -- temp
