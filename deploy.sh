#!/bin/bash

# Activate virtual environment
source ../venv/bin/activate

# run migrations
python manage.py migrate

# collect static files
python manage.py collectstatic --noinput

# restart apache2 and supervisor
sudo service apache2 restart
sudo service supervisor restart
