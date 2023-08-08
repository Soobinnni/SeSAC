from database.Database import Database
from crawling.crawling_movie_ranking_data import mk_movie_rank_info_list

def create_rank_table() -> None :
    # 크롤링 데이터가 더 수집될 수도 있으니 rank와 관계 테이블로 두지 않았음
    # id, date, crawling_count
    self.execute('''
        CREATE TABLE IF NOT EXISTS crawling_count(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            crawling_count INTEGER default 0
        )
    ''')
def update_crawling_count(date)->None:
    sql = """
        UPDATE crawling_count
        SET crawling_count = 1
        WHERE date = ?
    """
    self.execute(sql, (date,))
    self.commit()

def get_crawling_count(self, date)-> int :
    sql = """
        SELECT crawling_count
        FROM crawling_count
        WHERE date = ?
        """
    result = int(self.execute_fetch(sql, (date,))[0]['crawling_count'])

    return result