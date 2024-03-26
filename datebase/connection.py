from peewee import SqliteDatabase, Model

from typing import Iterable

sqlite_db = SqliteDatabase(
    "datebase/base.db",
    pragmas={"journal_mode": "wal", "cache_size": -1024 * 64},
)


class BaseModel(Model):
    
    @classmethod
    def get_all_rows(cls):
        return list(cls.select())
    
    class Meta:
        database = sqlite_db


def __create_table(model: BaseModel):
    if not model.table_exists():
        model.create_table(safe=True)


def create_tables(models: Iterable[BaseModel]):
    for model in models:
        __create_table(model)
