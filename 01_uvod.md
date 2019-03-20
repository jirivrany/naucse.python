# Nauč se Python - Lekce 1

[![](http://img.youtube.com/vi/DCBn5JHiviI/0.jpg)](http://www.youtube.com/watch?v=DCBn5JHiviI "Lekce první")


Ahoj, já jsem Jirka Vraný a tohle je seriál Nauč se Python. A pokud se chcete naučit programovat v tomto jazyce, poslouchejte dál.

Abychom se mohli pustit do práce, budete potřebovat minimálně dvě věci. Interpret jazyka Python a textový editor. 

Interpret vám umožní spoušet si programy, které vytvoříte. Samotná instalace není složitá, ale liší se systém od systému. Na našich stránkách naucse.python.cz najdete detailní popis jak postupovat při instalaci právě v tom vašem. I to, jak si pak aktivovat virtuální prostředí pro vývoj.  

Textový editor by měl podporovat jazyk Python. A když říkám podporovat, tak tím myslím, že takový editor umí od sebe barevně odlišit jednotlivé části programu. Říkáme tomu zvýrazňování syntaxe.  

Já budu ve svých ukázkách používat textový editor Atom, který si můžete zcela zdarma stáhnout ze stránek atom.io.  

Otestovat, zda máte správně nainstalovaný  interpret je docela snadné. Stačí, když do příkazové řádky napíšete příkaz python. Pokud je všechno v pořádku, interpret se spustí, v takzvaném interaktivním režimu. Krom jiných informací vám při startu vypíše s jakou verzí Pythonu pracujete. 

'''
$: python
'''

Interaktivní režim můžete používat pro zkoušení krátkých kódů, jako rychlou nápovědu nebo třeba jako kalkulačku. Pro psaní delších programů se ovšem moc nehodí. Většinu programů si totiž chceme uložit a používat je opakovaně. No a uložit výsledek vaší práce v interaktivním režimu není zrovna jednoduché. 

Tradice velí, že každý správný kurz programování začíná programem, který pozdraví uživatele výpisem na obrazovku. V anglickém prostředí to je obvykle Hello World, česky třeba Ahoj Světe. Než se s interaktivním režimem rozloučíme, ukážeme si jak těžké je napsat takový program v Pythonu.

No, doufám, že mi dáte za pravdu, ale moc těžké to není. Postačí nám k tomu totiž jedna jediná funkce - jmenuje se print. Program ahoj světe tvoří v Pythonu právě jeden příkaz - print(“ahoj světe”). V interaktivním režimu ho stačí zapsat, odeslat a je to - první program je hotový. Ani to nebolelo že?

'''
Python 3.6.8 |Anaconda custom (64-bit)| (default, Dec 30 2018, 01:22:34) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("ahoj světe")
ahoj světe
>>> 
'''

Nicméně, pokud bychom chtěli tento program někomu poslat, nebo třeba prodat, musíme ho uložit do souboru. A to nám půjde rozhodně lépe v textovém editoru. Interaktivní režim tedy pro tuto chvíli opustíme pomocí funkce exit(). 

Otevřeme editor a na první řádek nového souboru zapíšeme stejný příkaz jako v interaktivním režimu - print(“ahoj světe”). Nový soubor uložíme. Je dobré si pamatovat kam a pod jakým jménem - bude se to hned hodit. Jméno souboru by mělo naznačovat, co asi tak program dělá, přípona musí být .py - ta je určená právě pro Python programy.

Tak a teď musíme náš program spustit. Přejdeme tedy z editoru do příkazové řádky. V té se ještě musíme přepnout do pracovního adresáře. To je ten do kterého jsme před chvilkou uložili soubor s programem. Teď už stačí jen zavolat interpret příkazem python ahoj.py a počkat co se stane.

Sláva funguje to. Vždy když zavoláme interpret tímto způsobem, tak místo interaktivního režimu zpracuje příkazy ze souboru. Což je obvyklý způsob použití.
 
Teď se můžeme vrátit do editoru a přidat do programu další příkaz. V pythonu to jde velmi snadno. Má totiž hodně jednoduchý způsob zápisu programu - neboli syntax. Seznámíme se s ní postupně. Pro tuhle chvíli nám bohatě postačí když si zapamatujete, že nový příkaz se zapisuje na nový řádek.

Zkusme přidat další volání funkce print, tentokrát třeba výpočet druhé mocniny čtyř. Uložíme a opět přejdeme do příkazové řádky. Zopakujeme stejný příkaz jako minule python ahoj.py. Program by měl na nový řádek vypsat 16 - a vypsal. Výborné, začíná nám to jít.

Takže se můžeme vrátit do editoru, přidat další příkazy a opět je spustit v příkazové řádce. Programátorův denní chleba. Tenhle postup se opakuje pořád a pořád dokola, dokud není náš program hotový. I když těch příkazů do něj samozřejmě obykle napíšeme víc  najednou . 

Tak si to zkusme. Přidáme rovnou dvě volání funkce print. V prvním případě předáme funkci místo jedné hned dvě hodnoty - musíme je od sebe oddělit čárkou. Funkce se postará o to, že se vypíšou za sebe na jeden řádek. To se hodí, když například chceme k výsledku přidat nějaký komentář. No a ve druhém případě zkusíme vytisknout trochu delší větu. 

Uložíme, vrátíme se do příkazové řádky a spustíme program. 

Áááá něco je špatně. Program nedělá to co jsme chtěli. Dělá to co jsme mu přikázali. To bohužel dost často není totéž. Když počítač našemu příkazu nerozumí, dá nám to celkem rychle najevo. 

V tomhle případě říká, že na čtvrtém řádku našeho programu je chyba syntaxe. To znamená, že příkaz není zapsaný správně. Tady konkrétně jde o to, že text předávaný do funkce print musí být uzavřený do uvozovek. Takže to opravíme, uložíme a znovu otestujeme. A už nám to zase pracuje jak má.

Čím víc napíšete v životě programů, tím víc chybových hlášení uvidíte. Není potřeba se jich nějak bát. Jen málokterý program se povede na první dobrou. 

Náš první program - tedy sled příkazů, které říkají počítači co má dělat je hotový. Zatím nám k tomu stačil jediný příkaz - funkce print. Ale už příště si přidáme další základní stavební prvky každého programu - proměnné. 

Tak zatím ahoj. 
