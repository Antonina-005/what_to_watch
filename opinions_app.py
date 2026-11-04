# mypy: ignore-errors
from random import randrange

from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'MY_SECRET_KEY'
db = SQLAlchemy(app)


class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.Text, nullable=False)
    source = db.Column(db.String(256))


class OpinionForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired(), Length(1, 128)])
    text = StringField('Текст', validators=[DataRequired()])
    source = URLField('Ссылка', validators=[Length(0, 256)])
    submit = SubmitField('Добавить')


@app.route('/')
def index_view():
    quantity = Opinion.query.count()
    if not quantity:
        return 'В базе данных записей нет.'
    offset_value = randrange(quantity)
    opinion = Opinion.query.offset(offset_value).first()
    return render_template('opinion.html', opinion=opinion)


@app.route('/add', methods=['GET', 'POST'])
def add_opinion_view():
    form = OpinionForm()
    if form.validate_on_submit():
        opinion = Opinion(
            title=form.title.data,
            text=form.text.data,
            source=form.source.data
        )
        db.session.add(opinion)
        db.session.commit()
        return redirect(url_for('opinion_view', id=opinion.id))
    return render_template('add_opinion.html', form=form)


@app.route('/opinions/<int:id>')
def opinion_view(id):
    opinion = Opinion.query.get_or_404(id)
    return render_template('opinion.html', opinion=opinion)


if __name__ == '__main__':
    app.run()
