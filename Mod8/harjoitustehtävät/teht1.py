import mysql.connector

def hae_lentokenttä_icao_koodilla(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{icao}';"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for row in tulos:
            print(f"{row[0]}: {row[1]} ")
    return

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    passwd="M3trinH4uki",
    autocommit=True
)

icao = input("Kirjoita ICAO-koodi: ")
hae_lentokenttä_icao_koodilla(icao)

