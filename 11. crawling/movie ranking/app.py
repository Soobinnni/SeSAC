from flask import Flask, render_template
from database.Database import Database
from apscheduler.schedulers.background import BackgroundScheduler # scheduler

app = Flask(__name__)
db = Database()

root = '/movie/ranking'

#-----
#스케줄 실행 코드
def scheduler():
    print("Scheduler is alive!")

schedule = BackgroundScheduler(daemon=True, timezone='Asia/Seoul')
schedule.add_job(scheduler, 'interval', seconds=3)
schedule.start()
#-----


@app.route(root)
def movie_ranking() :
    sql = 'SELECT date FROM rank GROUP BY date'
    result = [date['date'] for date in db.execute_fetch(sql)]
    return render_template('movie_ranking.html', date_list = result)

@app.route(root+'/<date>')
def movie_ranking_by_date(date):
    sql = """
        SELECT *
        FROM rank r
        JOIN movie m ON m.id = movie_id
        WHERE r.date = ?
    """
    result = db.execute_fetch(sql, (date,))
    return render_template('movie_ranking_by_date.html', movie_info = result)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask     # Flask 라이브러리 선언
from flask import request                                     

#API서비스 선언
def 서비스의 함수명:
   return 실제참조할 클래스의 함수

#apscheduler 선언
sched = BackgroundScheduler(daemon=True)

#apscheduler실행설정, Cron방식으로, 1주-53주간실행, 월요일부터일요일까지실행, 21시에실행
sched.add_job(서비스의 함수명,'cron', week='1-53', day_of_week='0-6', hour='21')

#apscheduler실행
sched.start()

#API서비스 실행
if__name__ == "__main__":
   app.run(host='0.0.0.0',use_reloader=False)