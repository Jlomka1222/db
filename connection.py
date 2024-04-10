import psycopg2
from loguru import logger


class DatabaseConnection:
    def __init__(self, dbname='postgres', user='postgres', password='mysecretpassword', host='127.0.0.1'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.conn = None

    def create_connection(self):
        try:
            self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host)
            self.conn.autocommit = True
            logger.info("Connection open!")
        except psycopg2.DatabaseError as e:
            logger.error(f"connection error: {e}")

        return self.conn

    def close_connection(self):
        try:
            self.conn.close()
            logger.info("Connection closed.")
        except Exception as e:
            logger.error(f"Close exception:{e}")
