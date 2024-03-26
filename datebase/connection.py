from peewee import SqliteDatabase, Model

from typing import Iterable, TypeVar, Type

sqlite_db = SqliteDatabase(
    "datebase/base.db",
    pragmas={"journal_mode": "wal", "cache_size": -1024 * 64},
)

ModelType = TypeVar('ModelType', bound=Model)

class BaseModel(Model):
    """
    Базовая модель для всех моделей в базе данных.
    """

    class Meta:
        """
        Настройки метаданных модели.
        """
        database = sqlite_db
        """
        База данных, к которой привязана эта модель.
        """

    @classmethod
    def get_all_rows(cls: Type[ModelType]) -> Iterable[ModelType]:
        """
        Получить все строки из таблицы, соответствующей данной модели.
        
        Возвращает итератор с экземплярами модели.
        
        :return: Итератор с экземплярами модели.
        :rtype: Iterable[BaseModel]
        """
        return list(cls.select())


def __create_table(model: BaseModel):
    if not model.table_exists():
        print(f"Creating table {model.__name__}.")
        model.create_table(safe=True)
    else:
        print(f"Table {model.__name__} already exists.")


def create_tables(models: Iterable[BaseModel]):
    for model in models:
        __create_table(model)
