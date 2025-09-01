syote = float(input("Mikä luku? "))

if syote == "":
    print("Ohjelma lopetetaan!")
else:
    luku = float(syote)
    pieninluku = suurinluku = luku


    syote = input("Mikä luku? ")

    while syote != "":

        luku = float(syote)

        if luku < pieninluku:
            pieninluku = luku
        if luku > suurinluku:
            suurinluku = luku

        syote = input("Mikä luku? ")

print(f"Pienin luku: {pieninluku}")
print(f"Suurin luku: {suurinluku}")
