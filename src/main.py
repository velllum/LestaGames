import os

from core import app

# инициализируем, создаем приложение flask
application = app.create_app()


if __name__ == '__main__':
    application.run(host=os.getenv('HOST'), port=os.getenv('PORT'))

