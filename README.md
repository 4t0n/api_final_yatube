# YatubeAPI

## Описание проекта

Yatube API — это REST API на Django Rest Framework (DRF) для создания, обновления и удаления постов. С помощью него пользователи могут просматривать посты, оставлять комментарии и подписываться друг на друга.

### Основные функции:

-  **Создание, обновление и удаление постов.** Пользователи могут добавлять информацию о своих постах, включая текст, изображения и другие метаданные.
-  **Подразделение на группы.** Посты могут быть сгруппированы по различным группам. Это позволяет пользователям легко находить интересующие их посты.
-  **Комментарии.** Пользователи могут оставлять комментарии к постам. Это может быть полезно для обсуждения содержания поста, выражения своего мнения или просто общения с другими пользователями.
-  **Система подписок.** Пользователи могут подписываться на других пользователей.

## Установка

Для установки и запуска API необходимо выполнить следующие шаги:

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/4t0n/api_final_yatube.git
```

```
cd api_final_yatube
```

2. Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

3. Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

4. Выполнить миграции:

```
python3 manage.py migrate
```

5. Запустить проект:

```
python3 manage.py runserver
```

## Примеры

Вот несколько примеров запросов к API:

-  GET /api/v1/posts — получить список всех постов.
-  POST /api/v1/posts — создать новый пост.

Пример запроса:

```
  {
      "text": "string",
      "image": "string",
      "group": 1
  }
```

-  DELETE /api/v1/posts/{id} — удалить существующий пост.
-  GET /api/v1/posts/{id} — получить информацию о посте.
-  GET /api/v1/posts/{post_id}/comments — получить список всех комментариев поста.
-  POST /api/v1/posts/{post_id}/comments — создать новый комментарий к посту.

Пример запроса:

```
  {
      "text": "string"
  }
```

-  DELETE /api/v1/posts/{post_id}/comments/{id} — удалить комментарий.
-  GET /api/v1/groups — получить список всех групп.
-  POST /api/v1/follow — подписаться на пользователя.

Пример запроса:

```
  {
      "following": "string"
  }
```

Более подробную информацию можно найти в документации API.