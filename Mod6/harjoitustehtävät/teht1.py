import random


def noppa():
    return random.randint(1, 6)

def main():
    silmaluku = 0
    while silmaluku != 6:
        silmaluku = noppa()
        print(f"Heitto: {silmaluku}")

if __name__ == "__main__":
    main()
