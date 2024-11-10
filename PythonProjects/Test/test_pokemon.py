import requests
import pytest

URL1 = 'https://api.pokemonbattle.me/v2/'
URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '9f45579541361a467aed4b34709eb506'
HEADER = {'Content-Type' : 'application/json' , "trainer_token": TOKEN }
TRAINER_ID = 8086

def test_status_code():
    response = requests.get (url = f'{URL1}/pokemons', params = {'trainer_id' : TRAINER_ID} )
    assert response.status_code == 200

def test_trainer_id():
    response_get = requests.get(url = f'{URL}trainers', params = {'trainer_id' : TRAINER_ID} )
    assert response_get.json()["data"][0]['trainer_name'] == 'Egor'
    print (response_get.text)