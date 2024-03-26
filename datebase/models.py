from .connection import BaseModel

from peewee import AutoField, CharField, TextField

from typing import Iterable


class ArtsModel(BaseModel):
    """Модель данных для представления в базе данных "Arts"."""
    
    id_art = AutoField(primary_key=True)
    """Автоматически присваиваемый первичный ключ."""
    
    hieroglyph = CharField()
    """Поле для хранения иероглифа."""
    
    name = CharField()
    """Поле для хранения имени."""
    
    quote = TextField()
    """Поле для хранения цитаты."""
    
    pathImage = CharField()
    """Поле для хранения пути к изображению."""
    
    class Meta:
        """Настройки метаданных модели."""
        table_name = 'arts'
        """Имя таблицы в базе данных."""
    
    @classmethod
    def get_all_rows(cls):
        model = super(ArtsModel, cls).get_all_rows()
        
        return [
            ArtsModel(
                id_art=model.id_art,
                hieroglyph=model.hieroglyph,
                name=model.name,
                quote=model.quote,
                pathImage=rf'static\icons\{model.pathImage}'
            ) for model in model
        ]


class AboutModel(BaseModel):
    """Модель данных для представления в базе данных "About"."""
    
    id_art = AutoField(primary_key=True)
    """Автоматически присваиваемый первичный ключ."""
    
    hieroglyph = CharField()
    """Поле для хранения иероглифа."""
    
    name = CharField()
    """Поле для хранения имени."""
    
    surname = CharField()
    """Поле для хранения фамилии."""
    
    href_git = CharField()
    """Поле для хранения ссылки на Git."""
    
    href_telegram = CharField()
    """Поле для хранения ссылки на Telegram."""
    
    href_email = CharField()
    """Поле для хранения ссылки на Email."""
    
    class Meta:
        """Настройки метаданных модели."""
        table_name = 'about'
        """Имя таблицы в базе данных."""


def get_models() -> Iterable[BaseModel]:
    """Получение списка всех моделей.
    
    Возвращает список экземпляров класса.
    """
    return [ArtsModel, AboutModel]


