inch = float(input("Montako tuumaa? "))

while inch >= 0:
    cm = inch * 2.54
    print (f"{inch} tuumaa = {cm:.2f} cm.")

    inch = float(input("Montako tuumaa? "))

print ("Ohjelma lopetetaan!")