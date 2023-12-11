import requests
from tqdm import tqdm


class YA:
    def __init__(self, token, name_file):
        self.name_file = name_file
        self.token = token

# create a folder on Yandex disk
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    # создадим папку на яндекс диске
    def create_file(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {
            "path": {self.name_file}
        }
        headers = self.get_headers()
        response = requests.put(url, headers=headers, params=params)
        print(f"Статус добавления папки на яндекс диск: {response.status_code}")
        return response

    # загрузим в папку фотографии по полученному url

    def files_upload(self, photo_info):
        url_load = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()

        for file in photo_info.keys():
            for i in tqdm(str(file)):
                params = {"path": f"{self.name_file}/{file}.jpg", "url": photo_info[file]["url"]}
                response = requests.post(url_load, headers=headers, params=params)
                print(f"Статус загрузки фотографий в указанную папку: {response.status_code}")
                print("Файлы успешно загружены на диск")


