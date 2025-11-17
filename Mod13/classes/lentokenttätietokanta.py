import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    passwd="M3trinH4uki",
    autocommit=True
)

def hae_lentokenttä_icao_koodilla(icao):
    sql = "SELECT ident, name, municipality FROM airport WHERE ident= %s"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao,))
    rivi = kursori.fetchone()
    kursori.close()
    return rivi

