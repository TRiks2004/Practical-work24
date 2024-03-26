from .settings import env, BaseSettings

class SettingsAPP(BaseSettings):
    """
    Класс, представляющий настройки приложения. Содержит поля, которые определяют тип сервера, хост, порт,
    активацию перезагрузки приложения при изменении кода, активацию режима отладки и корневую папку
    статических файлов.

    Attributes:
        server (str): Тип сервера для запуска приложения. По умолчанию "wsgiref".
        host (str): Хост, на котором запускается сервер. По умолчанию "localhost".
        port (int): Порт, на котором запускается сервер. По умолчанию 5565.
        reloader (bool): Флаг активации перезагрузки приложения при изменении кода.
            По умолчанию True.
        debug (bool): Флаг активации режима отладки. По умолчанию True.
        static_root (str): Корневая папка статических файлов. По умолчанию "static".
    """
    server: str = env.str("SERVER_APP", default="wsgiref")
    host: str = env.str("SERVER_HOST", default="localhost")
    port: int = env.int("SERVER_PORT", default=5565)
    reloader: bool = env.bool("RELOADER_APP", default=True)
    debug: bool = env.bool("DEBUG_APP", default=True)

    static_root: str = env.str("STATIC_ROOT", default="static")


settings_app = SettingsAPP()  # Создание экземпляра класса настроек приложения.
