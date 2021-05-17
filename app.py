from flask import Flask, render_template
import database as db

app = Flask(__name__, template_folder='scaff')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/editor')
def editor():
    return render_template('editor.html')

@app.route('/docs')
def docs():
    conn = db.connect()
    posts = db.all_posts(conn)
    return render_template('docs.html', posts=posts)

@app.route('/docs/<int:id>')
def doc(id):
    conn = db.connect()
    post = db.fetch(conn, id)
    return render_template('doc.html', ID=post.id, TITLE=post.title, TEXT=post.body)

if __name__ == '__main__': app.run(port=3000)
