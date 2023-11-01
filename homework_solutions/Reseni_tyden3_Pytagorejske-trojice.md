## Řešení domácích úkolů - 3. týden

### Pythagorejské trojice

Pro dané $n$ vypište počet různých trojic přirozených čísel a, b, c takových, že
- $a,b,c \le n$
- $a \lt b$
- $a$ a $b$ jsou nesoudělná
- $a^2 + b^2 = c^2$

### Řešení

**Analýza** 

Řešení hrubou sílou: 

Prohledáme prostor přípustných trojic a, b, c. U těchto řešení můžeme dosáhnout významné úspory, když vhodně zmenšíme dimenzi prohledávaného prostoru, a když pak zvolíme rozumně úzké intervaly přípustných hodnot. 

Alternativní řešení:

Celá čísla m, n, $m>n$, definují unikátní Pythagorejskou trojici takto:
$$
a = m^2 - n^2,\quad b = 2mn,\quad c = m^2 + n^2
$$
Namísto prostoru a, b, c tedy můžeme prohledávat prostor m, n. 



### Vzorové řešení

V tomto řešení:

- i neboli a je nejmenší člen trojice a probíhá nezávisle od 1 do n. Přesnější by bylo zvolit interval od 2 do 0,71n - žádná Pythagorejská trojice neobsahuje číslo 1 a pokud má být i nejmenším členem trojice, musí být menší než $n / \sqrt{2}$.
- j neboli b musí být větší než i.
- k neboli c musí být úplným čtvercem a splňovat s i,j Pythagorovu větu. Pokud jsou i, j nesoudělná, je i, j, k Pythagorejská trojice. 

Nesoudělnost ověřujeme až nakonec, protože je určitě častější než Pythagorejská vlastnost, takže bychom zbytečně testovali soudělnost obrovského počtu dvojic. 

```python
from math import sqrt, gcd

n = int(input())
count = 0

for i in range(1, n):
    for j in range(i+1, n):
        k = sqrt(i * i + j * j)
        if int(k) == k and k <= n and gcd(i, j) == 1:
                count += 1

print(count)
```

 ### Alternativní řešení

Protože m, n generují unikátní trojici, v případě nalezení trojice s a > b prostě a, b prohodíme, tedy trojici započteme.

```python
max_n = int(input())

pocet = 0

for m in range(2, max_n):
    for n in range(1, m):
        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
        if a > 0 and c <= max_n and gcd(a, b) == 1:
            pocet += 1

print(pocet)
```

### Obvyklé problémy v řešeních

#### Testy

Pro tuto úlohu má ReCodEx 3 testy s hodnotami n = 10, 100, 300. Příslušné počty Pythagorejských trojic jsou 1, 16 a 47. 

Časté chyby:

- Vylučování řešení s a > b u alternativního ŕešení. 
- Přílišné "osekání" prohledávané oblasti. Je lepší si raději nechat bezpečnostní "okraj".

