# backend
[![Build Status](https://travis-ci.org/Motivatix/backend.svg?branch=master)](https://travis-ci.org/Motivatix/backend)

## Setup
```
$ virtualenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ nosetests
$ python import.py example_data/names example_data/data
$ python app.py
```
## Project structure
- motivatix
	- config.py # Configuration for development and testing environment
	- models.py # SQLAlchemy models
	- views.py # Flask routes
    - search.py # helper functions to search
- test
	- \_\_init\_\_.py # Base testcase to prepare and destroy application and database
	-  test_achievements_by_person.py and others # Test cases for API
- app.py # Script to start server
