# Проект backend_community_homework
## _Описание_
Создано и зарегистрировано приложение **Posts**.  
Подключена база данных.   
Десять последних записей выводятся на главную страницу.

В админ-зоне доступно управление объектами модели **Post**:       
можно публиковать новые записи или редактировать/удалять существующие.       
Пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы.

### Модели (models.py)
**Post** (запись)
| Название	| Имя поля	| Тип поля|
| ------ | ------ | ------ |
|Текст	|text	|Текст|
|Дата публикации	|pub_date|	Дата (автоматически добавляется текущая дата)|
|Автор	|author	|Ссылка на модель User (связь «один-ко-многим»)|
|Сообщество	|group	|Ссылка на модель Group (связь «один-ко-многим»)|

**Group** (сообщество)
|Название|	Имя поля|	Тип поля
| ------ | ------ | ------ |
|Имя	|title	|Строка|
|Адрес|	slug	|Поле типа slug|
|Описание	|description	|Текст|
|__str__	|	|Метод **__str__** возвращает имя сообщества (title)|

## Технологии
- Python 3.7.9
- Django 2.2.16
- Django Rest Framework 3.12.4
- Pytest 6.2.4

## Установка
1. **Клонируйте репозиторий:**
```sh
git clone https://github.com/Chuvichkin/hw02_community.git
```

2. **Cоздать и активировать виртуальное окружение:**
```sh
python -m venv venv
source venv/Scripts/activate
```

3. **Обновить pip и установить зависимости из файла requirements.txt:**
```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. **Выполнить миграции:**
```sh
cd yatube
python manage.py migrate
```

5. **Создать суперпользователя:**
```sh
python manage.py createsuperuser
```

6. **Проверка тестов:**
```sh
pytest
```

7. **Запустить проект:**
```sh
python manage.py runserver
```
Сервер запущен на странице:     
http://localhost:8000       

## Автор проекта

Чувычкин Сергей.
