from classes.hissi import Hissi


def main():
    h = Hissi(1, 10)

    h.siirry_kerrokseen(5)
    h.siirry_kerrokseen(1)

if __name__ == '__main__':
    main()