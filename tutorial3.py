"""
========================================
PYTHON ALAPVETŐ UTASÍTÁSOK ÉS SZINTAXIS
Tutorial - II. Óra
========================================

Ez a tutorial a Python programozás alapvető koncepcióit mutatja be:
- Alapvető utasítások
- Szintaxis
- Beépített adattípusok
- Operátorok
"""

print("="*60)
print("PYTHON ALAPVETŐ UTASÍTÁSOK ÉS SZINTAXIS - TUTORIAL")
print("="*60)

# ============================================================
# 1. PRINT UTASÍTÁS ÉS ALAPVETŐ OUTPUT
# ============================================================

print("\n1. PRINT UTASÍTÁS ÉS ALAPVETŐ OUTPUT")
print("-" * 60)

# Egyszerű print
print("Szia, világ!")

# Több érték nyomtatása
print("Név:", "János", "Kor:", 25)

# F-string (string formatting)
nev = "Péter"
kor = 30
print(f"A {nev} {kor} éves")

# Szöveges kifejezésekben escape karakterek
print("Ez egy \n új sor")
print("Tab\tkarakter")
print('Single és "double" idézőjelek')

# ============================================================
# 2. VÁLTOZÓK ÉS ÉRTÉKADÁS
# ============================================================

print("\n2. VÁLTOZÓK ÉS ÉRTÉKADÁS")
print("-" * 60)

# Változók deklarálása és inicializálása
x = 5
y = 10
z = x + y
print(f"x = {x}, y = {y}, z = {z}")

# Többszörös értékadás
a, b, c = 1, 2, 3
print(f"a = {a}, b = {b}, c = {c}")

# Érték cseréje
a, b = b, a
print(f"Csere után: a = {a}, b = {b}")

# Dinamikus típusozás
valtozo = 42
print(f"Típus: {type(valtozo)}")
valtozo = "szöveg"
print(f"Új típus: {type(valtozo)}")

# ============================================================
# 3. BEÉPÍTETT ADATTÍPUSOK RÉSZLETESEN
# ============================================================

print("\n3. BEÉPÍTETT ADATTÍPUSOK")
print("-" * 60)

# INT (Egész szám)
print("\n>>> INT (Egész szám):")
szam_int = 42
negatív = -15
nagy_szam = 1_000_000
print(f"Egész szám: {szam_int}, Negatív: {negatív}, Nagy: {nagy_szam}")

# FLOAT (Tizedes szám)
print("\n>>> FLOAT (Tizedes szám):")
pi = 3.14159
tizedes = 2.5
tudmanyos = 1.5e-3  # 0.0015
print(f"Pi: {pi}, Tudományos: {tudmanyos}")

# STRING (Szöveg)
print("\n>>> STRING (Szöveg):")
szoveg1 = "Python"
szoveg2 = 'programozás'
szoveg3 = """Ez egy
többsoros
szöveg"""
print(f"Szöveg: {szoveg1} {szoveg2}")
print(f"Többsoros:\n{szoveg3}")

# BOOL (Logikai érték)
print("\n>>> BOOL (Logikai érték):")
igaz = True
hamis = False
print(f"Igaz: {igaz}, Hamis: {hamis}")

# LIST (Lista)
print("\n>>> LIST (Lista - rendezett, módosítható):")
lista = [1, 2, 3, 4, 5]
vegyes_lista = [1, "szöveg", 3.14, True]
print(f"Lista: {lista}")
print(f"Vegyes lista: {vegyes_lista}")
print(f"Első elem: {lista[0]}, Utolsó: {lista[-1]}")

# TUPLE (Tuple)
print("\n>>> TUPLE (Tuple - rendezett, nem módosítható):")
tuple_adat = (1, 2, 3, 4, 5)
egy_elementu = (42,)
print(f"Tuple: {tuple_adat}")
print(f"Egy elemű tuple: {egy_elementu}")

# SET (Halmaz)
print("\n>>> SET (Halmaz - egyedi elemek, rendezetlen):")
halmaz = {1, 2, 3, 4, 5}
ures_halmaz = set()
print(f"Halmaz: {halmaz}")
print(f"Üres halmaz: {ures_halmaz}")

# DICT (Szótár)
print("\n>>> DICT (Szótár - kulcs-érték párok):")
szemely = {
    "név": "János",
    "kor": 25,
    "város": "Budapest",
    "végzettség": "BA"
}
print(f"Szótár: {szemely}")
print(f"Név: {szemely['név']}, Kor: {szemely['kor']}")

# ============================================================
# 4. OPERÁTOROK
# ============================================================

print("\n4. OPERÁTOROK")
print("-" * 60)

# ARITMETIKAI OPERÁTOROK
print("\n>>> ARITMETIKAI OPERÁTOROK:")
szam1 = 17
szam2 = 5
print(f"Összeadás: {szam1} + {szam2} = {szam1 + szam2}")
print(f"Kivonás: {szam1} - {szam2} = {szam1 - szam2}")
print(f"Szorzás: {szam1} * {szam2} = {szam1 * szam2}")
print(f"Osztás: {szam1} / {szam2} = {szam1 / szam2}")
print(f"Egész osztás: {szam1} // {szam2} = {szam1 // szam2}")
print(f"Maradék: {szam1} % {szam2} = {szam1 % szam2}")
print(f"Hatványozás: {szam1} ** {szam2} = {szam1 ** szam2}")

# ÖSSZEHASONLÍTÓ OPERÁTOROK
print("\n>>> ÖSSZEHASONLÍTÓ OPERÁTOROK:")
a = 10
b = 20
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

# LOGIKAI OPERÁTOROK
print("\n>>> LOGIKAI OPERÁTOROK:")
x = True
y = False
print(f"{x} and {y} = {x and y}")
print(f"{x} or {y} = {x or y}")
print(f"not {x} = {not x}")

# Kombinált logikai kifejezés
szam = 15
if 0 < szam < 20:
    print(f"{szam} a 0 és 20 közötti szám")

# BITWISE OPERÁTOROK
print("\n>>> BITWISE OPERÁTOROK:")
a = 5  # 0101
b = 3  # 0011
print(f"{a} & {b} (AND) = {a & b}")  # 0001 = 1
print(f"{a} | {b} (OR) = {a | b}")   # 0111 = 7
print(f"{a} ^ {b} (XOR) = {a ^ b}")  # 0110 = 6
print(f"~{a} (NOT) = {~a}")

# HOZZÁRENDELÉSI OPERÁTOROK
print("\n>>> HOZZÁRENDELÉSI OPERÁTOROK:")
x = 10
print(f"x = 10: {x}")
x += 5
print(f"x += 5: {x}")
x -= 3
print(f"x -= 3: {x}")
x *= 2
print(f"x *= 2: {x}")
x //= 4
print(f"x //= 4: {x}")

# ============================================================
# 5. FELTÉTELES UTASÍTÁSOK (IF-ELIF-ELSE)
# ============================================================

print("\n5. FELTÉTELES UTASÍTÁSOK")
print("-" * 60)

# IF utasítás
szam = 10
if szam > 0:
    print(f"{szam} pozitív szám")

# IF-ELSE utasítás
szam = -5
if szam >= 0:
    print(f"{szam} nem negatív")
else:
    print(f"{szam} negatív szám")

# IF-ELIF-ELSE utasítás
pont = 75
if pont >= 90:
    jegy = "A"
elif pont >= 80:
    jegy = "B"
elif pont >= 70:
    jegy = "C"
elif pont >= 60:
    jegy = "D"
else:
    jegy = "F"
print(f"Pont: {pont}, Jegy: {jegy}")

# Ternary operator (hármas operátor)
szam = 10
szoveg = "páros" if szam % 2 == 0 else "páratlan"
print(f"{szam} {szoveg} szám")

# ============================================================
# 6. CIKLUSOK
# ============================================================

print("\n6. CIKLUSOK")
print("-" * 60)

# FOR ciklus
print("\n>>> FOR ciklus (range használatával):")
for i in range(1, 6):
    print(f"  i = {i}")

# FOR ciklus listán
print("\n>>> FOR ciklus listán:")
gyumolcsok = ["alma", "banán", "narancs"]
for gyumolcs in gyumolcsok:
    print(f"  - {gyumolcs}")

# FOR ciklus szótáron
print("\n>>> FOR ciklus szótáron:")
szemely = {"név": "János", "kor": 25, "város": "Budapest"}
for kulcs, ertek in szemely.items():
    print(f"  {kulcs}: {ertek}")

# WHILE ciklus
print("\n>>> WHILE ciklus:")
szamlalo = 1
while szamlalo <= 3:
    print(f"  Számláló: {szamlalo}")
    szamlalo += 1

# BREAK utasítás
print("\n>>> BREAK utasítás (ciklus kilépése):")
for i in range(10):
    if i == 3:
        break
    print(f"  {i}", end=" ")
print()

# CONTINUE utasítás
print("\n>>> CONTINUE utasítás (iteráció kihagyása):")
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"  {i}", end=" ")
print()

# ELSE a ciklusban
print("\n>>> ELSE a ciklusban (ha normálisan fejeződik be):")
for i in range(3):
    print(f"  Iteráció {i}")
else:
    print("  Ciklus befejeződött!")

# ============================================================
# 7. LISTA OPERÁCIÓK ÉS INDEXELÉS
# ============================================================

print("\n7. LISTA OPERÁCIÓK ÉS INDEXELÉS")
print("-" * 60)

lista = [10, 20, 30, 40, 50]
print(f"Lista: {lista}")

# Indexelés
print(f"\nIndexelés:")
print(f"  lista[0] = {lista[0]}")
print(f"  lista[-1] = {lista[-1]}")
print(f"  lista[-2] = {lista[-2]}")

# Szeletelés (slicing)
print(f"\nSzeletelés:")
print(f"  lista[1:3] = {lista[1:3]}")
print(f"  lista[:3] = {lista[:3]}")
print(f"  lista[2:] = {lista[2:]}")
print(f"  lista[::2] = {lista[::2]}")
print(f"  lista[::-1] = {lista[::-1]}")

# Lista módosítása
print(f"\nLista módosítása:")
lista.append(60)
print(f"  append(60): {lista}")

lista.extend([70, 80])
print(f"  extend([70, 80]): {lista}")

lista.insert(2, 25)
print(f"  insert(2, 25): {lista}")

lista.remove(20)
print(f"  remove(20): {lista}")

elem = lista.pop()
print(f"  pop(): {elem}, lista: {lista}")

lista.sort()
print(f"  sort(): {lista}")

lista.reverse()
print(f"  reverse(): {lista}")

# ============================================================
# 8. SZÖVEG OPERÁCIÓK
# ============================================================

print("\n8. SZÖVEG OPERÁCIÓK")
print("-" * 60)

szoveg = "Python Programozás"
print(f"Eredeti szöveg: {szoveg}")

# Szöveg hossza
print(f"Hossz: {len(szoveg)}")

# Szöveg indexelése
print(f"Első karakter: {szoveg[0]}")
print(f"Utolsó karakter: {szoveg[-1]}")

# Szöveg szeletelése
print(f"Szelet [0:6]: {szoveg[0:6]}")

# Szöveg módosítása
print(f"Nagybetűsítés: {szoveg.upper()}")
print(f"Kisbetűsítés: {szoveg.lower()}")
print(f"Fordítás: {szoveg[::-1]}")

# Szöveg keresés és helyettesítés
print(f"Tartalmaz 'Python': {'Python' in szoveg}")
print(f"Helyettesítés: {szoveg.replace('Python', 'Java')}")

# Szöveg felosztása
szavak = szoveg.split()
print(f"Szavakra bontás: {szavak}")

# ============================================================
# 9. TÍPUSKONVERZIÓ
# ============================================================

print("\n9. TÍPUSKONVERZIÓ")
print("-" * 60)

# String to int
szam_str = "123"
szam_int = int(szam_str)
print(f"String '{szam_str}' -> int: {szam_int}, típus: {type(szam_int)}")

# String to float
szam_float = float("3.14")
print(f"String '3.14' -> float: {szam_float}, típus: {type(szam_float)}")

# Int to string
szam = 42
szoveg = str(szam)
print(f"Int 42 -> string: '{szoveg}', típus: {type(szoveg)}")

# List to tuple
lista = [1, 2, 3]
tupla = tuple(lista)
print(f"List {lista} -> tuple: {tupla}")

# String to list
szoveg = "Python"
karakterek = list(szoveg)
print(f"String 'Python' -> list: {karakterek}")

# ============================================================
# 10. INPUT ÉS OUTPUT
# ============================================================

print("\n10. INPUT ÉS OUTPUT")
print("-" * 60)

# Input olvasása (kommentben, hogy ne blokkoljuk a futást)
"""
nev = input("Mi a neved? ")
print(f"Szia, {nev}!")
"""

# Formázott output
szam = 123.456789
print(f"Normális: {szam}")
print(f"2 tizedes: {szam:.2f}")
print(f"Kitöltés nullákkal: {int(szam):05d}")

# ============================================================
# 11. OPERÁTOR PRECEDENCIA
# ============================================================

print("\n11. OPERÁTOR PRECEDENCIA")
print("-" * 60)

# Magas prioritás: **, unáris +/-
# Közepes prioritás: *, /, //, %
# Alacsony prioritás: +, -
# Legalacsonyabb: összehasonlítás, logikai operátorok

szam1 = 10 + 5 * 2
szam2 = (10 + 5) * 2
szam3 = 2 ** 3 ** 2
print(f"10 + 5 * 2 = {szam1}")
print(f"(10 + 5) * 2 = {szam2}")
print(f"2 ** 3 ** 2 = {szam3}")

# ============================================================
# ÖSSZEFOGLALÁS
# ============================================================

print("\n" + "="*60)
print("TUTORIAL VÉGE")
print("="*60)
print("\nA tutorial a következő témákat fedezte le:")
print("  1. Print utasítás és alapvető output")
print("  2. Változók és értékadás")
print("  3. Beépített adattípusok (int, float, str, bool, list, tuple, set, dict)")
print("  4. Operátorok (aritmetikai, összehasonlító, logikai, bitwise)")
print("  5. Feltételes utasítások (if-elif-else)")
print("  6. Ciklusok (for, while, break, continue)")
print("  7. Lista operációk és indexelés")
print("  8. Szöveg operációk")
print("  9. Típuskonverzió")
print("  10. Input és output")
print("  11. Operátor precedencia")
print("\nTovább gyakorláshoz készítsd el saját projektjeidet!")
print("="*60)

