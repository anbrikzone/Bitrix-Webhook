# Batch WEBHOOK для системы Битрикс 
### Пакетное обновление поля HONORIFIC ("Обращение") в контактах всех клиентов системы

## Описание
Данная программа позволяет обновить поле HONORIFIC, ответственное за обращение господин/госпожа для контактов в системе Битрикс CRM.

Проверка вида обращения происходит посредством поиска имён клиентов в базе данных (мужские и женские имена). Если имена найдены в таблице мужских имён, клиенту присваивается "Г-н" (Господин), если в таблице женских имён - "Г-жа" (Госпожа).

Используются batch-запросы, которые позволяют обновлять записи пакетами по 50 контактов за один раз.

## Особенности
Приложение позволяет обновлять не только поле "Обращение". Его легко можно исправить для обновления других полей в системе.
В программе используются следующие модули:
- request - отправка http-запросов
- peewee - ORM для работы с базой данных (в данном случае используется Postgres)
- tqdm - вывод в консоль индикатора выполнения запроса
- python-dotenv - загрузка переменных окружения из .env-файла

## Установка и запуск

Внимание. Для успешной работы приложения необходимо иметь заполненную базу данных с таблицами мужских и женских имён. 
Обновлено (25/04/2024): добавлена база мужских и женских имён

Установите Python окружение
```
python -m venv .venv
pip install -r requirements.txt
```

Создайте файл .env и заполните следующими значениями:
```
TOKEN = токен_Битрикс
BITRIX_URL = адрес_платформы

DB_HOST = адрес_сервера_БД
DB_USER = имя_пользователя
DB_PASSWORD = пароль
DB_DATABASE = база_данных
```

Запускаем приложение из консоли:
```
python -m webhook
```

## Дополнительно
Приветствуются любые замечания и предложения по улучшению кода :)
