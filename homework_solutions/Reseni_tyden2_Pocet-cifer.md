## Řešení domácích úkolů - 2. týden

### Počet cifer

Určete počet cifer zadaného kladného celého čísla. Vstupní hodnotu načtěte ze standardního vstupu do proměnné celočíselného typu. Výsledek bude rovněž celé číslo, které zapište na standardní výstup.

Navrhněte obecné řešení, nezávislé na velikosti proměnné typu  longint. Nepoužívejte pole v žádné podobě, tzn. ani proměnné typu  string.

**Příklad:**

*vstup*

```
5814
```

*výstup*

```
4
```

### Řešení

**Analýza** Načítáme jediné číslo, u kterého máme spočíst počet cifer a ten vypsat na standardní výstup. Základní algoritmus spočívá v určení počtu dělení 10, potřebných ke zredukování čísla na jednociferné. I když to zadání nevyžaduje, bylo by dobré, aby řešení fungovalo i pro nulu.

### Vzorové řešení

Cokoli co dostaneme na vstupu, bude mít nejméně jednu číslic. Dokud máme číslo větší nebo rovno 10, přidáváme další číslici a číslo dělíme 10. 

```python
n = int(input())
ndigits = 1
while n >= 10:
    n //= 10
    ndigits += 1

print(ndigits)
```

 ### Alternativní řešení

**Logaritmus**: Pro určení počtu číslic můžeme také využít logaritmus.

```python
from math import log10

n = int(input())
ndigits = 1
if n > 0:
    ndigits += int(log10(n))

print(ndigits)
```



