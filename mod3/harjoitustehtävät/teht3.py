biologinensukupuoli: str = input("Biologinen sukupuolesi? ")
hemoglobiiniarvo: int = int(input("Hemoglobiini arvosi? "))

if biologinensukupuoli == "Nainen" and hemoglobiiniarvo < 117:
    print("Sinun hemoglobiini arvosi on alhainen. ")
elif biologinensukupuoli == "Nainen" and hemoglobiiniarvo > 175:
    print("Sinun hemoglobiini arvosi on korkea.")

if biologinensukupuoli == "Mies" and hemoglobiiniarvo < 134:
    print("Sinun hemoglobiini arvosi on alhainen.")
elif biologinensukupuoli == "Mies" and hemoglobiiniarvo > 195:
    print("Sinun hemoglobiini arvosi on korkea.")

elif biologinensukupuoli == "Mies" and 134 < hemoglobiiniarvo < 195:
    print("Sinun hemoglobiini arvosi on normaali.")

elif biologinensukupuoli == "Nainen" and 117 < hemoglobiiniarvo < 175:
    print("Sinun hemoglobiini arvosi on normaali.")