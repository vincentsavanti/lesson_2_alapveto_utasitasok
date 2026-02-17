# ============================================
# PYTHON ALAPVETŐ UTASÍTÁSOK ÉS SZINTAXIS
# ============================================

# 1. BEÉPÍTETT ADATTÍPUSOK
# ========================

# Egész szám (int)
szam_int = 42
print(f"Integer: {szam_int}, típus: {type(szam_int)}")

# Tizedes szám (float)
szam_float = 3.14
print(f"Float: {szam_float}, típus: {type(szam_float)}")

# Szöveg (string)
szoveg = "Hello Python!"
print(f"String: {szoveg}, típus: {type(szoveg)}")

# Logikai érték (bool)
igaz = True
hamis = False
print(f"Boolean: {igaz}, {hamis}, típus: {type(igaz)}")

# Lista (list) - rendezett, módosítható
lista = [1, 2, 3, "szöveg", 3.14]
print(f"Lista: {lista}, típus: {type(lista)}")

# Tuple (tuple) - rendezett, nem módosítható
tuple_adat = (1, 2, 3, "szöveg")
print(f"Tuple: {tuple_adat}, típus: {type(tuple_adat)}")

# Szótár (dict) - kulcs-érték párok
szotar = {"név": "János", "kor": 25, "város": "Budapest"}
print(f"Szótár: {szotar}, típus: {type(szotar)}")

# Halmaz (set) - egyedi elemek, rendezetlen
halmaz = {1, 2, 3, 4, 5}
print(f"Halmaz: {halmaz}, típus: {type(halmaz)}")

print("\n" + "="*50 + "\n")

# 2. OPERÁTOROK
# =============

# Aritmetikai operátorok
a = 10
b = 3

print("ARITMETIKAI OPERÁTOROK:")
print(f"Összeadás: {a} + {b} = {a + b}")
print(f"Kivonás: {a} - {b} = {a - b}")
print(f"Szorzás: {a} * {b} = {a * b}")
print(f"Osztás: {a} / {b} = {a / b}")
print(f"Egész osztás: {a} // {b} = {a // b}")
print(f"Maradék (modulo): {a} % {b} = {a % b}")
print(f"Hatványozás: {a} ** {b} = {a ** b}")

print("\nÖSSZEHASONLÍTÓ OPERÁTOROK:")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

print("\nLOGIKAI OPERÁTOROK:")
x = True
y = False
print(f"{x} and {y} = {x and y}")
print(f"{x} or {y} = {x or y}")
print(f"not {x} = {not x}")

print("\nHIVATALOS OPERÁTOROK:")
c = 5
d = 5
e = "hello"
f = "hello"
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

print(f"{c} is {d}: {c is d}")  # azonos-e az azonosító
print(f"{e} is {f}: {e is f}")  # string interning miatt True
print(f"5 in [1,2,3,4,5]: {5 in [1, 2, 3, 4, 5]}")
print(f"'a' in 'hello': {'a' in 'hello'}")

print("\n" + "="*50 + "\n")

# 3. ALAPVETŐ UTASÍTÁSOK
# ======================

print("ALAPVETŐ UTASÍTÁSOK:")

# Feltételes utasítás (if-elif-else)
szam = 15
if szam < 0:
    print(f"{szam} negatív szám")
elif szam == 0:
    print(f"{szam} nulla")
else:
    print(f"{szam} pozitív szám")

# Ciklus (for)
print("\nFor ciklus (0-tól 4-ig):")
for i in range(5):
    print(f"  i = {i}")

# Ciklus (while)
print("\nWhile ciklus:")
szamlalo = 0
while szamlalo < 3:
    print(f"  Számlálás: {szamlalo}")
    szamlalo += 1

# Break és continue
print("\nBreak és continue:")
for i in range(10):
    if i == 3:
        continue  # Kihagyja ezt az iterációt
    if i == 7:
        break     # Kilép a ciklusból
    print(f"  {i}", end=" ")
print()

print("\n" + "="*50 + "\n")

# 4. TÍPUSKONVERZIÓ
# =================

print("TÍPUSKONVERZIÓ:")
szam_str = "123"
szam_int = int(szam_str)
print(f"String '{szam_str}' átkonvertálva int-re: {szam_int}")

szam_float = float("3.14")
print(f"String '3.14' átkonvertálva float-ra: {szam_float}")

szam_str2 = str(42)
print(f"Integer 42 átkonvertálva string-re: '{szam_str2}'")

szam_bool = bool(1)
print(f"Integer 1 átkonvertálva bool-ra: {szam_bool}")

print("\n" + "="*50 + "\n")

# 5. LISTA OPERÁCIÓK
# ==================

print("LISTA OPERÁCIÓK:")
lista = [10, 20, 30, 40, 50]
print(f"Original lista: {lista}")
print(f"Első elem (index 0): {lista[0]}")
print(f"Utolsó elem (index -1): {lista[-1]}")
print(f"Szelet [1:3]: {lista[1:3]}")

lista.append(60)
print(f"Append után: {lista}")

lista.extend([70, 80])
print(f"Extend után: {lista}")

lista.remove(30)
print(f"Remove(30) után: {lista}")

print(f"Lista hossza: {len(lista)}")

print("\n" + "="*50)
print("KÉSZ A BEMUTATÓ!")
print("="*50)
