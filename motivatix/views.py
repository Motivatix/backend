from flask import abort, jsonify
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from . import app
from models import Person, Achievement


@app.route('/achievements/<name>/')
def get_achievements_by_person(name):
    name = name.replace('_', ' ')
    try:
        person = Person.query.filter_by(name=name).one()
    except MultipleResultsFound:
        abort(500)  # Internal Server Error
    except NoResultFound:
        abort(404)  # Not Found
    response = [{'description': a.description, 'age': a.age}
                for a in person.achievements.all()]
    return jsonify(achievements=response)


@app.route('/achievements/<int:age>/')
def get_achievements_by_age(age):
    achievements = Achievement.query.filter_by(age=age).all()

    response = [{'person': a.person.name, 'description': a.description}
                for a in achievements]
    return jsonify(achievements=response)
