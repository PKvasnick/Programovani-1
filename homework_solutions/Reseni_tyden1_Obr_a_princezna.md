## Řešení domácích úkolů - 1. týden

### Obr a princezna

Aby princezně nebylo ve věži smutno, obr pro ni vymyslel hru. Budou soutěžit, kdo vymyslí větší číslo. Každé kolo začíná tak, že princezna napíše své číslo na standardní vstup vašeho programu, a následně zapíše své číslo obr. Váš program pak na standardní výstup vypíše "P", pokud vyhrála princezna, "O", pokud vyhrál obr, a "R", pokud hra nemá vítěze.

**Příklad:**

*Vstup:*
 10
 12
 *Výstup:*
 O

*Vstup:*
 12
 10
 *Výstup:*
 P

*Vstup:*
 10
 10
 *Výstup:*
 R

### Řešení

**Analýza** Ze vstupu načteme dvě čísla a podle výsledku třícestného srovnání vypíšeme na standardní výstup příslušný znak. Detaily:

- nepíšeme na standardní výstup nic jiného
- input() přečte ze standardního vstupu řetězec, zkonvertujeme na číslo pomocí int().

### Vzorové řešení

```python
princezna = int(input())   # input() - žádná výzva
obr = int(input())         # int, aby se vstup zkonvertoval na celé číslo.

if princezna > obr:
    print("P")
elif obr > princezna:
    print("O")
else:
    print("R")
```

 

### Obvyklé problémy v řešeních

```python
princezna = int(input("Zadej číslo princezny: "))
obr = int(input("Zadej číslo obra: "))
```

Výzvy se vypisují na standardní výstup. Protože jde o neznámý text, ReCodEx je nedokáže odfiltrovat od řešení a takovéto řešení tudíž neprojde testy. 

```python
princezna = input()
obr = input()
```

Pokud nezkonvertujete vstupní hodnoty na čísla, porovnají se jako řetězce, tudíž podle pořadí v abecedním uspořádání. V tomto uspořádání je např. "2" > "13".