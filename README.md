# vk.darklorian.ru
# Setup
Required Python 3.8+

Порядок действий: (Следующий гайд подразумевает что у вас установлен Python 3.8 и venv)
1. Зайти в virtual environment

```python -m venv venv```

```source venv/bin/activate```

2. Загрузить проект в локальный репозиторий (папку)

3. Инициализировать виртуальную среду и установить все необоходимые библиотеки

```pip install -r requirements.txt```

3. Запустить проект

```python manage.py runserver```


Все URLы будут вам доступны при условии наличия базы данных.
# Urls
## POST: http://vk.darklorian.ru/getphotos/

Need params: { album_id, owner_id }

Загружает фотографии из альбома при указании его album_id и owner_id

GET: http://vk.darklorian.ru/getphotos/
-----
Need params: { }

Отображает все фото и данные о них

POST: http://vk.darklorian.ru/best 
-----

Need params: { id }

Выбирает новое фото, которое будет приоритетно показываться

GET: http://vk.darklorian.ru/best
-----
Need params: { }

Показывает какое фото выбрано лучшим
POST: http://vk.darklorian.ru/dislike
-----
Need params: { id }

Убирает 1 лайк 

POST: http://vk.darklorian.ru/like
-----
Need params: { id }

Ставит выбранной записи 1 лайк

GET: http://vk.darklorian.ru/feed
-----
Need params: { }

Показывает 1 запись при 1 обращении

-----

#### От автора
Среди файлов есть шаблон POSTMAN, который можно сразу применить для тестирования.

Из дебага специально не вывел, чтобы проверяющие видели какие urls есть.
