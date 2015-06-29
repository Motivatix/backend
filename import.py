#!/usr/bin/env python
"""Imports parsed achievements data into database."""

import os
import sys


def usage(program_name):
    sys.stderr.write("""Usage: {} NAMES_FILE DATA_DIR

    NAMES_FILE - file containing a list of tab-separated values (one per line),
                 as created by dbpedia processing tool 'getnames'.
    DATA_DIR   - directory containing data about achievements of people from
                 NAMES_FILE, one file per person, containing tab-separated
                 list of achievements (age, achievement) as returned by wiki
                 processing tool 'achievements'.
    """.format(program_name))


def main(args):
    if len(args) < 3:
        usage(args[0])
        sys.exit(1)

    names_list = args[1]
    dump_dir = args[2]

    if not os.path.isfile(names_list):
        usage(args[0])
        sys.exit(2)

    if not os.path.isdir(dump_dir):
        usage(args[0])
        sys.exit(3)

    from motivatix import create_app
    create_app('default')

    from motivatix import db
    from motivatix.models import Person, Achievement

    with open(names_list) as f_names:
        for line in f_names:
            line = line.strip()
            name, wiki_id, _, thumbnail = line.split('\t')
            name = name.decode('utf-8')
            p_db = Person.query.filter_by(name=name).all()
            if len(p_db) == 0:
                person = Person(name, thumbnail)
                db.session.add(person)
            else:
                person = p_db[0]

            print('Processing: {}'.format(person.name))

            with open(os.path.join(dump_dir, wiki_id)) as f_achievements:
                for line_ac in f_achievements:
                    line_ac = line_ac.strip()
                    age, text = line_ac.split('\t')
                    text = text.decode('utf-8')
                    achievement = Achievement(text, int(age), person)
                    db.session.add(achievement)
    db.session.commit()


if __name__ == '__main__':
    main(sys.argv)

# vi:set et sts=4 sw=4 ts=4:
