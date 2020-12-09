from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Annabeth'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Powell!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Loving Danganronpa!'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts) 
