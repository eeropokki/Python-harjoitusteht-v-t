vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä",
              "syksy", "syksy", "syksy", "talvi")

kuukausiNro = int(input("Anna kuukauden numero (1-12): "))

vuodenaika = vuodenajat[kuukausiNro-1]

print(f"{kuukausiNro}. on {vuodenaika}")

