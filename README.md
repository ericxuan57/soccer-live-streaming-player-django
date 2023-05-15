# README

This is a soccer live-streaming player created using Django Web Framework.

## How to start the project

Make sure you have installed virtualenv pip. If not, install virtualenv via the command below.
```bash
pip install virtualenv
```

Create a virtualenv
```bash
virtualenv env
```

Activate the created virtualenv
```bash
source env/Scripts/Activate
```

Install development dependencies
```bash
pip install -r requirements.txt
```

Create .env file from .env.example file in soccer directory

Migrate Database
```bash
python manage.py makemigrations
python manage.py migrate
```

Create Superuser
```bash
python manage.py createsuperuser
```

Run the web application locally
```bash
python manage.py runserver
```