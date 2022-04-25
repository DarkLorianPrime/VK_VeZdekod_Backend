# VK_VeZdekod_Backend
# Setup
Required Python 3.8+

Порядок действий:
1. Загрузить проект в локальный репозиторий (папку)

3. Инициализировать виртуальную среду и установить все необоходимые библиотеки

```pip install -r requirements.txt```

3. Запустить проект

```python manage.py runserver```


Все URLы будут вам доступны при условии наличия базы данных.
# Urls
```shell

{ http://vk.darklorian.ru/getphotos/ }

Description:

{ Загружает фотографии из альбома при указании его album_id и owner_id }

Params:

{ album_id, owner_id }

Method:

{ POST }
```
-----
```shell

{ http://vk.darklorian.ru/getphotos/ }

Description:

{ Отображает все фото и данные о них }

Params:

{ }

Method:

{ GET }
```
-----
```shell

{ http://vk.darklorian.ru/best }

Description:

{ Выбирает новое фото, которое будет приоритетно показываться }

Params:

{ id - id записи. }

Method:

{ POST }
```
-----
```shell

{ http://vk.darklorian.ru/best }

Description:

{ Показывает какое фото выбрано лучшим }

Params:

{ }

Method:

{ GET }
```
-----
```shell

{ http://vk.darklorian.ru/dislike }

Description:

{ Убирает 1 лайк }

Params:

{ id - id записи. }

Method:

{ POST }
```
-----
```shell

{ http://vk.darklorian.ru/like }

Description:

{ Ставит 1 лайк }

Params:

{ id - id записи. }

Method:

{ POST }
```
-----
```shell

{ http://vk.darklorian.ru/feed }

Description:

{ Показывает 1 запись }

Params:

{ }

Method:

{ GET }
```
-----

#### От автора
Среди файлов есть шаблон POSTMAN, который можно сразу применить для тестирования.

Из дебага специально не вывел, чтобы проверяющие видели какие urls есть.
