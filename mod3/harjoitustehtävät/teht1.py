kuhanmitta = float(input("kuhan pituus senttimetreinä: "))

puuttuvamitta = 37 - kuhanmitta

if kuhanmitta < 37:
    print("Kuha on alamittainen. Laske kuha takaisin järveen.")
    print(f"Sinulta puuttuu {puuttuvamitta} cm alimmasta sallitusta pyyntimitasta.")