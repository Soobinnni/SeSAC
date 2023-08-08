import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import date

# link
daum_movie = 'https://movie.daum.net/ranking/reservation'

def get_requests_html_parser(url) :
    data = requests.get(url)

    soup = BeautifulSoup(data.text, 'html.parser')

    return soup

domain_soup = get_requests_html_parser(daum_movie)

# ----데이터베이스설정 
conn = sqlite3.connect('movie.db')
cursor = conn.cursor()

# ----테이블생성
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movie(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        ranking INTEGER,
        title TEXT,
        rating TEXT,
        reservation_rate TEXT,
        post_url TEXT,
        short_description TEXT
        )
    ''')
def mk_daum_movie_ranking_info() :
    # 1. 다음영화랭킹(제목/평점/예매율) 
    sql = 'INSERT INTO movie(date, ranking, title, rating, reservation_rate, post_url, short_description)\
            VALUES(?, ?, ?, ?, ?, ?, ?)'
    li = domain_soup.select('ol.list_movieranking')[0].select('li')
    # title, rating, reservation_rate, post_url, short_description
    #mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_item > div.poster_movie > img
    movie_ranking_info = [( str(date.today()), (i+1), l.select_one('.tit_item a').text,\
                            l.select_one('span.txt_append > span:nth-child(1) > span').text,\
                            l.select_one('span.txt_append > span:nth-child(2) > span').text,\
                            l.select_one('.thumb_item > div.poster_movie > img').attrs['src'],\
                            l.select_one('.poster_info a').text.strip() \
                            ) for i, l in enumerate(li)]

    return movie_ranking_info

def restore_daum_movie_ranking_info() :
    daum_movie_ranking_info = mk_daum_movie_ranking_info()

    sql = 'INSERT INTO movie(date, ranking, title, rating, reservation_rate, post_url, short_description)\
            VALUES(?, ?, ?, ?, ?, ?, ?)'
    for d in daum_movie_ranking_info :
        cursor.execute(sql, d)
        conn.commit()

def print_url_and_short_info():
    # 2. 포스터URL링크, 쇼트설명
    li = domain_soup.select('ol.list_movieranking')[0].select('li')
    url_list = [{'link' : 'https://movie.daum.net'+(l.select_one('.poster_info a').attrs['href'].strip()),\
                'short_info' : l.select_one('.poster_info a').text.strip() } for l in li]
    print(url_list)


if __name__ == '__main__' :
    # print_daum_movie_ranking_info()
    # print_url_and_short_info()
    # print(date.today())
    restore_daum_movie_ranking_info()