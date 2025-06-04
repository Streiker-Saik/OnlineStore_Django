# Проект "Приложение онлайн магазина с помощью Django"

- [Описание](#описание)
- [Проверить версию Python](#проверить-версию-python)
- [Установка Poetry](#установка-poetry)
- [Установка](#установка)
- [Запуск проекта](#запуск-проекта)
- [Структура проекта](#структура-проекта)
- [APP](#app)
- - [catalog](#catalog)
- - - [home](#home)
- - - [contact](#contact)
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
poetry add python-dotenv psycopg2
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
|   ├── migrations/
|   |   └── __init__.py
|   ├── templates/ #шаблоны html
|   |   └── catalog/
|   |   |   ├── contact.html
|   |   |   └── home.html
|   ├── __init__.py
|   ├── admin.py
|   ├── apps.py
|   ├── models.py
|   ├── tests.py
|   └── urls.py
|   └── views.py
├── config/
|   ├── __init__.py
|   ├── asgi.py
|   ├── settings.py
|   ├── urls.py
|   └── wsgi.py
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

# APP:
## catalog
### home
```
GET: Шаблон HTML главной страницы
```
### contact
```
GET: Шаблон HTML страницы контактов
POST: Возвращает сообщение при успешном отправке данных из формы
```

## Тестирование:
Этот проект использует pytest для тестирования. Чтобы запустить тесты, выполните следующие шаги:

- Запустите тесты с помощью команды:
```bash
pytest
```
- Для получения подробного отчета о тестировании запустите:
```bash
pytest -v
```
- Запустите mypy для проверки типов:
```
mypy "ваш_скрипт".py
```