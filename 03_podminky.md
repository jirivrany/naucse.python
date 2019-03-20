# Lekce 3 - rozhodování

[![](http://img.youtube.com/vi/uYstFl621WE/0.jpg)](http://www.youtube.com/watch?v=uYstFl621WE "Lekce druhá")


Ve třetím díle se podíváme na rozhodování. 

V životě se rozhodujeme prakticky pořád. Často nevědomě - mozek to dělá tak
nějak sám. Ale zkuste se zamyslet nad tím z kolika rozhodovacích kroků se skládá
jedno větší rozhodnutí - třeba kudy na křižovatce dál. 

Není jich zrovna málo co? No a taky málokterý reálný problém se dá vyřešit bez
nějakého toho rozhodování. A protože chceme dělat programy, které řeší reálné
problémy, musíme se naučit ta rozhodovací pravidla napsat. 

Většina rozhodnutí se dělá na základně vyhodnocení nějaké podmínky či otázky.
Například na té křižovatce to může být: vidím nějakou dopravní značku? Je to
směrová šipka? Je na ní text? A tak dále.

Proto se taky o rozhodování v programu často mluví a píše jako o podmínkách. No
a když už si nějakou tu cestu vybereme, pokračujeme po ní dál, auto za námi se
klidně může vydat tou druhou. Naše cesty se rozdělí - neboli rozvětví. 

Ale ať už se mluví o podmínkách, větvení programu či rozhodování je to pořád
jedno a totéž. A taky se to skoro ve všech programovacích jazycích zapisuje
stejně. Klíčové slovo pro podmínku je anglické **if**. 

Vraťme se k našemu příkladu s malováním. Dejme tomu, že už máme nějakou tu barvu
doma a chceme vědět, jestli nám bude stačit nebo ne. Samozřejmě, že náš mozek
nám dá správnou odpověď ještě dřív, než začneme psát první řádek nového kódu.
Ale aspoň budeme mít jistotu, že náš program funguje správně. 

Vytvoříme si novou proměnnou barva_doma a také výsledek předchozího počítání
uložíme do nové proměnné barva_potreba, místo toho, abychom ho hned vypsali. 

Obě proměnné nyní můžeme porovnat tímto zápisem `if barva_doma > barva_potreba`

Za if píšeme samotnou podmínku - rozhodovací výraz. Python za nás vyhodnotí a
určí, jestli je podmínka splněná - tedy True či ne - tedy False. Nemusíme se ale
omezovat pouze na tyto dvě logické hodnoty, Python vyhodnotí jako True i řadu
jiných hodnot - třeba nenulové číslo, neprázdný řetězec a další.

Jakmile napíšeme na konec řádku dvojtečku, ukončíme tím rozhodovací výraz. A
následující řádek musíme odsadit o čtyři mezery doprava. 

Dobré je, že většina editorů, které podporují Python je umí napsat po jednom
zmáčknutí tabelátoru a Atom samozřejmě taky. 

Proč musíme? Protože za podmínkou bude následovat kus programu, který se provede
jen a jen tehdy, když je podmínka splněná. No a v Pythonu se tenhle kus programu
vyznačí právě pomocí toho odsazení. Je to rychlé, přehledné a nepotřebujeme k
tomu žádné další speciální znaky. No a místo kus programu většinou říkejte
raději blok kódu - zní to víc odborně. 

Blok kódu může být libovolně dlouhý a může obsahovat i další vnořené bloky. Ale
v tomhle případě si vystačíme s jedním printem - když je podmínka splněná,
vypíšeme “barva doma bude stačit”. 

```python

barva_doma = 70.55
barva_potreba = pokoj_a + pokoj_b

if barva_doma == barva_potreba:
    print("barva doma nám bude přesně stačit")
```

Uložíme a spustíme program. 

A víme co už jsme věděli, barva nám v tomhle případě vystačí. 

Ale co když jí máme doma méně? 

Upravíme, uložíme a spustíme.  A program nevypíše nic…

Musíme ho naučit, co má dělat pokud podmínka splněná není. K tomu slouží další
anglické slovíčko **else**. 

Ukončíme blok splněné podmínky, prostě a jednoduše se s odsazením vrátíme zase
na původní hodnotu - o čtyři mezery zpět. 

Na nový řádek napíšeme `else:`  A to je všechno, podmínka tu není potřeba, můžeme
hned pokračovat na dalším řádku novým blokem. Odsadíme o čtyři mezery a pomocí
funkce print vypíšeme, že nám to stačit nebude. 

Příkaz if else nám stačí na jednoduchá rozhodnutí typu ano/ne. Ale dost často si
s tím nevystačíme. Potřebujeme ještě třetí větev, nebo třeba i čtvrtou či
padesátou. 

Tyhle další větve zapisujeme jednoduše tak, že za slovo ELSE dáme znovu IF a
zařadíme další podmínku. V Pythonu je ale zápis ještě trochu kratší a používá se
tu slovo **elif**. 

Takže co kdybychom přidali variantu, kdy máme přesně tolik barvy, kolik bude
potřeba. 

Pozor na to, že blok **elif** nemůžeme dát na konec toho co teď máme, tedy až za
příkaz **else**. Pořadí je vždy **if … elif … else**. Nový řádek s podmínkou bude tedy
nad blokem **else**. 

Napíšu `elif ==` a opět blok s výpisem print. 

No a máme za sebou další ze základních kamenů každého programu - rozhodování. V
rámci procvičování s můžete vyzkoušet, co všechno jde napsat do té podmínky -
tedy mezi if a dvojtečku. 

V programu za sebou můžete zařadit libovolný počet takových to rozhodnutí. A
můžete je do sebe také vnořit, jak už jsme si řekli. Náš příklad tedy na ukázku
můžeme přepsat třeba takhle.

Nejprve určíme, zda máme doma přesné množství barvy, podmínka s rovností se tedy
přesune nahoru. 

V else větvi - tedy v situaci kdy barvy není přesné množství pak provedeme test,
zda jí máme málo nebo moc. 

```python
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

if barva_doma == barva_potreba:
    print("barva doma nám bude přesně stačit")
else:
    if barva_doma > barva_potreba:
        print("barva doma bude stačit a ještě zbyde")
    else:
        print("barva stačit nebude")

```

Naposledy uložíme a spustíme. Je vidět, že i tenhle kód pracuje stejně jako ten
předchozí. Jsou situace, kdy se tenhle vnořený zápis hodí víc, třeba proto že
první situace nastává nejčastěji a není tak potřeba testovat další podmínky. Ale
to už opravdu záleží na konkrétním problému.

Teď už umíte nechat program rozhodovat kterou cestou se vydá. A příště si
ukážeme, jak ho donutit aby stejnou cestou chodil opakovaně - neboli v cyklu. 

Ale ještě chvilku o podmínkách. Zatím jsme si vystačili s tím, že v rozhodovacím
výrazu byla jen jedna operace. Tedy podmínka typu když platí A udělej tohle.
Někdy ale potřebujeme napsat podmínku ve stylu když platí A a zároveň B.
Případně - když platí A a nebo B. A tak je čas povolat na scénu logické
operátory. Ukážeme si tři nejzákladnější. 

Dva už jsme si vlastně představili, jen to bylo česky. Stačí tedy použít
anglická slovíčka **and** pro “a zároveň” a **or** pro “nebo”. Poslední člen do party je
**not** - česky ne, přesněji řečeno negace. 

Ukážeme si to na jednoduchém příkladu. V něm použijeme ještě operátor **%**, který
slouží pro takzvané modulo dělení. Nemusíte se bát, protože to není nic
složitého - je to zkrátka a dobře zbytek při celočíselném dělení. 5 modulo 2 je
1, 6 modulo 2 je nula a tak dále. 

Za pomoci operátoru modulo vytvoříme program, který nám vypíše, jestli je číslo
dělitelné 2 a zároveň třemi. Odpověď vypíšeme pomocí funkce print, kterou už
dobře známe. No a pro zadání čísla použijeme novou funkci - input. 

Když napíšete do programu `vstup = input(“zadej libovolné celé číslo”)` interpret
Pythonu se při provádění programu na tomhle řádku zastaví, vypíše text předaný
jako parametr a pak bude čekat dokud mu na klávesnici nezadáme číslo a
nezmáčkneme enter. 

Jakmile se to stane, uloží vše co jsme napsali do proměnné vstup. 

Pro kontrolu si to necháme ještě vypsat pomocí print(vstup) 

```python
vstup = input("zadej libovolné celé číslo: ")
print(vstup)
```

Uložíme

A spustíme

Samotné testování zařídí opět klíčové slovo if za které napíšeme vstup % 2 == 0
and vstup % 3 == 0.

V bloku podmínky if vypíšeme něco jako print(“číslo”, vstup, “je dělitelné 2 a
zároveň 3”). Tím se nám zadané číslo vypíše pěkně uprostřed věty.

No a můžeme pokračovat třeba testem pro číslo dělitelné pouze třemi ale ne
dvěma. 

Takže elif - tady si okopírujeme předchozí podmínku a upravíme jediný znak. U
vstup % 2 změníme == na != - ten vykřičník se čte jako negace, takže doslova
nerovná se. 

I ten print si pro rychlost okopírujeme a jen trochu upravíme - (“číslo”, vstup,
“je dělitelné 3 ale ne 2”)

No a takhle bychom mohli pokračovat dál a napsat si třeba test pro číslo
dělitelné 2 ale ne 3. Nebo nějaké úplně jiné hodnoty. 

Samozřejmě to že čekáme číslo program zatím nijak nehlídá, to bychom po něm pro
začátek trochu moc. Takže když do něj zkusíte zadat třeba nějaké slovo, program
skončí chybou. Můžete si to zkusit. Nebojte se v tom trochu povrtat - tím se
naučíte nejvíc. 


```python
vstup = input("zadej libovolné celé číslo: ")
print(vstup)

if vstup % 2 == 0 and vstup % 3 == 0:
    print("číslo", vstup, "je dělitelné dvěma a zároveň třemi")
elif vstup % 2 != 0 and vstup % 3 == 0:
    print("číslo", vstup, "je dělitelné třemi ale ne dvěma")

```

Ale pozor, pokud teď zastavíte video a začnete tenhle program zkoušet, skončí
chybou i pokud správně zadáte číslo. Zbývá nám poslední věc k tomu, aby program
dělal co má.

My jsme si toho zatím o datových typech moc neřekli. Prostě nějak používáme
čísla - dáváme je do proměnných, do podmínek. Ve funkci print pak umíme použít i
text. V některém z příštích dílů si o tom povíme víc.

Teď prostě trochu předběhnu - funkce input vrátí do proměnné vstup text. Jenže s
tím si neporadí matematické operátory v podmínce. Takže musíme ten text převést
na celé číslo a to pomocí funkce int.

Napíšeme vstup = int(vstup)

```python
vstup = input("zadej libovolné celé číslo: ")
print(vstup)

vstup = int(vstup)

if vstup % 2 == 0 and vstup % 3 == 0:
    print("číslo", vstup, "je dělitelné dvěma a zároveň třemi")
elif vstup % 2 != 0 and vstup % 3 == 0:
    print("číslo", vstup, "je dělitelné třemi ale ne dvěma")

```
Teď už můžeme program spustit a na vstupu zadat třeba 12. 

Teď už všechno funguje jak má a můžete se pustit do vlastních pokusů.