def RevList(lista):
    if len(lista) == 1:
        return lista

    else:
        return RevList(lista[1:]) + [lista[0]]


print (RevList([1,2,3,4,5]))
