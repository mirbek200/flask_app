from pydoc import describe
from flask import Flask, render_template, request, redirect
from peewee import *
from models import *

app = Flask(__name__)

@app.route('/')
def mike():
    all_posts = Post.select()
    return render_template("index.html", posts=all_posts)

@app.route('/create', methods = ('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        description= request.form['description']

        Post.create(
            title = title,
            description = description
        )
        return redirect('/')
    return render_template('create.html')
@app.route('/bye')
def bye():
    return '<h1>Bye bye<h1>'

if __name__=="__main__":
    app.run(debug=True)