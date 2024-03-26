from .connection import BaseModel

from peewee import AutoField, CharField, TextField

from typing import Iterable


class ArtsModel(BaseModel):
    id_art = AutoField(primary_key=True)
    hieroglyph = CharField()
    name = CharField()
    quote = TextField()
    pathImage = CharField()


def get_models() -> Iterable[BaseModel]:
    return [ArtsModel]
