def kokonaisluvut(luvut):
    return [luku for luku in luvut if luku % 2 != 0]

def main():
    luvut = [1,2,3,4,5,6,7,8,9,10]
    karsitut = kokonaisluvut(luvut)

    print("Alkuperäinen lista:", luvut)
    print("Parilliset karsittu:", karsitut)


if __name__ == "__main__":
    main()