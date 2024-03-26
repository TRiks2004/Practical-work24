from .connection import BaseModel

from peewee import AutoField, CharField, TextField

from typing import Iterable


class ArtsModel(BaseModel):
    id_art = AutoField(primary_key=True)
    hieroglyph = CharField()
    name = CharField()
    quote = TextField()
    pathImage = CharField()
    
    @classmethod
    def get_all_rows(cls):
        model = super(ArtsModel, cls).get_all_rows()
        
        return [
            ArtsModel(
                id_art=model.id_art,
                hieroglyph=model.hieroglyph,
                name=model.name,
                quote=model.quote,
                pathImage=f'static\icons\{model.pathImage}'
            ) for model in model
        ]



def get_models() -> Iterable[BaseModel]:
    return [ArtsModel]
