from flask import Flask, render_template, request
import database as db

app = Flask(__name__, template_folder='scaff')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/editor')
def editor():
    return render_template('editor.html')

@app.route('/edit', methods=['POST'])
def edit():
    id = request.form.get('id', None)
    if id == '': return render_template('editor.html',
            error_msg='please enter an ID')

    conn = db.connect()
    post = db.fetch(conn, id)
    try: 
        return render_template('editor.html', 
                title=post.title, 
                body=post.body, 
                tags=post.tags)

    except AttributeError:
        return render_template('editor.html', 
                error_msg=f'no post found with ID {id}')


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
