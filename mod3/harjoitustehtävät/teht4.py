vuosi = int(input("Anna vuosiluku: "))

if vuosi % 400 == 0:
    print(vuosi, "on karkausvuosi.")
elif vuosi % 100 == 0:
    print(vuosi, "ei ole karkausvuosi.")
elif vuosi % 4 == 0:
    print(vuosi, "on karkausvuosi.")
else:
    print(vuosi, "ei ole karkausvuosi.")