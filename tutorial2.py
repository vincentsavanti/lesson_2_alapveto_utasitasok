"""
========================================
PYTHON ALAPVETŐ UTASÍTÁSOK ÉS SZINTAXIS
II. Óra - Tutorial2
========================================
Forrás: https://pythonprogramozas.blogspot.com/2026/02/2-ora-alapveto-utasitasok-es-szintaxis.html
"""

print("="*70)
print("PYTHON ALAPVETŐ UTASÍTÁSOK ÉS SZINTAXIS - TUTORIAL2")
print("="*70)

# ============================================================
# SZINTAXIS (PYTHON)
# ============================================================

print("\n" + "="*70)
print("SZINTAXIS (PYTHON)")
print("="*70)

# 1. BEHÚZÁS (INDENTÁLÁS)
print("\n1. BEHÚZÁS (INDENTÁLÁS)")
print("-" * 70)
print("A Python blokkjait (pl. feltételek, ciklusok, függvények) kötelező behúzással jelöljük.")

if True:
    print("Ez egy blokk")

# 2. KETTŐSPONT HASZNÁLATA (:)
print("\n2. KETTŐSPONT HASZNÁLATA (:)")
print("-" * 70)
print("A vezérlési szerkezetek és függvények definíciója kettősponttal végződik.")

for i in range(3):
    print(i)

# 3. MEGJEGYZÉSEK
print("\n3. MEGJEGYZÉSEK")
print("-" * 70)
print("A # egysoros kommentet jelöl, a három idézőjeles szöveg több soros docstring lehet.")

# Ez egy komment

def fuggveny():
    """Ez egy docstring"""
    pass

fuggveny()

# 4. DINAMIKUS TÍPUSKEZELÉS
print("\n4. DINAMIKUS TÍPUSKEZELÉS")
print("-" * 70)
print("A változók típusa futásidőben dől el, nem kell előre deklarálni.")

x = 10
print(f"x = {x}, típus: {type(x)}")
x = "szöveg"
print(f"x = {x}, típus: {type(x)}")

# 5. NINCS SZÜKSÉG PONTOSVESSZŐRE
print("\n5. NINCS SZÜKSÉG PONTOSVESSZŐRE")
print("-" * 70)
print("Pythonban a sorvége jelzi az utasítás végét.")

a = 5
b = 10
print(a + b)

# ============================================================
# ALAPVETŐ UTASÍTÁSOK (PYTHON)
# ============================================================

print("\n" + "="*70)
print("ALAPVETŐ UTASÍTÁSOK (PYTHON)")
print("="*70)

# 1. VÁLTOZÓÉRTÉKADÁS
print("\n1. VÁLTOZÓÉRTÉKADÁS")
print("-" * 70)
print("Értéket az egyenlőségjellel (=) adunk változónak.")

x = 42
print(f"x = {x}")

# 2. FELTÉTELES ELÁGAZÁS (IF, ELIF, ELSE)
print("\n2. FELTÉTELES ELÁGAZÁS (IF, ELIF, ELSE)")
print("-" * 70)
print("Logikai feltételek alapján különböző kódrészletek hajthatók végre.")

x = 10
if x > 0:
    print("Pozitív")
elif x == 0:
    print("Nulla")
else:
    print("Negatív")

# 3. CIKLUSOK (FOR, WHILE)
print("\n3. CIKLUSOK (FOR, WHILE)")
print("-" * 70)
print("Ismétlődő műveletek végrehajtására szolgálnak.")

print("\nFor ciklus:")
for i in range(3):
    print(i)

print("\nWhile ciklus:")
while False:
    print("Nem fut le")

# 4. FÜGGVÉNYDEFINIÁLÁS (DEF)
print("\n4. FÜGGVÉNYDEFINIÁLÁS (DEF)")
print("-" * 70)
print("Újrafelhasználható kódrészlet létrehozása.")

def koszones(nev):
    return "Szia " + nev

print(koszones("Anna"))

# 5. MODULOK IMPORTÁLÁSA
print("\n5. MODULOK IMPORTÁLÁSA")
print("-" * 70)
print("Külső modulok funkcióinak használata.")

import math
print(math.sqrt(16))

# 6. BEMENET ÉS KIMENET
print("\n6. BEMENET ÉS KIMENET")
print("-" * 70)
print("Az input() beolvas, a print() kiír.")

# Kommentben tartjuk, hogy ne blokkoljuk az interaktív futást
# nev = input("Add meg a neved: ")
# print("Szia", nev)

# Helyette mutatunk egy példát:
nev = "János"
print("Szia", nev)

# ============================================================
# BEÉPÍTETT ADATTÍPUSOK (PYTHON)
# ============================================================

print("\n" + "="*70)
print("BEÉPÍTETT ADATTÍPUSOK (PYTHON)")
print("="*70)

# 1. INT
print("\n1. INT - Egész számok")
print("-" * 70)
print("Egész számok tárolására szolgál.")

x = 10
print(f"x = {x}, típus: {type(x)}")

# 2. FLOAT
print("\n2. FLOAT - Lebegőpontos számok")
print("-" * 70)
print("Lebegőpontos számok.")

pi = 3.14
print(f"pi = {pi}, típus: {type(pi)}")

# 3. BOOL
print("\n3. BOOL - Logikai értékek")
print("-" * 70)
print("Logikai érték: True vagy False.")

igaz = True
print(f"igaz = {igaz}, típus: {type(igaz)}")

# 4. STR
print("\n4. STR - Szöveges adat")
print("-" * 70)
print("Szöveges adat.")

szoveg = "Hello"
print(f"szoveg = {szoveg}, típus: {type(szoveg)}")

# 5. LIST
print("\n5. LIST - Rendezett, módosítható adatsorozat")
print("-" * 70)
print("Rendezett, módosítható adatsorozat.")

lista = [1, 2, 3]
print(f"lista = {lista}, típus: {type(lista)}")

# 6. TUPLE
print("\n6. TUPLE - Rendezett, nem módosítható adatsorozat")
print("-" * 70)
print("Rendezett, nem módosítható adatsorozat.")

t = (1, 2, 3)
print(f"t = {t}, típus: {type(t)}")

# 7. DICT
print("\n7. DICT - Kulcs-érték párokat tárol")
print("-" * 70)
print("Kulcs-érték párokat tárol.")

szotar = {"nev": "Anna", "kor": 20}
print(f"szotar = {szotar}, típus: {type(szotar)}")

# 8. SET
print("\n8. SET - Ismétlődésmentes elemek halmaza")
print("-" * 70)
print("Ismétlődésmentes elemek halmaza.")

halmaz = {1, 2, 3}
print(f"halmaz = {halmaz}, típus: {type(halmaz)}")

# ============================================================
# OPERÁTOROK (PYTHON)
# ============================================================

print("\n" + "="*70)
print("OPERÁTOROK (PYTHON)")
print("="*70)

# 1. ARITMETIKAI OPERÁTOROK
print("\n1. ARITMETIKAI OPERÁTOROK")
print("-" * 70)
print("Számítási műveletek: +, -, *, /, //, %, **")

print(5 + 2)
print(5 ** 2)

# 2. ÖSSZEHASONLÍTÓ OPERÁTOROK
print("\n2. ÖSSZEHASONLÍTÓ OPERÁTOROK")
print("-" * 70)
print("Két érték összehasonlítása.")

print(5 > 3)

# 3. LOGIKAI OPERÁTOROK
print("\n3. LOGIKAI OPERÁTOROK")
print("-" * 70)
print("Logikai műveletek: and, or, not")

print(True and False)

# 4. ÉRTÉKADÓ OPERÁTOROK
print("\n4. ÉRTÉKADÓ OPERÁTOROK")
print("-" * 70)
print("Rövidített értékadás.")

x = 5
x += 2
print(x)

# 5. TAGSÁGI OPERÁTOROK
print("\n5. TAGSÁGI OPERÁTOROK")
print("-" * 70)
print("Ellenőrzi, hogy egy elem szerepel-e egy gyűjteményben.")

print(3 in [1, 2, 3])

# 6. AZONOSÍTÓ OPERÁTOROK
print("\n6. AZONOSÍTÓ OPERÁTOROK")
print("-" * 70)
print("Az objektumazonosság vizsgálata (is).")

a = None
print(a is None)

# ============================================================
# ÖSSZEFOGLALÁS
# ============================================================

print("\n" + "="*70)
print("TUTORIAL2 VÉGE")
print("="*70)
print("\nA tutorial a következő témákat fedezte le:")
print("  - SZINTAXIS: Behúzás, kettőspont, megjegyzések, típuskezelés")
print("  - ALAPVETŐ UTASÍTÁSOK: Változó, feltétel, ciklusok, függvények, modulok, I/O")
print("  - BEÉPÍTETT ADATTÍPUSOK: int, float, bool, str, list, tuple, dict, set")
print("  - OPERÁTOROK: Aritmetikai, összehasonlító, logikai, értékadó, tagsági, azonosító")
print("\n" + "="*70)

