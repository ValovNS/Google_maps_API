import requests

class PostGetloc():

    def check_status_code(self, result, method,
                          check_type):  # Функция, которая получает результат запроса и тип проверки, проверяет статус-код
        print(f"Статус-код метода {method} на {check_type}: {result.status_code}")
        assert result.status_code == 200, "ОШИБКА, Статус-код некорректен"

    def check_place_id(self,result): # Функция, которая проверяет наличие place_id в ответе и выводит его
        assert 'place_id' in result
        print(f"Поле place_id присутствует в теле ответа: {result.get("place_id")}")

    def post_new_location(self):  # Функция, которая добавляет локацию
        base_url = 'https://rahulshettyacademy.com'    # базовая url
        key = '?key=qaclick123'                  # ключ допуска
        post_resourse = '/maps/api/place/add/json'     # путь метода post

        post_url = base_url + post_resourse + key
        print(post_url)
        json_new_location = {                          # тело запроса post
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                }, "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": [
                    "shoe park",
                    "shop"
                ],
                "website": "http://google.com",
                "language": "French-IN"
            }


        result_post = requests.post(post_url, json=json_new_location)     # отправка запроса post, который включает url и тело запроса
        self.check_status_code(result_post, "POST", "добавление локации")
        return result_post.json()

    def five_loc_in_file(self):  # Функция, которая записывает 5 новых локаций в файл и проверяет наличие place_id
        count = 1
        while count <= 5:
            loc = self.post_new_location()
            print(f"Тело ответа: {loc}")
            self.check_place_id(loc)
            with open("place_id", 'a') as file:
                file.write(f'{loc.get("place_id")}\n')
            count +=1

    def get_new_location(self):  # Функция, которая считывает place_id из файла, подставляет его в url, проверяет статус код
        base_url = 'https://rahulshettyacademy.com'  # базовая url
        key = '?key=qaclick123'  # ключ допуска
        get_resourse = '/maps/api/place/get/json'  # путь метода get

        with open('place_id', 'r') as file:
            lines = file.readlines()
            for line in lines[:5]:
                line = line.strip()
                print (f"\nПоле place_id: {line}")
                get_url = base_url + get_resourse + key + '&place_id=' + line
                result_get = requests.get(get_url)
                print(result_get.json())
                self.check_status_code(result_get, "GET", "существование локации")



response = PostGetloc()
response.five_loc_in_file()
response.get_new_location()
