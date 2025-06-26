# Проект "Приложение онлайн магазина с помощью Django"

- [Описание](#описание)
- [Проверить версию Python](#проверить-версию-python)
- [Установка Poetry](#установка-poetry)
- [Установка](#установка)
- [Запуск проекта](#запуск-проекта)
- [Структура проекта](#структура-проекта)
- [Приложение blog](#приложение-blog)
  - [Admin blog](#admin-blog)
    - [BlogPostAdmin](#blogpostadmin)
  - [Models blog](#models-blog)
    - [Model_BlogPost](#model_blogpost)
  - [Urls blog](#urls-blog)
  - [Views blog](#views-blog)
    - [BlogPostCreateView](#blogpostcreateviews)
    - [BlogPostDeleteViews](#blogpostdeleteviews)
    - [BlogPostDetailViews](#blogpostdetailviews)
    - [BlogsPostListViews](#blogpostlistviews)
    - [BlogPostUpdateViews](#blogpostupdateviews)
- [Приложение catalog](#приложение-catalog)
  - [Admin catalog](#admin-catalog)
    - [CategoryAdmin](#categoryadmin)
    - [ProductAdmin](#productadmin)
    - [ContactAdmin](#contactadmin)
  - [Forms catalog](#forms-catalog)
    - [ProductForm](#productform)
  - [Models catalog](#models-catalog)
    - [Model_Category](#model_category)
    - [Model_Product](#model_product)
    - [Model_Contact](#model_contact)
  - [Urls catalog](#urls-catalog)
  - [Views catalog](#views-catalog)
    - [ProductsListViews](#productslistviews)
    - [ContactsCreateView](#contactscreateview)
    - [ProductDetailViews](#productdetailviews)
    - [ProductCreateViews](#productcreateviews)
    - [ProductUpdateViews](#productupdateviews)
    - [ProductDeleteView](#productdeleteview)
  - [Кастомные команды](#кастомные-команды)

   
## Описание:

Разработка приложения(веб-сайта) онлайн магазина и блога, с помощью фреймворка Django.

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
├── blog/ # приложение блог
|   ├── migrations/ # пакет миграции моделей
|   |   ├── 0001_initial.py
|   |   ├── ...
|   |   └── __init__.py
|   ├── templates/ # шаблоны html
|   |   └── blog/
|   |   |   ├── base.html # базовый шаблон
|   |   |   ├── blogpost_confirm_delete.html # форма удаления
|   |   |   ├── blogpost_detail.html # форма детальной информации о посте
|   |   |   ├── blogpost_form.html # форма создания и редоктирования
|   |   |   ├── blogpost_list.html # форма списка постов
|   |   |   └── header.html # верхняя часть страницы(меню)
|   ├── __init__.py
|   ├── admin.py # регистрация моделе в админке
|   ├── apps.py
|   ├── models.py # модели БД
|   ├── tests.py 
|   └── urls.py # маршрутизация приложения
|   └── views.py # конструктор контроллеров
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
|   |   |   ├── base.html # базовый шаблон
|   |   |   ├── contact.html
|   |   |   ├── footer.html # нижняя часть страницы
|   |   |   ├── header.html # верхняя часть страницы(меню)
|   |   |   ├── home.html
|   |   |   ├── product_confirm_delete.html # шаблон для удаления прлодукта
|   |   |   ├── product_detail.html # шаблон для детальной информации о продукте
|   |   |   └── product_form.html # шаблон для создания/изменения продукта
|   ├── templatetags/ 
|   |   └── my_tags.py
|   ├── __init__.py
|   ├── admin.py # регистрация моделе в админке
|   ├── apps.py
|   ├── forms.py # формы
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
|   └── images/
|   |   └── ...
|   └── preview/
|   |   └── ...
├── static/
|   ├── css/
|   |   └── ...
|   └── js/
|   |   └── ...
├── .env
├── .flake8 # настройка для flake8
├── .gitignore
├── blogpost_fixture.json # фикстура blog.BlogPost
├── category_fixture.json # фикстура catalog.Category
├── manage.py
├── poetry.lock
├── product_fixture.json # фикстура catalog.Product
├── pypproject.toml # зависимости для poetry
├── README.md
└── requirements.txt # ависимости для pip
```

---
# Приложение blog:
## Admin blog
### BlogPostAdmin
Класс для работы администратора с постами блога
- Вывод на дисплей: **id**, **title**(заголовок), **content**(содержание), **publication**(опубликовано) и 
**views_count**(количество просмотров)
- Фильтрация по **publication**(опубликовано) и **views_count**(количество просмотров)
- Поиск по **title**(заголовок) и **content**(содержание)
- Сортировка по **created_at**(дата и время создания)


## Models blog
- **BlogPost**: Модель представляющая пост блога
### Model_BlogPost
- **title**: Заголовок
- **content**: Содержание
- **preview**: Превью(изображение)
- **created_at**: Дата и время создания продукта
- **publication**: Признак публикации
- **views_count**: Количество просмотров


## Urls blog:
- **Страница блогов:** 
http://127.0.0.1:8000/blogs/
- **Страница Добавление блога:**
http://127.0.0.1:8000/blogs/create/
- **Страница просмотра детальной информации о блоге**
http://127.0.0.1:8000/blogs/(pk)>/detail/
  - где (pk) - это, целое число PrimaryKey, ID поста
- **Страница изменение блога:**
http://127.0.0.1:8000/blogs/(pk)>/edit/
  - где (pk) - это, целое число PrimaryKey, ID поста
- **Страница удаление блога:**
http://127.0.0.1:8000/blogs/(pk)>/delete/
  - где (pk) - это, целое число PrimaryKey, ID поста


## Views blog
### BlogPostCreateView:
Класс отвечающий за создание поста.
После успешного создания блога переадресует на список блогов.
### BlogPostDeleteViews:
Класс отвечающий за удаление поста.
После успешного удаления пользователя перенаправляет на список блогов.
### BlogPostDetailViews:
Класс отвечающий за получение детальной информации о посте.
При заходе пользователя на страницу, увеличивает количество просмотров.
### BlogsPostListViews:
Класс отвечающий за предоставление списка постов.
Отображает список блогов в шаблоне blogpost_list.html с пагинацией.
Отображения блогов - только опубликованные (publication=True)
### BlogPostUpdateViews:
Класс отвечающий за изменение поста.
После удачного изменения переходит на детальную информацию о посте.

---
# Приложение catalog:
## Admin catalog
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


## Forms catalog
### ProductForm
Форма для создания и редактирования продукта.
Инициализация стилизации форм с подсказками.
Включает в себя валидации:
- запрещает использование определенных слов в name и description
- запрещает цене быть отрицательной
- запрещает загружать файлы не форматов JPG/PNG и с размером больше 5 МБ

## Models catalog
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


## Urls catalog
- **Главная страница:** http://127.0.0.1:8000/
- **Страница для администратора:** http://127.0.0.1:8000/admin/
- **Cтраница контактов:** http://127.0.0.1:8000/contacts/ 
- **Страница информации о продукте:** http://127.0.0.1:8000/product/(pk)/detail/
  - где (pk) - это, целое число PrimaryKey, ID продукта
- **Страница добавления продукта:** http://127.0.0.1:8000/create/
- **Страница изменения продукта:** http://127.0.0.1:8000/product/(pk)/edit/
  - где (pk) - это, целое число PrimaryKey, ID продукта
- **Страница удаления продукта:** http://127.0.0.1:8000/product/(pk)/delete/
  - где (pk) - это, целое число PrimaryKey, ID продукта


## Views catalog:
### ProductsListViews:
Класс отвечающий за представление списка продукта.
Отображает список продуктов в шаблоне home.html с пагинацией.
Порядок отображения продуктов - от нового к старому (по полю updated_at)
### ContactsCreateView:
Класс отвечающий за создание контактов.
Позволяет пользователям отправлять свои контактные данные через форму, а также сохраняет их в модели Contact. 
После успешного создания перенаправляет на страницу контактов.
### ProductDetailViews:
Класс отвечающий за получение детальной информации о продукте.
Отображает полные данные о выбранном продукте в шаблоне product_detail.html.
Добавляет информацию о категории продукта в контекст.
### ProductCreateViews:
Класс отвечающий за создание продукта.
Позволяет пользователям добавлять новые продукты через форму. 
После успешного создания перенаправляет на главную страницу.
## ProductUpdateViews:
Класс отвечающий за изменения продукта.
Позволяет пользователям редактировать продукты через форму.
После успешного создания перенаправляет на детальную информацию о продукте.
## ProductDeleteView:
Класс отвечающий за удаление продукта
После успешного удаления перенаправляет на список блогов.


## Кастомные команды
### add_product
Команда для добавления продуктов из fixture
- 'category_fixture.json'
- 'product_fixture.json'
```bash
python manage.py add_products
```