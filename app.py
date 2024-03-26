# Это основной модуль приложения. Он отвечает за запуск веб-сервера Bottle и подключение к нему статических файлов.

import bottle

# Модуль, который содержит все маршруты приложения.
import routes

# Модуль, который содержит настройки приложения.
from common import settings_app, SettingsAPP

# Модуль, который предоставляет функции для работы с путями файлов.
import pathlib

from datebase import create_tables, models


def up() -> None:
    create_tables(models.get_models())


def include_static_files(static_root: str) -> None:
    """
    Функция, которая подключает статические файлы к приложению.

    param static_root: корневой каталог статических файлов.
    """
    BASE_DIR = pathlib.Path(__file__).parent

    @bottle.route(f"/static/<filepath:path>")
    def server_static(filepath):
        """
        Маршрут, который отвечает за отдачу статических файлов.

        param filepath: путь к файлу.
        """
        return bottle.static_file(filepath, root=f"{BASE_DIR}/{static_root}")


def main(settings: SettingsAPP):
    """
    Функция, которая запускает веб-сервер Bottle с настройками, заданными в settings_app.

    param settings: настройки приложения.
    """
    up()

    include_static_files(settings.static_root)

    bottle.run(
        server=settings.server,
        host=settings.host,
        port=settings.port,
        reloader=settings.reloader,
        debug=settings.debug,
    )


if __name__ == "__main__":
    main(settings_app)
