# Курсовая работа «Резервное копирование»
Возможна такая ситуация, что мы хотим показать друзьям фотографии из социальных сетей, но соц. сети могут быть недоступны по каким-либо причинам. Давайте защитимся от такого.
Нужно написать программу для резервного копирования фотографий с профиля(аватарок) пользователя vk в облачное хранилище Яндекс.Диск.
Для названий фотографий использовать количество лайков, если количество лайков одинаково, то добавить дату загрузки.
Информацию по сохраненным фотографиям сохранить в json-файл.

## Задание:
Нужно написать программу, которая будет:

Получать фотографии с профиля. Для этого нужно использовать метод photos.get.
Сохранять фотографии максимального размера(ширина/высота в пикселях) на Я.Диске.
Для имени фотографий использовать количество лайков.
Сохранять информацию по фотографиям в json-файл с результатами.
Обратите внимание: инструкция для получения токена для ВК находится в вашем личном кабинете в итоговом блоке по модулю.

## Входные данные:
Пользователь вводит:

id пользователя vk;
токен с Полигона Яндекс.Диска. Важно: Токен публиковать в github не нужно!
## Выходные данные:
json-файл с информацией по файлу:
_____________________________________________

    [{
    "file_name": "34.jpg",
    "size": "z"
    }]
___________________________________________
    
Измененный Я.диск, куда добавились фотографии.​​
## Обязательные требования к программе:
Использовать REST API Я.Диска и ключ, полученный с полигона.
Для загруженных фотографий нужно создать свою папку.
Сохранять указанное количество фотографий(по умолчанию 5) наибольшего размера (ширина/высота в пикселях) на Я.Диске
Сделать прогресс-бар или логирование для отслеживания процесса программы.
Код программы должен удовлетворять PEP8.
У программы должен быть свой отдельный репозиторий.
Все зависимости должны быть указаны в файле requiremеnts.txt.​
## Необязательные требования к программе:
Сохранять фотографии и из других альбомов.
Сохранять фотографии на Google.Drive.
