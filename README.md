## GreenDataProject

A web-app and database that stores product packagings

## Installation

1. First, create a python virtual environment:
`python3 -m venv 'venv_name'`

2. Then activate it:
`./venvname/bin/activate`
or
`./venvname/Scripts/activate`

3. Install needed python modules:
`pip install django, dnspython, django-countries, pytz`

4. Check the versions using `pip list`:

| | Version |
| ---- | ---- |
|Django|3.2|
|django-counties| 7.1|
|pytz|2021.1|
|sqlparse|0.4.1|

5. Make migrations (automatically create the database's design):

```sh
 python GreenData/manage.py makemigrations
 python GreenData/manage.py migrate
```

6. Run the server:
`python manage.py runserver`
