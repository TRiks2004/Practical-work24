# Импортируем необходимые модули
import environ
import pathlib

# Импортируем базовый класс настроек из модуля pydantic_settings
from pydantic_settings import BaseSettings

# Получаем абсолютный путь к родительскому каталогу текущего модуля
BASE_DIR = pathlib.Path(__file__).parent.parent

# Создаем объект окружения и читаем переменные из файла .env
env = environ.Env()
environ.Env.read_env(BASE_DIR / ".env")

# Комментарий:
# BASE_DIR - это абсолютный путь к родительскому каталогу текущего модуля.
# env - это объект окружения, который позволяет читать переменные из файла .env.
# environ.Env.read_env(BASE_DIR / ".env") - это вызов метода read_env() 
#   объекта env с аргументом, который является путем к файлу .env.
