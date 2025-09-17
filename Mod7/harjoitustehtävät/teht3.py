lentoasemat = {}

komento = ""

while komento != "lopeta":
    komento = input("Haluatko syöttää uuden lentoaseman ('syötä'), hakea jo syötetyn lentoaseman ('hae') vai lopettaa?"
                   " (komento 'lopeta' lopettaa) ")

    if komento == "syötä":
        icao = input("Syötä ICAO-koodi: ")
        name = input("Syötä lentoaseman nimi: ")
        if icao and name:
            lentoasemat[icao] = name
            print(f"Tallennettu: {icao} = {name}")
        else:
            print("VIRHE: koodi ja nimi eivät saa olla tyhjiä. ")
    elif komento == "hae":
        icao = input("Syötä ICAO-koodi: ")
        name = lentoasemat.get(icao)
        if name is None:
            print("Koodia ei löydy. ")
        else:
            print(f"{icao}: {name}")

print("Ohjelma päättyi.")