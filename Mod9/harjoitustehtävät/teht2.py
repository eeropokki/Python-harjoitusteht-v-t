from classes.auto import Auto

auto1 = Auto("ABC-123", 142)

print(f"Rekisteritunnus,{auto1.rekisteritunnus} "
      f"Huippunopeus {auto1.huippunopeus} "
      f"Nopeus {auto1.nopeus} "
      f"Matka {auto1.matka}")

auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)

print(f" Auton nopeus kiihdytyksen jälkeen {auto1.nopeus} km/h ")

# jarrutus
auto1.kiihdytä(-200)

print(f" Auton nopeus hätäjarrutuksen jälkeen: {auto1.nopeus} km/h ")