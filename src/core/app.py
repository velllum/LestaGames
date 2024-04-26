from flask import Flask

from . import settings
from . import urls


def create_app() -> Flask:
    """- инициализируем приложения"""
    app = Flask(__name__, template_folder=settings.path_to_templates)
    init_config(app)

    # запускаем контекст объекта
    with app.app_context():
        init_urls(app)
        return app


def init_config(app: Flask):
    """- инициализируем конфигурационные данные"""
    print(" * Инициализация конфигурационного файла")
    app.config.from_pyfile(settings.path_to_config)


def init_urls(app: Flask):
    """- инициализируем url маршрутов"""
    print(" * Инициализация URL")
    urls.init_urls(app)

