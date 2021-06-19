import sqlite3
import datetime

class doc:
    # default constructor is for creating a new doc, then storing in database
    def __init__(self, title, date=None, body=None, tags=None, publish=0, views=0):
        self.id    = None
        self.title = title
        self.date  = date
        self.body  = body
        self.tags  = tags
        self.pub   = publish
        self.views = views

    # this constructor can be used when populating an instance from preexisting database entry
    @classmethod
    def from_database(cls, conn, id):
        curs = conn.cursor()
        curs.execute('SELECT * FROM docs WHERE id=?;', (id,))
        res = curs.fetchone()
        if res is None: return None

        id, title, date, body, tags, pub, views = res
        obj = cls(title, date, body, tags, pub, views)
        obj.id = id
        return obj

    def set_body(self, text): self.body = text
    def set_id(self, id): self.id = id

    def save(self, conn):
        t = datetime.datetime.now()
        tup = (self.title, t.strftime('%b %d, %Y'), self.body, self.tags, self.pub, self.views)
        if self.id is None:
            conn.execute('INSERT INTO docs (title, date, body, tags, pub, views) VALUES (?,?,?,?,?,?);', tup)
        else:
            conn.execute('UPDATE docs SET title=?, date=?, body=?, tags=?, pub=?, views=? WHERE id=?', tup + (self.id,))
        conn.commit()

    def __repr__(self): return f'[DOC "{self.title}" ({self.views} views)]'

def connect(): return sqlite3.connect('database.db')

def all_posts(conn):
    curs = conn.cursor()
    curs.execute('SELECT id FROM docs WHERE pub=1')
    return [doc.from_database(conn, r[0]) for r in curs.fetchall()]

def fetch(conn, id): return doc.from_database(conn, id)

CREATE_DOCS = '''CREATE TABLE docs (
    ID          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT NOT NULL,
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
        D = doc(title=f'Title {i+1}', publish=1)
        D.set_body('wooo yea \n' * (i+1))
        D.save(conn)

    conn.close()

