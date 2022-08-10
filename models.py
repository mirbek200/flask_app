from peewee import *
from datetime import datetime

db = PostgresqlDatabase(
    'flask_db',
    host = 'localhost',
    port = '5432',
    user = 'flask_user',
    password = '123'
)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Post(BaseModel):
    title = CharField(max_length = 255, null = False)
    description = CharField(max_length = 255, null = False)
    date = DateField(default = datetime.now)

    def __repr__(self):
        return self.title

# db.create_tables([Post])



db.close()  