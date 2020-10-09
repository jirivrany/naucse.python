pokusy = 3,1,2,3,1,3,2,9

soucet = 0
pocet = 0

for cislo in pokusy:
    soucet = soucet + cislo
    pocet = pocet + 1

prumer = soucet / pocet
print('průměrný počet hodů:', prumer)    