def ktoreslowo(s1,s2):
    ile1=0
    for i in range(len(s1)):
        if s1[i]=="0" or s1[i]=="1" or s1[i]=="2" or s1[i]=="3" or s1[i]=="4" or s1[i]=="5" or s1[i]=="6" or s1[i]=="7" or s1[i]=="8" or s1[i]=="9":
            ile1+=int(s1[i])
    ile2=0
    for i in range(len(s2)):
        if s2[i]=="0" or s2[i]=="1" or s2[i]=="2" or s2[i]=="3" or s2[i]=="4" or s2[i]=="5" or s2[i]=="6" or s2[i]=="7" or s2[i]=="8" or s2[i]=="9":
            ile2+=int(s2[i])
    if ile1>ile2:
        return 1
    else: return -1


plik = open('Bialka.txt')
text = plik.read()
tablicaplik=[]
j=0
plik.close()
for i in range(0,len(text)):
    if text[i]=="\n":
        tablicaplik.append(text[j:i+1])
        j=i+1
listaPosortowana = sorted(tablicaplik,cmp=ktoreslowo)
plik = open('plik', 'w')
plik.writelines(listaPosortowana)
plik.close()
