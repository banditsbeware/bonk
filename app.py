from flask import Flask, render_template

app = Flask(__name__, template_folder='scaff')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/docs')
def docs():
    return render_template('docs.html')

@app.route('/docs/<int:id>')
def doc(id):
    # perform database lookup
    # title = ' '
    # text = ' '
    return render_template('doc.html', title=title, text=text)


if __name__ == '__main__': app.run(port=3000)
