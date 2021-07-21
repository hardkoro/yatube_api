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

### Получение публикаций:

Запрос:

```
GET http://localhost:8000/api/v1/posts/
```

Ответ:

```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2019-08-24T14:15:22Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

### Добавление комментария к посту: 

Запрос:

```
POST http://localhost:8000/api/v1/posts/{post_id}/comments/
```

Ответ:

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

