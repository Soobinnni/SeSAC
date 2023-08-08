from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler 
import time

from database.MovieRankDatabaseQuery import MovieRankDatabaseQuery
from database.store_movie_rank_data import restore_rank_values

app = Flask(__name__)
db = MovieRankDatabaseQuery()
root = '/movie/ranking'

#-----
# route functions
@app.route(root)
def movie_ranking() :
    date_list = db.get_movie_dates_grouped()
    return render_template('movie_ranking.html', date_list = date_list)

@app.route(root+'/<date>')
def movie_ranking_by_date(date):
    daily_movie_rank_info = db.get_movie_rank_info_on_date(date)
    return render_template('movie_ranking_by_date.html', daily_movie_rank_info = daily_movie_rank_info)

#-----
# scheduler : 1) 자동화 2) 멀티 스레드 지원으로 메인 스레드와 별개의 스레드에서 스케줄 작업 진행
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"{func.__name__} 실행 시간: {run_time:.6f}초")
        return result
    return wrapper

@measure_time
def crawling_daily_movie_rank_info():
    print("영화 정보 크롤링 스케줄 시작")
    restore_rank_values()

def initialize_scheduler():
    scheduler = BackgroundScheduler(daemon=True, timezone='Asia/Seoul')
    scheduler.add_job(crawling_daily_movie_rank_info, 'cron', hour=0, minute=0) # 매 12시 스케줄 등록
    scheduler.start()


# TODO: 크롤링 작업이 실패했거나, 재 업로드가 필요할 때 수동으로 작업할 수 있는 코드 작성하기 
# 페이지에 비밀번호 설정하여 인증, 인가하기

#-----
# app run
if __name__ == '__main__':
    initialize_scheduler()  
    app.run(debug=True)