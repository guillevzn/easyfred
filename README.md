# easyfred
Easy to use Fred API with Python

This package is not inteded to substitute other (and more complete) packages to use the Fred API, but to provide an easy to use alternative. The main porpouse is to have the most simple way to use in-code documentation.

Install via pip: ```pip install easyfred```

Easy example usage:

```
import easyfred

fred = easyfred.Fred(api_key='YOUR_API_KEY')
"""
First you have to introduce your API KEY associated with you Fred account.
https://fredaccount.stlouisfed.org/apikeys
"""

fred.get_info()
"""
With get_info() you can display all available methods in the library
with their needed arguments and what will they return aech of these.
"""

data = fred.search_and_get_all_series_metadata(search_text='GDP growth spain')
"""
This is an example of how you can get a specific table by searching with keywords.
"""
```