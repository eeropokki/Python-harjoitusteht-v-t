import random
from classes.auto import Auto
from prettytable import PrettyTable


class Kilpailu:
    def __init__(self, kilpailun_nimi, kilpailun_pituus, osallistuvat_autot):
        self.nimi = kilpailun_nimi
        self.pituus = kilpailun_pituus
        self.autot = osallistuvat_autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        jarjestetyt_autot = sorted(self.autot, key=lambda a: a.matka, reverse=True)

        table = PrettyTable(["Rekisteritunnus", "Nopeus (km/h)", "Huippunopeus (km/h)", "Matka (km)"])
        for auto in jarjestetyt_autot:
            table.add_row([auto.rekisteritunnus, auto.nopeus, auto.huippunopeus, round(auto.matka, 1)])

        print(table)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False


if __name__ == "__main__":

    autot = [Auto(f"ABC-{i + 1}", random.randint(100, 200)) for i in range(10)]

    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    tunnit = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunnit += 1

        if tunnit % 10 == 0:
            kilpailu.tulosta_tilanne()

    print(f"Kilpailu on päättynyt! Lopullinen tulos.")
    kilpailu.tulosta_tilanne()
