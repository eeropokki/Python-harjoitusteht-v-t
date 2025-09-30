import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    passwd="M3trinH4uki",
    autocommit=True
)

icao1 = input("Anna 1. lentokentän ICAO-koodi: ")
icao2 = input("Anna 2. lentokentän ICAO-koodi: ")

kursori = yhteys.cursor()
kursori.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (icao1,))
a = kursori.fetchone()

kursori.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (icao2,))
b = kursori.fetchone()

kursori.close()
yhteys.close()

if not a or not b:
    print("Toista kenttää ei löytynyt")
else:
    distance = geodesic(a,b).kilometers
    print(f"Etäisyys {icao1} - {icao2}: {distance:.2f} km")

