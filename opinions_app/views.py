# mypy: ignore-errors
from random import randrange

from flask import Blueprint, redirect, render_template, url_for

from . import db
from .forms import OpinionForm
from .models import Opinion

# Создаем блюпринт для наших страниц
opinions_bp = Blueprint('opinions', __name__)

@opinions_bp.route('/')
def index_view():
    quantity = Opinion.query.count()
    if not quantity:
        return 'В базе данных записей нет.'
    offset_value = randrange(quantity)
    opinion = Opinion.query.offset(offset_value).first()
    return render_template('opinion.html', opinion=opinion)

@opinions_bp.route('/add', methods=['GET', 'POST'])
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
        return redirect(url_for('opinions.opinion_view', id=opinion.id))
    return render_template('add_opinion.html', form=form)

@opinions_bp.route('/opinions/<int:id>')
def opinion_view(id):  
    opinion = Opinion.query.get_or_404(id)
    return render_template('opinion.html', opinion=opinion)
