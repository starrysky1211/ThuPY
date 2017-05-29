from app.main import main_blueprint
from flask import render_template
from .forms import NameForm


@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)


@main_blueprint.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
