import requests

"""
Скрипт делает запрос к https://fakerapi.it/api/v1/
В качестве аргументов может принимать следующие параметры:
    -resources — ресурс (тексты, адреса, компании и т.д.) Является обязательным параметром.
    -quantity - общий параметр для всех ресурсов. Означает ожидаемое кол-во строк в содержимом ответа. Не обязательный параметр, по умолчанию 10.
    -locale - общий параметр. Означает язык в содержимом ответа. Не обязательный параметр, по умолчанию "en_EN".
    -**kwargs - для определенных под раздел параметров. Все параметры можно увидеть: https://fakerapi.it/en
Проверяет, что полученные ответ содержит положительный код состояния.
Возвращает список кортежей (тело ответа, без кода состояния).
"""
class ReqAPI:

    def __init__(self, resources, quantity=10, locale="en_EN", **kwargs):
        self.resources = resources
        self.quantity = quantity
        self.locale = locale
        self.kwargs = kwargs

    def get_method(self):
        url = "https://fakerapi.it/api/v1/" + self.resources
        query = {"_quantity": self.quantity, "_locale": self.locale}

        if self.kwargs:
            query = {**query, **self.kwargs}

        response = requests.get(url, params=query)

        assert response.ok
        return response.json()["data"]

if __name__ == "__main__":
    quantity = input("Введите значение для параметра 'quantity': ")
    print(ReqAPI("texts", 1, "ru_RU",).get_method())