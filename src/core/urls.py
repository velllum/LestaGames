from flask import Flask

from . import views


def init_urls(app: Flask):
    """- регистрируем urls """
    app.add_url_rule(rule='/', endpoint="index", view_func=views.Index.as_view("index"))

