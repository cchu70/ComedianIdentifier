##database manager

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
#Prevent posible package not found error
import sqlite3

sqlite_file = 'my_db.sqlite'                #filename for database

class DatabaseManager:
    def __init__(self):
        self.__conn = sqlite3.connect(sqlite_file)
        self.__cur = self.__conn.cursor()
        self.create()

    def create(self):
        command = '''CREATE TABLE IF NOT EXISTS JOKES (
            Comedian text,
            Joke text,
            Charlen integer,
            Wordlen integer
        )
        '''
        self.__cur.execute(command)
        self.__conn.commit()

    def execute(self, command):
        self.__cur.execute(command)

    def fetch(self):
        return self.__cur.fetchone()

    def fetch_all(self):
        return self.__cur.fetchall()

    def commit(self):
        return self.__conn.commit()

    def close(self):
        return self.__conn.close()





