# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
# Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
# Käyttäjälle on näytettävä pelkkä vitsin teksti.

import json
import requests

request = "https://api.chucknorris.io/jokes/random"

answer = requests.get(request).json()

print(answer["value"])