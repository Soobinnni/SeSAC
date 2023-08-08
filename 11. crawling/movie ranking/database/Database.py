import sqlite3

class Database():
    def __init__(self) -> None:
        self.db = sqlite3.connect('database/movie.db', check_same_thread=False)
        self.db.row_factory = sqlite3.Row  
        self.cursor = self.db.cursor()

    def execute(self, query, args=()):
        self.cursor.execute(query, args)

    def execute_fetch(self, query, args=()):
        self.cursor.execute(query, args)
        result = self.cursor.fetchall()
        result = [dict(element) for element in result]
        return result

    def commit(self):
        self.db.commit()

