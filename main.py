import sqlite3
import time

from flask import Flask, request

app = Flask(__name__)
database = sqlite3.connect('database.sqlite3', check_same_thread=False)
cursor = database.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS sheet(client TEXT, timestamp REAL, url TEXT)''')


@app.route('/register')
def register():
    cursor.execute(
        f'INSERT INTO sheet(client, timestamp, url) VALUES ("{request.args.get("client")}", {time.time()}, "{request.args.get("url")}")')
    return {'status': 200}


@app.route('/inspect')
def inspect():
    select = cursor.execute(f'SELECT * FROM sheet')
    r = []
    for c, t, u in select:
        r.append((c, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t)), u))
    return f'{r}'


if __name__ == '__main__':
    app.run()
