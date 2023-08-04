from flask import Flask, render_template, request
from database import Database

app = Flask(__name__)
database = Database()

@app.route("/")
def index():
    # read
    return render_template('index.html')

@app.route("/list")
def list():
    # read
    result = database.execute_fetch('SELECT * FROM board')
    return result

@app.route('/create', methods=['POST'])
def create():
    title = request.form['title'] 
    message = request.form['message'] 
    
    # create
    database.execute('INSERT INTO board(title, message) VALUES(?, ?)', (title, message))
    database.commit()
    
    return "OK"


@app.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    # delete
    database.execute('DELETE FROM board WHERE id = ?', (id,))
    database.commit()

    return 'OK'

@app.route('/<int:id>/update', methods=['POST'])
def update(id):
    title = request.form['title'] 
    message = request.form['message'] 

    # delete
    database.execute('UPDATE board SET title = ? WHERE id = ?', (title, id))
    database.execute('UPDATE board SET message = ? WHERE id = ?', (message, id))
    database.commit()

    return 'OK'

if __name__ == '__main__' :
    app.run(debug=True)