import requests as r;
url = 'https://pokeapi.co/api/v2/pokemon/ditto/';
req = r.get(url);
poke = req.csv();
print(poke);