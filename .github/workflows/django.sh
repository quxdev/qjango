export DJANGO_SECRET_KEY='thequickbrownfoxjumpsoverthelazydog'
export DJANGO_DEBUG='True'
export DJANGO_ALLOWED_HOSTS='localhost'
export BOOTSTRAP='bs5'
export EMAIL_BACKEND=django.core.mail.backends.console.ConsoleBackend
export DJANGO_SETTINGS_MODULE="project.settings"

pip install --upgrade pip
pip install -r requirements/py312_dj5.txt

pip install pylint pylint-django
pylint --rcfile=.pylintrc project
pylint --rcfile=.pylintrc apps

pip install black
black --check project
black --check apps

python manage.py test project
python manage.py test apps
