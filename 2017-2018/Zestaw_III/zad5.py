def piramida(level):
    if level > 0:
        print (level * '*')
        piramida(level-1)

piramida(10)
