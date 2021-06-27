from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user={'username':'Krishna'}
    posts=[
        {
            'author': {'username':'Jesus'},
            'body'  : "I slept with your mother"
        },
        {
            'author':{"username": "Jesus' mother"},
            'body'  : "My son fucked my best friend oh no"
        }
    ]
    return render_template('index.html',title='Home',user=user, posts=posts)
