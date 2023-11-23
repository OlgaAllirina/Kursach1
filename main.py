from Class_YA import YA
from getVKid import VK


if __name__ == '__main__':

    # запрашиваем у пользователя необходимые параметры:
    token = input("Введите Yandex token: ")
    name_file = input("Введите имя папки на YandexDisk: ")
    access_token = input("Введите токен ВК: ")
    owner_id = input("Введите id пользователя ВК: ")

    # создаём экземпляр класса VK:
    vk_user = VK(access_token)
    # получаем словарик по выгруженным фоткам из вк + json файл с информацией о фото
    vk_user.profile_photos(owner_id)
    # создаём экземпляр класса Yandex:
    ya_user = YA(token, name_file)
    # создаём папку на YandexDisk
    ya_user.create_file()
    # отправляем полученные фото в папку на YandexDisk
    ya_user.files_upload(vk_user.profile_photos(owner_id))


