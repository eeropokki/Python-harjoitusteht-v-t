nimet = set()
nimi = "x"

while nimi != "":
    nimi = input("Kirjoita nimi: ")

    if nimi != "":
        if nimi in nimet:
            print("Aiemmin syötetty nimi.")
        else:
            print("Uusi nimi.")
            nimet.add(nimi)

print("\nSyötetyt nimet: ")
for n in nimet:
    print(n)