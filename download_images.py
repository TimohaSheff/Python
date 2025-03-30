import requests
import os

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)

# Создаем директорию, если её нет
os.makedirs('test_site/static/images', exist_ok=True)

# Список изображений для скачивания
images = [
    ('https://img.freepik.com/free-photo/traditional-ukrainian-russian-borscht-on-a-blue-background-top-view-copy-space_187166-4221.jpg', 'test_site/static/images/borsch.jpg'),
    ('https://img.freepik.com/free-photo/dumplings-meat-on-a-white-plate_2829-20110.jpg', 'test_site/static/images/pelmeni.jpg'),
    ('https://img.freepik.com/free-photo/baked-mushrooms-with-cheese-in-a-ceramic-form_2829-19664.jpg', 'test_site/static/images/julienne.jpg')
]

# Скачиваем каждое изображение
for url, filename in images:
    download_image(url, filename)
    print(f'Downloaded {filename}') 