import requests 

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '9f45579541361a467aed4b34709eb506'
HEADER = {'Content-Type' : 'application/json' , "trainer_token": TOKEN }
body_creat = {
    "name": "Ультра",
    "photo_id": 52
}
body_name = {
    "pokemon_id": "128011",
    "name": "ЕГОрчикс",
    "photo_id": 52
}
body_boy = {
    "pokemon_id": "128011"  
}

'''response = requests.post (url = f'{URL}pokemons', headers = HEADER, json = body_creat)
print (response.text)'''

'''response_name = requests.put (url = f'{URL}pokemons', headers = HEADER, json = body_name)
print (response_name.text)''' 

response_attack = requests.post (url = f'{URL}trainers/add_pokeball',headers = HEADER, json = body_boy)
print (response_attack.text) 