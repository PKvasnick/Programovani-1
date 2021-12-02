text = """
Praha -2 0
Brno 0 -1
Ostrava 1 1
"""
for radek in text.split("\n"):
    if len(radek) == 0:
        continue
    vec = radek.split(" ")
    mesta.append(vec[0])
    x.append(float(vec[1]))
    y.append(float(vec[2]))
