from flask import Flask
import random

app = Flask(__name__)

topics = [
    {'id':1, 'title':'html','body': 'html is...'},
    {'id':2, 'title':'css','body': 'css is...'},
    {'id':3, 'title':'javascript','body': 'javascript is...'}
]

@app.route('/')
def index():
    Litags = ''
    for topic in topics:
        Litags = Litags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {Litags}
            </ol>
            <h2>Welcome</h2>
            Hello,Web
        </body>
    </html>
    '''

@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<id>/')
def read(id):
    print(id)
    return 'Read : <strong>' + id +'</strong>'

app.run()