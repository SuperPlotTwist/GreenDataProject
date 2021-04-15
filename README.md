# GreenDataProject
A web-app and database that stores product packagings

## Installation
1. First, create a python virtual environment:
`python3 -m venv 'venv_name'`

2. Then activate it:
`./venvname/bin/activate`
or
`./venvname/Scripts/activate`

3. Install needed python modules:
`pip install django, dnspython, djongo`

4. Check the versions using `pip list`:

| | Version |
| ---- | ---- |
|Django|3.2|
|djongo| 1.3.4|
|pymongo|3.11.3|
|sqlparse|0.2.4|


5. Make migrations:
```
	python GreenData/manage.py makemigrations
	python GreenData/manage.py migrate
```

6. Run the server:
`python manage.py runserver`