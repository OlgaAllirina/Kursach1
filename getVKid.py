import requests
from datetime import datetime
import json


class VK:
    url = 'https://api.vk.com/method/photos.get'

    def __init__(self, token_vk, version='5.131'):
        self.params = {
            'access_token': token_vk,
            'v': version
        }

    def profile_photos(self, owner_id, count=5):
        '''
        Метод выгружает заданное количество фотографий со страницы пользователя,
        создаёт json файл для дальнейшей работы в классе яндекса
        owner_id — идентификационный номер владельца аккаунта ВКонтакте
        count - количество выгружаемых фото максимального размера
        '''
        self.count = count
        self.owner_id = owner_id
        profile_photos_params = {
            'owner_id': owner_id,
            'album_id': 'profile',
            'extended': True,
            'photo_sizes': True,
            'count': count
        }
        response = requests.get(self.url, params={**self.params, **profile_photos_params}).json()
        photo_info = {}
        file_json = []
        for element in response["response"]["items"]:
            # получим лайки
            likes_photo = element["likes"]["count"]
            # получим дату публикаций
            date_public = element["date"]
            # получим максимальный размер фотографий
            sort_dict = {'s': 1, 'm': 2, 'x': 3, 'o': 4, 'p': 5, 'q': 6, 'r': 7, 'y': 8, 'z': 9, 'w': 10}
            size = max(element['sizes'], key=lambda el: sort_dict[el['type']])
            letter = size['type']
            url = size['url']
            # сравниваем фотографии при одинаковом количестве лайков по дате загрузки
            if likes_photo in photo_info:
                likes_photo = f"{likes_photo} - {datetime.strftime(datetime.fromtimestamp(date_public), '%Y-%m-%d %H-%M-%S')}"
            photo_info[likes_photo] = {'letter': letter, 'url': url}
            # создадим файл json в необходимом формате
            file_json.append({"file_name": f'{likes_photo}.jpg', "size": f'{letter} pixels'})
        # запишем полученный файл в json
        with open("out_file_js.json", "a", encoding='utf-8') as js_file:
            json.dump(file_json, js_file, indent=4)
        return photo_info



