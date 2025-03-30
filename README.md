# Ресторан "Русская кухня"

Веб-приложение ресторана русской кухни, разработанное на Django.

## Функциональность

- Главная страница с меню ресторана
- Страница "О нас" с информацией о ресторане
- Страница достижений и наград
- Страница с карточками блюд в стиле Pinterest

## Технологии

- Python 3.x
- Django
- HTML/CSS
- Git

## Установка и запуск

1. Клонировать репозиторий:
```bash
git clone [URL репозитория]
```

2. Создать и активировать виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

3. Установить зависимости:
```bash
pip install django
```

4. Выполнить миграции:
```bash
python manage.py migrate
```

5. Запустить сервер разработки:
```bash
python manage.py runserver
```

## Структура проекта

- `test_site/` - основное приложение
  - `templates/` - HTML шаблоны
  - `static/` - статические файлы (CSS, изображения)
  - `views.py` - представления
- `Shevkunov_Timofey/` - настройки проекта 