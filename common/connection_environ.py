import environ
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

def get_env() -> environ.Env:
    """
    Возвращает переменные окружения
    """
    return env
    


if __name__ == '__main__':
    print(BASE_DIR)
    print(env)
