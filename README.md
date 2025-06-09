# Проект "Приложение онлайн магазина с помощью Django"

- [Описание](#описание)
- [Проверить версию Python](#проверить-версию-python)
- [Установка Poetry](#установка-poetry)
- [Установка](#установка)
- [Запуск проекта](#запуск-проекта)
- [Структура проекта](#структура-проекта)
- [Приложение catalog](#приложение-catalog)
  - [Admin](#admin)
    - [CategoryAdmin](#categoryadmin)
    - [ProductAdmin](#productadmin)
  - [Models](#models)
    - [Model_Category](#model_category)
    - [Model_Product](#model_product)
    - [Model_Contact](#model_contact)
  - [Urls](#urls)
  - [Views](#views)
    - [contact](#contact)
    - [home](#home)
    - [product_detail](#product_detail)
- [Кастомные команды](#кастомные-команды)


## Описание:

Разработка приложения(веб-сайта) онлайн магазина, с помощью фреймворка Django.

## Проверить версию Python:

Убедитесь, что у вас установлен Python (версия 3.x). Вы можете проверить установленную версию Python, выполнив команду:
```
python --version
```

## Установка Poetry:
Если у вас еще не установлен Poetry, вы можете установить его, выполнив следующую команду
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
Проверить Poetry добавлен в ваш PATH.
```bash
poetry --version
```

## Установка:
- Клонируйте репозиторий:
```bash
git clone git@github.com:Streiker-Saik/OnlineStore_Django.git
```
- Перейдите в директорию проекта:
```
cd OnlineStore_Django
```
### При использовании PIP:
- Активируйте виртуальное окружение
```
python -m venv <имя_вашего окружения>
<имя_вашего_окружения>\Scripts\activate
```
- Установите зависимости
```
pip install -r requirements.txt
```
### При использование POETRY:
- Активируйте виртуальное окружение
```bash
poetry shell
```
- Установите необходимые зависимости:
```bash
poetry install
```
или
```bash
poetry add python-dotenv psycopg2 pillow
poetry add --group lint flake8 black isort mypy ipython
poetry add --group dev django
```
- Зайдите в файл .env.example и следуйте инструкция

## Запуск проекта:
Чтобы запустить сервер разработки, выполните следующую команду:
```bash
python manage.py runserver
```

## Структура проекта:
```
OnlineStore_Django/
├── catalog/ # приложение каталог
|   ├── management/ # кастомные команды
|   |   └── commands/
|   |   |   ├── __init__.py
|   |   |   └── add_products.py
|   ├── migrations/ # пакет миграции моделей
|   |   ├── 0001_initial.py
|   |   ├── ...
|   |   └── __init__.py
|   ├── templates/ # шаблоны html
|   |   └── catalog/
|   |   |   ├── contact.html
|   |   |   ├── home.html
|   |   |   └── product_detail.html
|   ├── __init__.py
|   ├── admin.py # регистрация моделе в админке
|   ├── apps.py
|   ├── models.py # модели БД
|   ├── tests.py 
|   └── urls.py # маршрутизация приложения
|   └── views.py # конструктор контроллеров
├── config/
|   ├── __init__.py
|   ├── asgi.py
|   ├── settings.py
|   ├── urls.py # маршрутизация проета
|   └── wsgi.py
├── media/
|   └── image/
├── static/
|   ├── css/
|   └── js/
├── .env
├── .gitignore
├── category_fixture.json # фикстура catalog.Category
├── manage.py
├── poetry.lock
├── product_fixture.json # фикстура catalog.Product
├── pypproject.toml
└── README.md
```


## Admin
### CategoryAdmin
Класс для работы администратора с категориями
- Вывод на дисплей: **id** и **name**(название категории)
- Поиск по **name**(имени) и **description**(описанию)
### ProductAdmin
Класс для работы администратора с продуктами
- Вывод на дисплей: **id**, **name**(название продукта), **price**(цена) и **category**(категория)
- Фильтрация по **category**(категории)
- Поиск по **name**(имени) и **description**(описанию)
### ContactAdmin
Класс для работы администратора с контактами
- Вывод на дисплей: **name**(имя человека), **phone**(контактный телефон), **message**(сообщение)
- Фильтрация по **created_at**(дате создания)
- Сортировка по **name**(имя человек)
# Приложение catalog:


## Models
- **Category**: Модель представляющая категорию
- **Product**: Модель, представляющая продукт
### Model_Category
- **name**: Название категории
- **description**: Описание категории
### Model_Product
- **name**: Наименование продукта
- **description**: Описание продукта
- **image**: Изображение продукта
- **category**: Связь с категорией, к которой принадлежит продукт
- **price**: Цена продукта
- **created_at**: Дата и время создания продукта
- **updated_at**: Дата и время последнего изменения продукта
### Model_Contact
- **name**: Имя
- **phone**: Номер телефона
- **message**: Сообщение
- **created_at**: Дата создания


## Urls:
- **Главная страница:** http://127.0.0.1:8000/ - 
- **Домашняя страниц(главная страница):** http://127.0.0.1:8000/home/
- **Cтраница контактов:** http://127.0.0.1:8000/contacts/ 
- **Страница информации о продукте:** http://127.0.0.1:8000/product_detail/(product_id)/
  - где (product_id) - это, целое число, ID продукта


## Views
### home:
- GET: Шаблон HTML главной страницы
### contact:
- GET: Шаблон HTML страницы контактов
- POST: Возвращает сообщение при успешном отправке данных из формы
Заполнение формы и отправка заполняет БД контакты
### product_detail:
- GET: Шаблон HTML информации о продукте


## Кастомные команды
### add_product
Команда для добавления продуктов из fixture
- 'category_fixture.json'
- 'product_fixture.json'
```bash
python manage.py add_products
```