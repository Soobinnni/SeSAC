from database.Database import Database

class MovieRankDatabaseQuery(Database) :
    def get_movie_dates_grouped(self) :
        sql = 'SELECT DISTINCT date FROM rank'
        result = [date['date'] for date in self.execute_fetch(sql)]

        return result
    
    def get_movie_rank_info_on_date(self, date):
        sql = """
            SELECT *
            FROM rank r
            JOIN movie m ON m.id = movie_id
            WHERE r.date = ?
            ORDER BY ranking
        """
        result = self.execute_fetch(sql, (date,))
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