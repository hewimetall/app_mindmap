import configparser
from fastapi.templating import Jinja2Templates
from loguru import logger
SETTINGS_FILE_NAME = 'settings.ini'

class Settings(object):
    def __init__(self) -> None:
        self._cp = configparser.ConfigParser()
        self._cp.read(SETTINGS_FILE_NAME)
        
    def __getattribute__(self, name: str):
        try:
            return super().__getattribute__(name)
        except:
            # retunr default data
            logger.debug(f"Not found attr {name}")
            return name

    @property
    def user(self):
        return self._cp['user', 'adm']

    @property
    def password(self):
        return self._cp.get('password', 'adm_pwd')

    @property
    def db_file(self):
        return self._cp.get('db_file', 'db_file')

settings = Settings()
templates = Jinja2Templates(directory="templates")
