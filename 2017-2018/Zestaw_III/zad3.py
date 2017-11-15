def nwd_rek(liczba1,liczba2):
    if liczba1 and liczba2 > 0:
        if liczba1 > liczba2:
            return nwd_rek(liczba1 - liczba2,liczba2)
        elif liczba2 > liczba1:
            return nwd_rek(liczba2 - liczba1,liczba1)
        else:
            return liczba1
    else:
        return "Podaj liczbe wieksza od 0 !"

print(nwd_rek(36,0))
