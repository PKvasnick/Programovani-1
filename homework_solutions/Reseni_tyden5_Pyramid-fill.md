## Řešení domácích úkolů - 5. týden

### Pyramidová výplň

Načtěte ze standardního vstupu přirozené číslo $n$ a vyplňte čtverec $n\times n$ čísly  takto:

 1     2     3     2     1    
 2     3     4     3     2    
 3     4     5     4     3    
 2     3     4     3     2    
 1     2     3     2     1    

anebo

 1     2     2     1    
 2     3     3     2    
 2     3     3     2    
 1     2     2     1    

Čísla v každém sloupci a řádku rostou ve směru ke středu matice vždy o 1. 

Implementujte matici jako seznam seznamů a vyplněnou schému vytiskněte jako seznam na standardní výstup. 

#### Příklad 1

**Vstup:**

2

**Výstup:**

[[1, 1], [1, 1]]

#### Příklad 2

**Vstup:**

6

**Výstup:**

[[1, 2, 3, 3, 2, 1], [2, 3, 4, 4, 3, 2], [3, 4, 5, 5, 4, 3], [3, 4, 5, 5, 4, 3], [2, 3, 4, 4, 3, 2], [1, 2, 3, 3, 2, 1]]

#### Poznámky

- ReCodEx-ové testy pro tento úkol kontrolují správné řešení pro n = 2, 5, 10. 
- Tak jako obvykle bude odměněn čistý kód. 

---

### Analýza

Tato úloha se zakládá na nalezení a kombinování vzoru. I když lze konstruovat požadovaný obrazec mnohými způsoby, základním krokem je uvědomění si, že všechny obrazce lze konstruovat ze základního vzoru typu `1 2 3 4 3 2 1`, a to v horizontálním i vertikálnim směru. 

### Vzorové řešení

Začneme tím, že zkonstruujeme základní vzor:

```python
row = [min(i, n-i+1) for i in range(1,n+1)]
```

Toto generuje posloupnosti typu `1 2 3 ... 3 2 1`.

Tento vzor pak stačí použít na horizontální i vertikální směr:

```python
n = int(input())

row = [min(i, n-i+1) for i in range(1,n+1)]
rows = [[row[i] + row[j] - 1 for i in range(n)] for j in range(n)]

print(rows)
```

#### Obvyklé problémy

Tato úloha je vnímána jako lehká a objevuje se celá plejáda různých řešení. Ocenění se dostává elegantním řešením, zatímco efektivnost kódu u této úlohy nehraje roli. 
