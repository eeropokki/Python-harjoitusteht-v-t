from flask import Flask, jsonify
from classes import lentokenttätietokanta

app = Flask(__name__)


@app.route('/kenttä/<icao>')
def kenttä(icao):
    rivi = lentokenttätietokanta.hae_lentokenttä_icao_koodilla(icao.upper())

    if rivi:
        vastaus = {
            "ICAO": rivi[0],
            "Name": rivi[1],
                "Municipality": rivi[2]
    }
    else:
        vastaus = {"error" : "lentokenttää ei löytynyt!"}

    return jsonify(vastaus)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
