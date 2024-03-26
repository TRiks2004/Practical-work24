# ARTS BERSERK

## Для началы работ с репозиторием 
* Нужно устоновит в систему [poetry](https://python-poetry.org "Системма контроля окружения")
* И спомошью [poetry](https://python-poetry.org "Системма контроля окружения") нужно устоновить зависемости описанные в `pyproject.toml`
```bash
    # Инцелизация проекта в терменале 
    poetry shell 
    # Установка зависимостей
    poetry install
```

## Запуск программы на лакальной машине
```bash
    poetry run python app.py
```
Сайт по умалчанию работает на `http://127.0.0.1:5564/`

### В проекте реализованно 3 странницы
* [`/`]((http://127.0.0.1:5564/hello)) или [`/hello`](http://127.0.0.1:5564/hello) - приветственная страница
* [`/about`](http://127.0.0.1:5564/about) - информация о проекте
* [`/contact`](http://127.0.0.1:5564/contact) - контакты проекта





