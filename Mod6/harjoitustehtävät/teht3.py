def gallonsToLitres(gallons: float) -> float:
    return gallons * 3.785

def main():
    gallons = float(input("Anna bensiinin määrä (negatiivinen lopettaa): "))

    while gallons >= 0:
        litres = gallonsToLitres(gallons)
        print(f"{gallons} galloonaa = {litres:.2f} litraa bensiiniä.")

        gallons = float(input("Anna bensiinin määrä (negatiivinen lopettaa): "))

if __name__ == "__main__":
    main()


