from classes.hissi import Hissi

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for _ in range(hissien_maara):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissia(self, hissi_numero, kohde_kerros):
        if 1 <= hissi_numero <= len(self.hissit):
            print(f"Ajetaan hissiä {hissi_numero} kerrokseen {kohde_kerros}.")
            hissi = self.hissit[hissi_numero - 1]
            hissi.siirry_kerrokseen(kohde_kerros)
        else:
            print(f"Hissiä {hissi_numero} ei ole olemassa.")

    def palohalytys(self):
        print("PALOHÄLYTYS! Kaikki hissit siirtyvät pohjakerrokseen. ")
        for index, hissi in enumerate(self.hissit, start=1):
            print(f"Hissi {index}: ")
            hissi.siirry_kerrokseen(self.alin_kerros)

if __name__ == '__main__':
    talo = Talo(1, 10, 3)

    talo.aja_hissia(1, 5)

    talo.aja_hissia(2, 8)

    talo.aja_hissia(1, 1)

    talo.aja_hissia(3, 7)

    talo.palohalytys()
