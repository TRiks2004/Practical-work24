from bottle import route, view, redirect, template
from datetime import datetime

from enum import Enum

from datebase import models

class Views(Enum):
    hello = "hello"
    about = "about"
    arts = "arts"

    @staticmethod
    def get_views(name: "Views") -> str:
        return f"views/{name.value}.html"

    @staticmethod
    def get_view_hello() -> str:
        return Views.get_views(Views.hello)

    @staticmethod
    def get_view_arts() -> str:
        return Views.get_views(Views.arts)

    @staticmethod
    def get_view_about() -> str:
        return Views.get_views(Views.about)


class Routes(Enum):
    hello = "hello"
    about = "about"
    arts = "arts"

    spase = ""

    @staticmethod
    def get_routes(name: "Routes") -> str:
        return f"/{name.value}"

    @staticmethod
    def get_route_hello() -> str:
        return Routes.get_routes(Routes.hello)

    @staticmethod
    def get_route_arts() -> str:
        return Routes.get_routes(Routes.arts)

    @staticmethod
    def get_route_about() -> str:
        return Routes.get_routes(Routes.about)

    @staticmethod
    def get_route_spase() -> str:
        return Routes.get_routes(Routes.spase)


@route(Routes.get_route_spase())
def spase():
    return redirect(Routes.get_route_hello())


@route(Routes.get_route_hello())
def hello():
    return template(Views.get_view_hello())


@route(Routes.get_route_about())
def about():
    return template(Views.get_view_about())


@route(Routes.get_route_arts())
def arts():
    return template(
        Views.get_view_arts(),
        dict = {
            "arts": models.ArtsModel.get_all_rows()
        })
