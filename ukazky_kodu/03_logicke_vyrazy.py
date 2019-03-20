vstup = input("zadej libovolné celé číslo: ")
print(vstup)

vstup = int(vstup)

if vstup % 2 == 0 and vstup % 3 == 0:
    print("číslo", vstup, "je dělitelné dvěma a zároveň třemi")
elif vstup % 2 != 0 and vstup % 3 == 0:
    print("číslo", vstup, "je dělitelné třemi ale ne dvěma")
