from flask import Flask, render_template, request, g
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
    # TODO: better checking here
    id = request.form.get('id', None)
    if id == '': return render_template('editor.html',
            msg='please enter an ID')

    conn = db.connect()
    post = db.fetch(conn, id)
    try: 
        return render_template('editor.html', 
                id=id,
                title=post.title, 
                body=post.body, 
                tags= '' if post.tags is None else post.tags)

    except AttributeError:
        current_id = None
        return render_template('editor.html', 
                msg=f'no post found with ID {id}')

@app.route('/submit', methods=['POST'])
def submit():
    rf = request.form
    title = rf.get('title', None)
    body  = rf.get('body', None)
    tags  = rf.get('tags', None)
    id    = rf.get('id', None)

    if rf.get('publish') is not None: publish = 1
    if rf.get('save')    is not None: publish = 0

    new_doc = db.doc(title=title, body=body, tags=tags, publish=publish)

    if id is not None: new_doc.set_id(id)
    
    conn = db.connect()
    new_doc.save(conn)
    posts = db.all_posts(conn)

    return render_template('docs.html', posts=posts)


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
