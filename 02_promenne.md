# Lekce 2 - proměnné

[![](http://img.youtube.com/vi/uzoLMv2brZk/0.jpg)](http://www.youtube.com/watch?v=uzoLMv2brZk "Lekce druhá")


Ahoj já jsem Jirka Vraný a tohle je seriál nauč se Python. Druhý díl bude o
proměnných.

Ať už váš program bude používat data velká, nebo docela malá, bude potřeba je
nějak uložit do paměti počítače, pak je v případě potřeby přečíst a nebo třeba
změnit. 

A právě k tomu se v programování používají proměnné. Tenhle termín možná znáte z
matematiky. Proměnné v programování mají ale trochu volnější definici a také
širší záběr. 

A máte docela štěstí na výběr jazyka - protože lehčí práce s proměnnými než v
Pythonu už to snad ani být nemůže.

Přestavte si, že potřebujete vymalovat pokoj. Než vyrazíte do prodejny barev,
musíte si spočítat jakou plochu mají stěny, které chcete vymalovat. 

No dobře, tak nemusíte, ale pak se vám může stát, že vám barva nevyjde, nebo
naopak zbude. Případně budete v krámě dělat "éééé..." až se vás prodavač zeptá kolik
toho potřebujete vymalovat.

Takže jdeme počítat. Obsah obdélníka vypočítáme vynásobením délek jeho stran. A
zatímco tenhle vzoreček bude pořád stejný, dokud bude geometrie geometrií, tak
délky stran jsou pokaždé jiné, nebo aspoň můžou být. Mění se - jsou to proměnné. 

Pojďme si to celé napsat jako jednoduchý program v Pythonu. Opět budeme
potřebovat editor a příkazovou řádku s aktivním virtuálním prostředním. 


Samozřejmě i bez proměnných můžeme nějak dojít k výsledku. Prostě ta čísla
zadáme přímo do funkce print. Jak už víme, funkce může mít několik parametrů,
které od sebe oddělíme čárkou. Takže napíšeme:

```
print(“na stěnu bude potřeba”, 2,3 * 4, “m2 barvy”).
``` 

Uložíme a spustíme. Tak a už víme, že na tu první stěnu je potřeba 9.2 m2 barvy. 

Jenže stěny máme v každé místnosti čtyři, nějaká ta okna a dveře se také najdou.
Také je vidět, že se nám některé rozměry opakují.  Co s tím dál?

Můžeme změnit čísla a program znovu spustit - ale tím přijdeme o předchozí
výsledek. No ale přece si ho nebudeme opisovat na papír, že?  

Tak co přidat další print a vypočítat postupně všechny čtyři stěny? Pak
vypočítat velikost oken, dveří a nějak to od sebe odečíst na dalším řádku funkce
print.

A pak půjdeme do druhé místnosti, která má sice dvě stěny jiné, ale dvě jsou
stejné a dveře a okna jsou taky stejné. Nějak se s tím popereme, ale nakonec se
ukáže, že nám pes překousnul metr a všechny rozměry máme špatně a musíme to
přepsat..

Tak pojďme k tomu co máme probrat - co a k čemu jsou proměnné a jak nám můžou
pomoci s řečením našeho problému.

Prozatím stačí, když si budete pamatovat, že pomocí proměnných můžete ukládat
data do paměti počítače a pak si je z ní zase vyzvednout. Je to podobné jako
paměť na kalkulačce - jen o dost lepší.

Pokud chcete použít nějakou proměnnou, tak prostě napíšete její jméno, pak
mezeru, rovná se a pak hodnotu, kterou ta proměnná bude mít. A to je všechno. 

Když pak někde dál v programu použijete to jméno, Python se postará o to, aby se
na tam místě použila hodnota, která je pod ním uložena. 

Tomuhle zápisu říkáme přiřazení - jménu na levé straně přiřazujeme hodnotu na
pravé straně rovnítka. A nebo naopak hodnotě na pravé straně dáváme pro tuto
chvíli jméno na levé straně výrazu. 

Pojďme tedy náš program přepsat. Máme tu vlastně jen 3 různé délky stěn, výška
je ve všech místnostech stejná a to platí i pro okna a dveře. Máme tedy 5
základních proměnných.

V Pythonu platí konvence, že jména proměnných se píší vždy malými písmeny
anglické abecedy. Takže na háčky a čárky také raději zapomeňte. 

V optimálním případě by pak jméno proměnné mělo naznačovat její obsah. V
proměnných s krátkými jmény typu a b c se člověk rychle ztratí. Pokud chceme
použít více slov, oddělíme je podtržítkem. Mezera by nefungovala - název
proměnné musí být jedno slovo. 

Takže napíšeme `stena_a = 4`. Když to uložíme a spustíme, program do paměti zapíše
hodnotu 4. Ale na obrazovku samozřejmě nevypíše nic. 

Hodnotu proměnné ale můžeme předat funkci print jako parametr. Řádek
`print(stena_a)` nám na obrazovku vypíše hodnotu. V tomhle případě 4.

Tím se nám poprvé ten název přesunul z levé strany výrazu někam jinam a Python
se při volání funkce print postaral o doplnění hodnoty.

Výška stěny je ve všech místnostech stejné - 2 metry 30.  

Šířky jednotlivých stěn jsou čtyři, šest a tři a půl metru. 

Každou hodnotu si uložíme do nové proměnné.

Okna a dveře jsou také ve všech místnostech stejná - okno má 1.5 x 1.5 m a dveře
2 x 0.8. 

Když se nad tím trochu zamyslíme, nepotřebujeme vlastně ani tak znát plochu
jednotlivých stěn. Ve výsledku chceme vědět, kolik barvy máme koupit. Takže
můžeme vypočítat rovnou spotřebu barvy pro jednu místnost.

Pojďme spočítat první pokoj. Všechny stěny můžeme zapsat do jednoho výrazu. 

Proměnná pro výsledek se bude jmenovat `pokoj_a`.

```
pokoj_a = 2 * sirka_b * vyska + 2 * sirka_a * vyska. 
```

Dobrá zpráva je, že si nemusíme moc lámat hlavu s prioritou operací - Python to
řeší automaticky a samozřejmě správně. 

Nejdříve provede násobení a potom hodnoty sečte. Stejně jako v předchozím
případě u funkce print i tady na pravou stranu doplní hodnoty všech proměnných. 

Teď bychom si zase mohli hodnotu výsledku vypsat, ale počkejme s tím, ještě to
není hotové.  Pokoj má přece 2 okna a jedny dveře. A ty malovat nechceme.

Takže jejich plochu od výsledku můžeme odečíst. Zápisem 

```
pokoj_a = pokoj_a - dvere - 2 x okno 
```

říkáme doslova - vezmi původní hodnotu pokoj_a od ní odečetl hodnotu dvere a 2x
okno a výsledek ulož pod znovu pod jméno pokoj_a. 

U druhého pokoje budeme postupovat stejně, nejdřív vypočítáme základní plochu.
Takže nová proměnná 

```
pokoj_b bude mít hodnotu 2 * sirka_a * vyska + 2 * sirka_c * vyska. 
```

Druhý pokoj má jen jedno okno a jedny dveře - a ty znovu odečteme. 

```
pokoj_b = pokoj_b - okno - dvere.
```

A teď  už můžeme výsledek vypsat - print(budemepotrebovat, pokoja + pokojb, m2
barvy). 

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

```

Uložíme, spustíme a můžeme vyrazit nakupovat...

Ještě poslední věc, ale docela důležitá. Jak je vidět, můžeme proměnné mezi
sebou sčítat, násobit a tak dále. Dost často pak potřebujeme mezi sebou dvě
hodnoty také porovnat. 

Který z našich pokojů má větší plochu stěn? První nebo druhý? 

Python umí pomocí operátorů porovnat, jestli je první hodnota větší než druhá a
nebo jestli jsou stejné. Umí také vybrat z nějaké posloupnosti hodnot tu
největší, ale o tom až příště. 

Porovnání se zapisuje stejně jako v matematice pomocí symbolů < > případně <= a
\>=. Jediný rozdíl je v operátoru pro rovnost - používáme dvojité == 

Jedno rovná se je totiž vyhrazené pro přiřazení.

Výsledkem tohoto porovnání je buď pravda - **True** nebo nepravda **False**. Pozor na to
velké písmenko na začátku. S malým písmenkem to nebude fungovat - Python bude
hledat proměnnou se jménem true, která ale neexistuje.

Operaci porovnání používáme pokud potřebujeme, aby se náš program naučil
reagovat na situace typu když je a větší než b udělej tohle a když není, tak
udělej něco jiného. A o tom si povíme příště. Teď jdeme pro ty barvy…
