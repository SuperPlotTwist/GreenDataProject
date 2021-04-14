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

4. Make migrations:
```
	python GreenData/manage.py makemigrations
	python GreenData/manage.py migrate
```

4. Run the server:
`python manage.py runserver`