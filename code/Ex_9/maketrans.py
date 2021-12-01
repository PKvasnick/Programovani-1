text = """
Zmráka sa, stmieva sa, k noci sa chýli.
– – – – – – – – – – – – – –
Od hory, od lesa tak plače, kvíli...
Výčitky neznámych duše sa chytia.
...Vyplniť nádeje nebolo sily –
zapadly, zapadly vo shone žitia...

Ohlaky nízko sú, tak letia, letia...!
Žaluje zúfale žaloby márne
ktos’ príliš úbohý z šíreho sveta,
že veril, že čakal, že starne, starne...

Zmráka sa, stmieva sa. Shora i zdola
havrany veslujú do noci spešne...
ktos’ príliš úbohý o pomoc volá,
do tvári hádže nám spomienky hriešne...
– – – – – – – – – – – – – –
Zmráka sa, pôjdeme... Noc je už zpola.
"""

find_chars = "\n"
replace_chars = " "
remove_chars = ",.–’!" # proto je dobře mít volbu uvozovek 

table = text.maketrans(find_chars, replace_chars, remove_chars)
print(text.translate(table).split())
