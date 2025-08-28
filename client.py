import requests

# URL Вашего API
base_url = 'http://127.0.0.1:5000/ads'

# Список объявлений для создания
ads_to_create = [
    {
        'title': 'Объявление 1',
        'description': 'Описание 1',
        'created_at': '2023-10-01',
        'owner': 'Владелец 1'
    },
    {
        'title': 'Объявление 2',
        'description': 'Описание 2',
        'created_at': '2023-10-02',
        'owner': 'Владелец 2'
    },
    {
        'title': 'Объявление 3',
        'description': 'Описание 3',
        'created_at': '2023-10-03',
        'owner': 'Владелец 3'
    }
]

# 1. Создание нескольких объявлений (POST)
for ad in ads_to_create:
    response_post = requests.post(base_url, json=ad)
    print('POST статус-код:', response_post.status_code)  # Выводим статус-код ответа
    print()
    print('POST ответ:', response_post.json())             # Выводим текст ответа
    print()

# 2. Получение всех объявлений (GET)
response_get = requests.get(base_url)
print('GET статус-код:', response_get.status_code)    # Выводим статус-код ответа
print()
print('GET ответ:', response_get.json())               # Выводим текст ответа в формате JSON
print()

# 3. Получение конкретного объявления (GET)
ad_id = 1  # Замените на ID объявления, которое хотите получить
response_get_single = requests.get(f'{base_url}/{ad_id}')
print('GET (одиночное) статус-код:', response_get_single.status_code)  # Выводим статус-код ответа
try:
    response_data = response_get_single.json()  # Попытка декодирования JSON
    print('GET (одиночное) ответ:', response_data)  # Выводим текст ответа в формате JSON
except requests.exceptions.JSONDecodeError:
    print('Ошибка декодирования JSON:', response_get_single.text)  # Выводим текст ответа, если это не JSON
print()

# 4. Удаление объявления (DELETE)
response_delete = requests.delete(f'{base_url}/{ad_id}')
print('DELETE статус-код:', response_delete.status_code)  # Выводим статус-код ответа

# Обработка JSON-ответа
if response_delete.status_code == 200:
    response_data = response_delete.json()  # Парсим JSON-ответ
    print('DELETE ответ:', response_data.get('message', 'Нет сообщения'))  # Выводим сообщение
else:
    print('Ошибка при удалении:', response_delete.text)  # Выводим текст ошибки