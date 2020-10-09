"""
Bonusový kód - ve videu není
Takto bychom mohli vyřešit simulaci bez použití range()
"""

import random

celkovy_pocet = 0
pocet_kroku = 8000000
krok = 0

while krok < pocet_kroku:

    hod1 = random.randint(1, 6)
    hod2 = random.randint(1, 6)

    pocet_hodu = 0
    while hod1 != hod2:
        hod1 = hod2
        hod2 = random.randint(1, 6)
        pocet_hodu += 1

    celkovy_pocet += pocet_hodu
    krok += 1
    
print("cp", celkovy_pocet)
print("avg", celkovy_pocet / pocet_kroku)