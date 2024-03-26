from bottle import route, view, redirect, template
from datetime import datetime


@route("/")
@route("/hello")
def hello():
    return template("views/hello.html")


@route("/about")
def about():
    return template("views/about.html")


@route("/arts")
def arts():
    return template("views/arts.html")
