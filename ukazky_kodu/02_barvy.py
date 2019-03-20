stena_a = 4
print(stena_a)

vyska = 2.3
sirka_a = 4
sirka_b = 6
sirka_c = 3.5

okno = 1.5 * 1.5
dvere = 2 * 0.8

pokoj_a = 2 * sirka_b * vyska + 2 * sirka_a * vyska
pokoj_a = pokoj_a - dvere - 2 * okno

pokoj_b = 2 * sirka_a * vyska + 2 * sirka_c * vyska
pokoj_b = pokoj_b - okno - dvere

print("budeme potřebovat", pokoj_a + pokoj_b, "m barvy")

barva_doma = 70.55
barva_potreba = pokoj_a + pokoj_b