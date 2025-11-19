import random
from classes.auto import Auto
from prettytable import PrettyTable

autot = []

for i in range(1, 11):
    # arvo huippunopeus 100-200
    huippunopeus = random.randint(100,200)
    autot.append(Auto("ABC-" + str(i), huippunopeus))

kokonaismatka = 0
while kokonaismatka < 10000:
    for auto in autot:
        # arvo nopeuden muutos -10 - 15
        # kutsu kiihdytä
        auto.kiihdytä(random.randint(-10,15))
        # kutsu kulje
        auto.kulje(1)

        # hae matkan arvo, jos yli 10000, lopeta kisa asettamalla auton matka kokonaismatkaksi
        if auto.matka > kokonaismatka:
            kokonaismatka = auto.matka

# googlaa joku taulukkokirjasto tulostamiseen
autot = sorted(autot, key=lambda a: a.matka, reverse=True)

table = PrettyTable(["Rekisteritunnus", "Nopeus (km/h)", "Huippunopeus (km/h)", "Matka (km)"])
for auto in autot:
    table.add_row([auto.rekisteritunnus, auto.nopeus, auto.huippunopeus, round(auto.matka, 1)])

print(table)
