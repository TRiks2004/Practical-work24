from peewee import *

sqlite_db = SqliteDatabase(
    'datebase/base.db', 
    pragmas={
        'journal_mode': 'wal',
        'cache_size': -1024 * 64
    }
)


# Arts
# hieroglyph - иероглиф
# name - название
# quote - цитата
# pathImage - путь к изображению


class BaseModel(Model):
    class Meta:
        database = sqlite_db


def create_table(model: BaseModel):
    if not model.table_exists():
        model.create_table(safe=True)



