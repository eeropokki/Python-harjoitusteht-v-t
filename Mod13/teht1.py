from flask import Flask

app = Flask(__name__)


@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    vastaus = {
        # TODO: kirjaa, nyt isPrime arvo json-muodossa
        "Number": luku,
        "isPrime": True
    }

    # palautetaan palvelun kutsujalle saatu json-data
    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
