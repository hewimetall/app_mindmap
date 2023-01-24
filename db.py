import sqlite3
from settings import settings
from loguru import logger

class MixSqlCon(object):
    _conn:sqlite3.Connection = None

    def get_con(self)->sqlite3.Connection:
        if not self._conn: self.set_con(settings.db_file)
        return self._conn  


    def set_con(self, value  ) -> None:
        if self._conn: self.close_con()
        try:
            self._conn = sqlite3.connect(value)
            return self
        except sqlite3.Error as error:
            logger.exception("Ошибка при подключении к sqlite")

    
    def close_con(self) -> None:
        self._conn.close()
        logger.debug("Соединение с SQLite закрыто")

    conn = property(
        fget=get_con,
        fset=set_con,
        fdel=close_con,
        doc=" Connector for sql lite"
    )



class SqlLiteDriver(MixSqlCon):

    def execute(self, sql, *args):
        try:
            sql_row = self.conn.execute(sql, *args)
            logger.debug(sql_row)
            return sql_row.fetchall()[0]
        except:
            logger.exception("Ошибка запроса sqlite")
            logger.warning(sql)


db = SqlLiteDriver()
