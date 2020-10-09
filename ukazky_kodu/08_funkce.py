def secti(a, b):
    return a + b

#vysledek = secti(5, 5, 5)
#print(vysledek)


def vetsi(a, b):
    """
    funkce vrátí větší z čísel a, b
    """
    if a > b:
        return a
    else:
        return b

print(vetsi(5, 10))
print(vetsi(5, 3))        

