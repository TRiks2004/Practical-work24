from .connection import BaseModel

from peewee import AutoField, CharField, TextField

class ArtsModel(BaseModel):
    id_art = AutoField(primary_key=True)
    hieroglyph = CharField()
    name = CharField()
    quote = TextField()
    pathImage = CharField()