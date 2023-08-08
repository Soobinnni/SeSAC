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
    
    def create_movie_table(self) :
    # id, title, post_url, short_description, link
        self.execute('''
            CREATE TABLE IF NOT EXISTS movie(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                post_url TEXT,
                short_description TEXT,
                link TEXT
            )
        ''')

    def create_rank_table(self) :
    # id, date, ranking, rating, reservation_rate, movie_id
        self.execute('''
            CREATE TABLE IF NOT EXISTS rank(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                ranking INTEGER,
                rating REAL,
                reservation_rate REAL,
                movie_id INTEGER,
                FOREIGN KEY (movie_id) REFERENCES movie (id)
            )
        ''')

    def commit(self):
        self.db.commit()

