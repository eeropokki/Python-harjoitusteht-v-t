yritykset = 0

oikeaTunnus = "python"
oikeaSalasana = "rules"

kauttajatunnus = input("Mikä on käyttäjätunnus? ")
salasana = input("Mikä on salasana? ")
yritykset += 1

while (kauttajatunnus != oikeaTunnus or salasana != oikeaSalasana) and yritykset < 5:
    print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")
    kauttajatunnus = input("Mikä on käyttäjätunnus? ")
    salasana = input("Mikä on salasana? ")
    yritykset += 1

if kauttajatunnus == oikeaTunnus and salasana == oikeaSalasana:
    print("Tervetuloa!")
else:
    print("Pääsy evätty")
