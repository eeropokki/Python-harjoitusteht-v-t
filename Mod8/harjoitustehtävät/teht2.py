import mysql.connector

def hae_lentokenttien_lukumäärä_maakoodilla(maakoodi):
    sql = f"SELECT type, COUNT(*) FROM airport WHERE iso_country = '{maakoodi}' GROUP BY type ORDER BY COUNT(*) DESC;"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for row in tulos:
        print(f"{row[0]}: {row[1]}")

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    passwd="M3trinH4uki",
    autocommit=True
)

maakoodi = input("Kirjoita maakoodi: ")
hae_lentokenttien_lukumäärä_maakoodilla(maakoodi)