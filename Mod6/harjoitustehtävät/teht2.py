import random


def noppa(sivut):
    return random.randint(1, sivut)

def main():
    sivut = 21
    maksimi = int(input("Anna maksimisilmäluku, johon heittelyä jatketaan: "))

    silmaluku = 0
    while silmaluku != maksimi:
        silmaluku = noppa(sivut)
        print(f"Heitto: {silmaluku}")

if __name__ == "__main__":
    main()
