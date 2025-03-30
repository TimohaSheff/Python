from django.shortcuts import render

def index(request):
    context = {
        "page_title": "Ресторан 'Русская кухня'",
        "restaurant_name": "Добро пожаловать в ресторан 'Русская кухня'",
        "menu_items": [
            {
                "name": "Борщ",
                "photo": "images/b.jpg",
                "ingredients": ["Свекла", "Капуста", "Морковь", "Картофель", "Говядина"],
                "details": {
                    "spicy": False,
                    "cooking_time": 120,
                    "price": 350,
                    "vegetarian": False
                }
            },
            {
                "name": "Пельмени",
                "photo": "images/p.jpg",
                "ingredients": ["Мясной фарш", "Тесто", "Лук", "Специи"],
                "details": {
                    "spicy": False,
                    "cooking_time": 30,
                    "price": 400,
                    "vegetarian": False
                }
            },
            {
                "name": "Грибной жульен",
                "photo": "images/g.jpg",
                "ingredients": ["Грибы", "Сливки", "Сыр", "Лук"],
                "details": {
                    "spicy": False,
                    "cooking_time": 25,
                    "price": 320,
                    "vegetarian": True
                }
            }
        ]
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def achievements(request):
    context = {
        "achievements": [
            {
                "year": 2020,
                "award": "Лучший новый ресторан",
                "category": "Открытие года",
                "description": "Премия журнала 'Гастроном' за лучший ресторан русской кухни"
            },
            {
                "year": 2021,
                "award": "Народный выбор",
                "category": "Традиционная кухня",
                "description": "Победитель в номинации 'Лучший ресторан традиционной кухни' по версии городского портала"
            },
            {
                "year": 2022,
                "award": "Золотая вилка",
                "category": "Качество обслуживания",
                "description": "Награда за высочайший уровень сервиса и качество обслуживания"
            },
            {
                "year": 2023,
                "award": "Звезда гастрономии",
                "category": "Аутентичность",
                "description": "Признание за сохранение традиционных рецептов русской кухни"
            }
        ]
    }
    return render(request, "achievements.html", context)

def pinterest_cards(request):
    return render(request, 'pinterest_cards.html')

# Create your views here.
