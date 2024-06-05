from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return { test: "blabla"}

@app.route('/hello')
def hello():
    return 'Hello, Musica Cafe'