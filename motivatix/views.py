from flask import abort, render_template, request
from sqlalchemy.orm.exc import MultipleResultsFound

from . import app
from search import search_by_name, search_by_age
from models import Person


@app.route('/')
def index():
    return render_template('index.html')


# srch-term can be
# - name of person: returns all his/her achievements
# - age: returns some (10? 20?) achievements achieved at that age
@app.route('/search', methods=['GET'])
def search():
    search_term = request.args.get('srch-term', '')

    try:
        try:
            age = int(search_term)
            achievements = search_by_age(search_term)
            return render_template('search.html', mode='age', age=age,
                                   achievements=achievements)
        except ValueError:
            person = Person.query.filter_by(name=search_term).all()
            if len(person) > 0:
                thumbnail = person[0].thumbnail
            else:
                thumbnail = 'http://www.aip-inc.us/upload/blank-face.jpg'

            achievements = search_by_name(search_term)
            return render_template('search.html', mode='name',
                                   name=search_term, achievements=achievements,
                                   thumbnail=thumbnail)
    except MultipleResultsFound:
        abort(500)  # Internal Server Error
