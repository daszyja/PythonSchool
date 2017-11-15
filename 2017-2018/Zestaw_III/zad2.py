def binary_search_rek(lista, element, start=0, end=None):
    if end is None:
        end = len(lista) - 1
    if start > end:
        return False

    mid = (start + end) // 2
    if element == lista[mid]:
        return mid
    if element < lista[mid]:
        return binary_search_rek(lista, element, start, mid-1)
    # element > lista[mid]
#    return binary_search_rek(lista, element, mid+1, end)
