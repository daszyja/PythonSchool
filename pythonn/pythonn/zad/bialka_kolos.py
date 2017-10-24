#dla mnie execution time wynosi: ..... 

def digs_count(digs1, digs2, counter1=0, counter2=0):
    for j in digs1:   # for j in digs1 .... chyba by wystarczylo...
        # korzystamy z gotowej funkcji pythona rownie dobrze mozemy sprawdzac
        # to: if digs1[i]=="0" or digs1[i]=="1" or digs1[i]=="2" or
        # digs1[i]=="3" or digs1[i]=="4" etc.... tylko po co? - wtedy muesielibysmy robic range(len(digs))
        if j.isdigit() is True:
            j = int(j)
            counter1 += j  # sumujemy sobie ;)
    for j in digs2:
        if j.isdigit() is True:
            j = int(j)  # zamieniamy string na int... gdyz a != 'a' :D
            counter2 += j  # suma
    if counter1 > counter2:
        return 1  # True
    else:
        return -1  # False



plik = open("bialka11.txt")
filelist = []

with open("bialka1.txt") as plik:
    for text in plik:
        text = text.rstrip('\n')
        filelist.append(text)

sorted_file = sorted(filelist, cmp=digs_count)
plik = open("bialka_sorted.txt", 'w')
plik.write('\n'.join(sorted_file) + '\n')
plik.close()
