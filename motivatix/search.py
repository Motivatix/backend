from sqlalchemy.orm.exc import NoResultFound

from models import Person, Achievement


def search_by_name(name):
    try:
        person = Person.query.filter_by(name=name).one()
    except NoResultFound:
        return []
    else:
        return [{'description': a.description, 'age': a.age}
                for a in person.achievements.all()]


def search_by_age(age):
    achievements = Achievement.query.filter_by(age=age).all()

    return [{'person': a.person.name, 'description': a.description}
            for a in achievements]
