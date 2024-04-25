from peewee import *
from settings import *

from names import get_names_man, get_names_woman

# Подключаемся к базе Postgres
db = PostgresqlDatabase(database=DB_DATABASE, 
                        host=DB_HOST, 
                        user=DB_USER, 
                        password=DB_PASSWORD)

# Описываем модели для БД
class names_man(Model):
    name = CharField()

    class Meta:
        database = db

class names_woman(Model):
    name = CharField()

    class Meta:
        database = db

db.connect()
if not db.table_exists([names_man, names_woman]):
    db.create_tables([names_man, names_woman])
    names_man.insert_many(get_names_man()).execute()
    names_woman.insert_many(get_names_woman()).execute()
db.close()