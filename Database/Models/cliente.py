from peewee import Model, CharField, DateTimeField
from Database.database import db
from datetime import datetime

class BaseModel(Model):
    class Meta:
        database = db

class Cliente(BaseModel):
    nome = CharField()
    email = CharField()
    data_registro = DateTimeField(default=datetime.now())


def conectar_banco():
    db.connect()
    db.create_tables([Cliente])