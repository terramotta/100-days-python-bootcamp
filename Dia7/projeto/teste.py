import requests
import json

response = requests.get("https://random-word-api.herokuapp.com/word")
print(type(response.json()))

for content in response.json().lower():
    print(content)


#pylint: disable-all