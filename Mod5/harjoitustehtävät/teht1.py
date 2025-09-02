import random

arpakuutiot = int(input("Montako arpakuutiota? "))

heitot = []

for i in range(arpakuutiot):
    heitto = random.randint(1,6)
    heitot.append(heitto)

print(f"Silmälukujen arvot: {heitot}")
print(f"Silmälukujen summa: {sum(heitot)}")

