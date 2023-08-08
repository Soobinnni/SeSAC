from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
# ----데이터베이스설정 
conn = sqlite3.connect('movie.db', check_same_thread=False)
cursor = conn.cursor()

@app.route('/movie/ranking')
def movie_ranking() :
    sql = 'SELECT date, ranking, title, rating, reservation_rate, post_url, short_description FROM movie'
    cursor.execute(sql)
    result = cursor.fetchall() 
    return render_template('movie_ranking.html', movie_rankings = result)
if __name__ == '__main__':
    app.run(debug=True)