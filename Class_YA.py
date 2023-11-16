import requests
import os
from pprint import pprint


url = "https://cloud-api.yandex.net/v1/disk/resources"
params = {
    "path": "Photo"
    }
headers = {
    "Authorization": "OAuth y0_AgAAAAByLriYAADLWwAAAADyLUAyEnmXwlZqRfiVXDcHKZBe_Dw9uck"
    }
response = requests.put(url, headers=headers, params=params)
print(response.status_code)
pprint(response.json())


class YA:
    def __init__(self, token):
        self.token = token
# create a folder on Yandex disk

    def create_file(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {
            "path" : "Photo"
        }
        headers = {
            "Authorization" : "OAuth y0_AgAAAABxRXrCAADLWwAAAADx33R5HzyPEUCNS4GM569cZCoauFy9TRg"
        }
        response = requests.put(url, headers=headers, params=params)
        print(response.status_code)


