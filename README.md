# Проект "Приложение онлайн магазина с помощью Django"

- [Описание](#описание)
- [Проверить версию Python](#проверить-версию-python)
- [Установка Poetry](#установка-poetry)
- [Установка](#установка)
- [Запуск проекта](#запуск-проекта)
- [Структура проекта](#структура-проекта)
- [Приложение catalog](#приложение-catalog)
  - [Models](#models)
    - [Model_Category](#model_category)
    - [Model_Product](#model_product)
  - [Views](#views)
    - [home](#home)
    - [contact](#contact)
- [Тестирование](#тестирование) 

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
cd "ваш-репозиторий"
```
- Установите необходимые зависимости:
```bash
poetry add python-dotenv psycopg2 pillow
poetry add --group lint flake8 black isort mypy
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
├── catalog/ #приложение каталог
|   ├── migrations/ #пакет миграции моделей
|   |   └── __init__.py
|   ├── templates/ #шаблоны html
|   |   └── catalog/
|   |   |   ├── contact.html
|   |   |   └── home.html
|   ├── __init__.py
|   ├── admin.py
|   ├── apps.py
|   ├── models.py #модели БД
|   ├── tests.py 
|   └── urls.py
|   └── views.py #конструктор
├── config/
|   ├── __init__.py
|   ├── asgi.py
|   ├── settings.py
|   ├── urls.py
|   └── wsgi.py
├── media/
|   ├── css/
|   ├── js/
├── static/
|   ├── css/
|   ├── js/
├── .env
├── .gitignore
├── manage.py
├── poetry.lock
├── pypproject.toml
└── README.md
```

# Приложение catalog:
### Models
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

## Views
### home:
- GET: Шаблон HTML главной страницы
### contact:
- GET: Шаблон HTML страницы контактов
- POST: Возвращает сообщение при успешном отправке данных из формы
