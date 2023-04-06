# fred.py

import requests
import json
import pandas as pd

class Fred:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.stlouisfed.org/fred/"

    def json_series(self, series_id):
        url = self.base_url + "series/observations?series_id=" + series_id + "&api_key=" + self.api_key + "&file_type=json"
        response = requests.get(url)
        data = json.loads(response.text)
        return data
    
    def get_table(self, series_id):
        data = self.json_series(series_id)
        df = pd.json_normalize(data['observations'])
        return df

