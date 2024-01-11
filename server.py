from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'random: <strong>' + str(random.random()) + '</strong>'

@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<id>/')
def read(id):
    print(id)
    return 'Read : <strong>' + id +'</strong>'

app.run()