import requests


access_token = "vk1.a.dDShW-EN9G_NNxWvX7HIv6REL11azvotkUIA8HJjQkTpHB89UHjzkB_dXv9NYeR_WpnuuRnDRciNusVwHzUj4LJrPB8WNz692t-NYk_6QBNFw4-wGGdoPNJ4jX8SP7voUhP9LNnV5Nr0-TrQirYzu3qTR8LrhaRHEHnsDRz51w-MmE-r--_VLs_22lvX9ikB11fszYdt8u-ckV5S46S-6g"
user_id = "147557206"


class VK:

    def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
       url = 'https://api.vk.com/method/users.get'
       params = {'user_ids': self.id}
       response = requests.get(url, params={**self.params, **params})



    def get_photo(self, count = 5):
        self.count = count
        params = {
           "access_token": self.token,
           "v": "5.131",
           "owner_id": self.id,
           "album_id": "profile",
           "extended": True,
           "photo_sizes": True,
           "count": count
              }
        response = requests.get(f"https://api.vk.com/method/photos.get ", params=params, timeout=3).json()
        return response




vk = VK(access_token, user_id)
print(vk.users_info())

