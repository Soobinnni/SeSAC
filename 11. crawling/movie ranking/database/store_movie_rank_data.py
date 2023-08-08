from database.Database import Database
from crawling.crawling_movie_ranking_data import mk_movie_rank_info_list

db = Database()
movie_rank_infos = mk_movie_rank_info_list()
        
def check_movie_name_in_movie_table(title:tuple):
    sql = """
        SELECT id
        FROM 
            ( 
                SELECT * 
                FROM movie 
                WHERE title = ?
            )
        """
    result = db.execute_fetch(sql, title)
    
    if result :
        return result[0]['id']
    else :
        return False
    
# TODO: 함수명이 적절하지 않은 것 같음, 너무 많은 처리를 함
def restore_rank_values() -> None:
    movie_id = None

    for movie_rank_info in movie_rank_infos:
        is_the_movie_in_the_movie_table = check_movie_name_in_movie_table((movie_rank_info['title'],))

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
            db.execute(sql, movie_values)
            db.commit()

            movie_id = db.execute_fetch('SELECT id FROM movie WHERE title = ?', (movie_rank_info['title'],))[0]['id']
            print('movie정보 없음')
        
        # insert into rank
        sql = 'INSERT INTO rank(date, ranking, rating, reservation_rate, movie_id)\
                VALUES(?, ?, ?, ?, ?)'
        values = ( movie_rank_info['date'], \
                    movie_rank_info['ranking'],\
                    movie_rank_info['rating'],\
                    movie_rank_info['reservation_rate'],\
                    movie_id)
        db.execute(sql, values)
        db.commit()


def create_movie_table()-> None:
# id, title, post_url, short_description, link
    db.execute('''
        CREATE TABLE IF NOT EXISTS movie(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            post_url TEXT,
            short_description TEXT,
            link TEXT
        )
    ''')

def create_rank_table()-> None :
# id, date, ranking, rating, reservation_rate, movie_id
    db.execute('''
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