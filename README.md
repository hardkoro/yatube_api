# YaTube API

## Description

YaTube API allows to retrieve & edit data on YaTube service — a social network for diaries / blogs

## Technology Stack

[![Python](https://img.shields.io/badge/-Python-464646??style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://www.django-rest-framework.org/)
[![Djoser](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://github.com/sunscrapers/djoser)
[![GitHub](https://img.shields.io/badge/-GitHub-464646??style=flat-square&logo=GitHub)](https://github.com/)

- Python
- Django
- Django REST Framework
- Djoser
- GitHub

## Deployment

- Clone repo and change directory to the cloned repo:

  ```bash
  git clone https://github.com/hardkoro/yatube_api.git
  ```

  ```bash
  cd yatube_api
  ```

- Create & activate virtual environment:

  ```
  python3 -m venv venv
  ```

  ```
  . venv/bin/activate/
  ```
  
- Install dependencies:

  ```
  pip install -r requirements.txt
  ```
  
- Migrate:

  ```
  python3 /yatube/manage.py migrate
  ```
  
- Run server:

  ```
  python3 /yatube/manage.py runserver
  ```

Documentation will be available at: http://localhost:8000/redoc/
  
## Examples

### Create post:

  Request:

    ```
    POST /api/v1/posts/
    ```

    ```
    curl -i -H 'Accept: application/json' -d 'text=test' http://localhost:8000/api/v1/posts/
    ```

  Response:

    ```
    HTTP/1.1 201 Created
    Date: Wed, 21 Jul 2021 17:10:04 GMT
    Status: 201 Created
    Content-Type: application/json
    Content-Length: 109
    
    {
        "id": 1,
        "author": "hardkoro",
        "text": "test",
        "pub_date": "2021-07-21T17:14:04.538150Z",
        "image": null,
        "group": null
    }
    ```

### Get posts:

  Request:

    ```
    GET /api/v1/posts/
    ```

    ```
    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/posts/
    ```

  Response:

    ```
    HTTP/1.1 200 OK
    Date: Wed, 21 Jul 2021 17:12:24 GMT
    Status: 200 OK
    Content-Type: application/json
    Content-Length: 109
    
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

### Add comment to the post: 

  Request:

    ```
    POST /api/v1/posts/1/comments/
    ```

    ```
    curl -i -H 'Accept: application/json' -d 'text=test&post=1' http://localhost:8000/api/v1/posts/1/comments/
    ```

  Response:

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

## Author 

[Evgeny Korobkov](https://github.com/hardkoro/)
