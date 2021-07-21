# YaTube API v.1

## Описание

API позволяет получать и редактировать информацию о публикациях, комментариях, группах и подписках сервиса YaTube.

Документация доступна по адресу: http://localhost:8000/redoc/

## Установка

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/hardkoro/api_final_yatube.git
```

```bash
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```bash
python -m venv venv
```

```bash
source venv/source/activate
```

Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

Выполнить миграции:

```bash
python manage.py migrate
```

Запустить проект:

```bash
python manage.py runserver
```

## Примеры

### Создание публикации:

Запрос:

```
POST /api/v1/posts/
```

```
curl -i -H 'Accept: application/json' -d 'text=test' http://localhost:8000/api/v1/posts/
```

Ответ:

```
{
    "id": 1,
    "author": "hardkoro",
    "text": "test",
    "pub_date": "2021-07-21T17:02:23.783149Z",
    "image": null,
    "group": null
}
```

### Получение публикаций:

Запрос:

```
GET /api/v1/posts/
```

```
curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/posts/
```

Ответ:

```
[
    {
        "id": 1,
        "author": "hardkoro",
        "text": "test",
        "pub_date": "2021-07-21T17:14:04.538150Z",
        "image": null,
        "group": null
    }
]
```

### Добавление комментария к публикации: 

Запрос:

```
POST /api/v1/posts/1/comments/
```

```
curl -i -H 'Accept: application/json' -d 'text=test&post=1' http://localhost:8000/api/v1/posts/1/comments/
```

Ответ:

```
HTTP/1.1 201 Created
Date: Wed, 21 Jul 2021 17:14:46 GMT
Status: 201 Created
Content-Type: application/json
Content-Length: 91

{
    "id": 1,
    "author": "hardkoro",
    "text": "test",
    "created": "2021-07-21T17:14:45.671229Z",
    "post": 1
}
```

