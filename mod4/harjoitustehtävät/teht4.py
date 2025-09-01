import random

randomNumber = random.randint(1, 10)
arvaus = int(input("Arvaa kokonaisluku (1-10 välillä): "))

while arvaus != randomNumber:

    if arvaus > randomNumber:
        print("Liian suuri arvaus. ")
    if arvaus < randomNumber:
        print("Liian pieni arvaus. ")

    arvaus = int(input("Arvaa kokonaisluku (1-10 välillä): "))

print("Arvasit oikein! ")