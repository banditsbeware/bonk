from flask import Flask
from .blue import bp

app = Flask(__name__)

app.register_blueprint(bp)
