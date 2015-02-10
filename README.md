# backend
[![Build Status](https://travis-ci.org/Motivatix/backend.svg?branch=master)](https://travis-ci.org/Motivatix/backend)

## Setup
```
$ virtualenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ nosetests
$ python app.py
```
## Project structure
- motivatix
	- config.py # Configuration for development and testing environment
	- models.py # SQLAlchemy models
	- views.py # Flask routes
- test
	- __init__.py # Base testcase to prepare and destroy application and database
	-  test_achievements_by_person.py and others # Test cases for API
- app.py # Script to start server
