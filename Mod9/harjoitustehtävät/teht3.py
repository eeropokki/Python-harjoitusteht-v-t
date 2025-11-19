from classes.auto import Auto

auto1 = Auto("ABC-123", 142)

auto1.matka = 2000
auto1.kiihdytä(60)
auto1.kulje(1.5)

print(f"Rekisteritunnus: {auto1.rekisteritunnus} "
      f"Huippunopeus: {auto1.huippunopeus} "
      f"Nopeus: {auto1.nopeus} "
      f"Matka: {auto1.matka}")

