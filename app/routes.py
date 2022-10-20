from app import app
from flask import flash, render_template, redirect, url_for

from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    print('in the index endpoint')
    user = { 'username' : 'Miguel'}
    posts = [
        {
            'author' : { 'username' : 'John'},
            'body' : 'Beautiful day in Portland'
        },
        {
            'author' : { 'username' : 'Susan'},
            'body' : 'The Avengers movie was cool'
        }
    ]
    return render_template('index.html', user=user, posts=posts, title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
