import os

from dotenv import load_dotenv

load_dotenv()


# получить полный путь до корневой директории
basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
# получить путь до файла config.cfg
path_to_config = os.path.join(basedir, os.getenv('APP_CONFIG_FILE'))
# получить путь до шаблонов
path_to_templates = os.path.join(basedir, 'src', 'templates')
