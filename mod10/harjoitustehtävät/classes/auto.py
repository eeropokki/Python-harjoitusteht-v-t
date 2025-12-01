class Auto:

    def __init__(self, new_rekisteritunnus, new_huippunopeus):
        self.rekisteritunnus = new_rekisteritunnus
        self.huippunopeus = new_huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, arvo):
        pass
        # Lisää arvo self nopeuteen
        self.nopeus += arvo
        # Tarkasta ettei nopeus ole yli huippunopeus. Jos on, aseta nopeus = huippunopeus.
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        # Tarkasta ettei nopeus ole alle 0. Jos on, aseta nopeus = 0.
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        pass
        # Laske kuinka paljon auto on kulkenut annetussa ajassa tietyllä nopeudella.
        # Lisää kuljettu matka kokonaismatkaan.
        self.matka += self.nopeus * aika


