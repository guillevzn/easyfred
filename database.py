import sqlite3


def connect():
    return sqlite3.connect('database.db')

def create_table(connection):
    with connection:
        connection.execute(
            'CREATE TABLE beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);'
        )

create_table(connect())
#%%
import json
import requests

api_key = '733fa628f2c2813c263501118e80e79c'

endpoint = 'https://api.stlouisfed.org/fred/releases'

params = {
'api_key': api_key,
'file_type': 'json'
            }

response = requests.get(endpoint,params=params)

resp = json.loads(response.text)

for i in resp['releases']:
    print(i['name'])
# %%
