from database.Database import Database
from crawling.crawling_movie_ranking_data import mk_movie_rank_info_list
from .crawling_count import CrawlingCountDatabase

class MovieDatabase(Database) :
    def __init__(self) -> None:
        self.movie_rank_infos = mk_movie_rank_info_list()
        
    def check_movie_name_in_movie_table(self, title:tuple):
        sql = """
            SELECT id
            FROM 
                ( 
                    SELECT * 
                    FROM movie 
                    WHERE title = ?
                )
            """
        result = self.execute_fetch(sql, title)
        
        if result :
            return result[0]['id']
        else :
            return False
        

    def restore_rank_values(self) :
        movie_id = None

        for movie_rank_info in self.movie_rank_infos:
            is_the_movie_in_the_movie_table = self.check_movie_name_in_movie_table((movie_rank_info['title'],))
            if bool(is_the_movie_in_the_movie_table) :
                movie_id = is_the_movie_in_the_movie_table
                print('movie정보 있음')

            else : 
                # insert into movie
                sql = 'INSERT INTO movie(title, post_url, short_description, link)\
                        VALUES(?, ?, ?, ?)'
                movie_values = ( movie_rank_info['title'],\
                                movie_rank_info['post_url'],\
                                movie_rank_info['short_description'],\
                                movie_rank_info['link']) 
                self.execute(sql, movie_values)
                self.commit()

                movie_id = self.execute_fetch('SELECT id FROM movie WHERE title = ?', (movie_rank_info['title'],))[0]['id']
                print('movie정보 없음')
            
            # insert into rank
            sql = 'INSERT INTO rank(date, ranking, rating, reservation_rate, movie_id)\
                    VALUES(?, ?, ?, ?, ?)'
            values = ( movie_rank_info['date'], \
                        movie_rank_info['ranking'],\
                        movie_rank_info['rating'],\
                        movie_rank_info['reservation_rate'],\
                        movie_id)
            self.execute(sql, values)
            self.commit()

            # crawling count
            CrawlingCountDatabase().update_crawling_count(movie_rank_info['date']) 


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