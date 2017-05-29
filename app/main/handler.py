from app.main import main_blueprint
from flask import render_template


@main_blueprint.route('/')
def index():
    return render_template('index.html')


@main_blueprint.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
