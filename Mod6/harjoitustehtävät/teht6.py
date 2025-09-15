import math

def pizza(halkaisijaCM, hintaEuro):

    halkaisijaM = halkaisijaCM / 100
    pinta_ala = math.pi * (halkaisijaM / 2) ** 2

    return hintaEuro / pinta_ala

def main():
    halkaisija1 = float(input("Pizzan halkaisija : "))
    hinta1 = float(input("Pizzan hinta : "))
    yksikköhinta1 = pizza(halkaisija1, hinta1)

    halkaisija2 = float(input("Pizzan halkaisija : "))
    hinta2 = float(input("Pizzan hinta : "))
    yksikköhinta2 = pizza(halkaisija2, hinta2)

    print(f"1. pizzan yksikköhinta: {yksikköhinta1:.2f} €/neliömetriä.")
    print(f"2. pizzan yksikköhinta: {yksikköhinta2:.2f} €/neliömetriä.")

    if yksikköhinta1 < yksikköhinta2:
        print("Ensimmäinen pizza on parempi vastine rahalle.")
    elif yksikköhinta2 < yksikköhinta1:
        print("Toinen pizza on parempi vastine rahalle.")
    else:
        print("Pizzat ovat yhtä edullisia neliömetriä kohti.")

if __name__ == '__main__':
    main()