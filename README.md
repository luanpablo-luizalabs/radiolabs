RadioLabs
=========

A Django version of https://github.com/alexayub-luizalabs/labsRadio


How to use
==========

**NOTE:** It's recommended to use a virtualenv.

Firstly, run:

    pip install -r requirements.txt
    python manage.py migrate

Create your user:

    python manage.py createsuperuser

Then, run the project:

    python manage.py runserver 0.0.0.0:8000

Done.
