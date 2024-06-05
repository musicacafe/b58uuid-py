from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({ test: "blabla"})

@app.route('/hello')
def hello():
    return 'Hello, Musica Cafe'