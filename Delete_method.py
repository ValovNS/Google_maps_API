import requests

class PostGetloc():

    def check_place_id(self,result):  # Функция, которая проверяет наличие place_id в ответе и выводит его
        assert 'place_id' in result
        print(f"Поле place_id присутствует в теле ответа: {result.get("place_id")}")

    def write_new_place_id(self,place_id):  # Функция, которая записывает place_id в новый файл
        with open('new_place_id', 'a') as new_file:
            new_file.writelines(f"{place_id}\n")


    def get_new_location(self):  # Функция, которая считывает place_id из файла, подставляет его в url, проверяет статус код
        base_url = 'https://rahulshettyacademy.com'  # базовая url
        key = '?key=qaclick123'  # ключ допуска
        get_resourse = '/maps/api/place/get/json'  # путь метода get
        with open('place_id', 'r') as file:
            lines = file.readlines()
            for idx, line in enumerate(lines[:5], start=1):
                line = line.strip()
                get_url = base_url + get_resourse + key + '&place_id=' + line
                result_get = requests.get(get_url)
                print(f"\nПоле place_id: {line}")
                print(result_get.json())
                check = result_get.status_code
                if check == 404:
                    print(f"Код ошибки {check} - локация не существует")
                elif check == 200:
                    self.write_new_place_id(line)
                    print(f"Статус код {check} - локация существует")


    def delete_loc(self):
        base_url = 'https://rahulshettyacademy.com'  # базовая url
        key = '?key=qaclick123'  # ключ допуска
        delete_resourse = '/maps/api/place/delete/json'

        with open('place_id', 'r') as file: # Прочитать все строки из файла
            lin = file.readlines()
            delete_url = base_url + delete_resourse + key
            json_delete_location2 = {
                "place_id": lin[1].strip()
            }
            json_delete_location4 = {
                "place_id": lin[3].strip()
            }
            result_delete2 = requests.put(delete_url, json=json_delete_location2)
            result_delete4 = requests.put(delete_url, json=json_delete_location4)




response = PostGetloc()
response.delete_loc()
response.get_new_location()