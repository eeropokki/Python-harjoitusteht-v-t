luku = int(input("Anna kokonaisluku: "))

if luku < 2:
    print("Luku ei ole alkuluku.")
else:
    on_alkuluku = True
    for i in range(2, luku):
        if luku % i == 0 :
            on_alkuluku = False

    if on_alkuluku:
        print("Luku on alkuluku!")
    else:
        print("Luku ei ole alkuluku.")