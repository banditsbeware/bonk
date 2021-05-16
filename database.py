import sqlite3
import datetime

class doc:
    def __init__(self, title, id=None, date=None, body=None, tags=None, publish=0, views=0):
        self.title = title
        self.id    = id
        self.date  = date
        self.body  = body
        self.tags  = tags
        self.pub   = publish
        self.views = views

    def set_body(self, text):
        self.body = text

    def read_body(self, file_name):
        with open(file_name, 'r') as f: self.body = f.read()

    def save(self, conn):
        t = datetime.datetime.now()
        tup = (t.strftime('%b %d, %Y'), self.title, self.body, self.tags, self.pub, self.views)
        conn.execute('INSERT INTO docs (date, title, body, tags, pub, views) VALUES (?,?,?,?,?,?);', tup)
        conn.commit()

    def __repr__(self):
        return f'[post titled "{self.title}"]'

def connect():
    return sqlite3.connect('database.db')

def all_posts(conn):
    curs = conn.cursor()
    curs.execute('SELECT * FROM docs WHERE pub=1')
    posts = []
    for r in curs.fetchall():
        posts.append(doc(r[0], r[1], r[2], r[3], r[4], r[5], r[6]))

    return posts

def fetch(conn, id):
    curs = conn.cursor()
    curs.execute(f'SELECT * FROM docs WHERE pub=1 AND id={id};')
    r = curs.fetchone()
    return doc(r[0], r[1], r[2], r[3], r[4], r[5], r[6])


CREATE_DOCS = '''CREATE TABLE docs (
    title       TEXT NOT NULL,
    ID          INTEGER PRIMARY KEY AUTOINCREMENT,
    date        TEXT NOT NULL,
    body        BLOB,
    tags        TEXT,
    pub         INTEGER check (pub=0 or pub=1),
    views       INTEGER
);'''

if __name__ == '__main__':

    conn = connect()

    conn.execute('DROP TABLE docs')
    conn.execute(CREATE_DOCS)

    for i in range(10):
        D = doc(title=f'some title {i+1}', publish=1)
        D.set_body(f'wooo ' * i**2)
        D.save(conn)

    posts = all_posts(conn)

    for p in posts: print(f'{p.id}: {p.title}')

    conn.close()

