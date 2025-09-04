luvut = []

luku = input("Syötä luku (tyhjä merkkijono lopettaa): ")

if luku == "":
    print("Lopetit ohjelman. ")
else:
    while luku != "":
        luvut.append (int(luku))
        luku = input("Syötä luku (tyhjä merkkijono lopettaa): ")
    luvut.sort(reverse=True)
    print(luvut[0:6 -1])