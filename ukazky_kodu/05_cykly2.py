import random

hod1 = random.randint(1, 6)
hod2 = random.randint(1, 6)

while hod1 != hod2:
    print(hod1, hod2)
    hod1 = hod2
    hod2 = random.randint(1, 6)

print("dvě stejná čísla:", hod1, hod2)    