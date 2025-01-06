# Qjango - A Qux Django Template

## Directory Structure

```
qjango
├── activate.sh
├── deploy.sh
├── qjango <github.git/quxdev/qjango.git>
│   ├── apps
│   ├── common
│   ├── config
│   ├── mailroom
│   ├── media
│   ├── project
│   ├── qux
│   ├── requirements
│   └── templates
└── venv
    ├── bin
    ├── include
    ├── lib
    └── share
```

## Virtual Environment

```
# Create virtual environment
python3 -m venv venv

if [[ $OSTYPE != darwin* ]]; then
    sed -i '' 's/PS1=\"(venv)/PS1=\"(venv:${repo})/g' venv/bin/activate
else
    sed -i 's/PS1=\"(venv)/PS1=\"(venv:${repo})/g' venv/bin/activate
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip and install packages
pip install --upgrade pip
pip install -r requirements/py312_dj5.txt

if [[ $OSTYPE == darwin* ]]; then
    pip install --upgrade pygraphviz --config-settings="--global-option=build_ext" --config-settings="--global-option=-I$(brew --prefix graphviz)/include/" --config-settings="--global-option=-L$(brew --prefix graphviz)/lib/";
else
    pip install --upgrade pygraphviz
fi
```

## Getting Started

```
account="quxdev"
repo="qjango"

git clone https://github.com/${account}/${repo}.git
cd ${repo}

# Update submodules
git submodule update --init

# Migrate models to db.sqlite3
python manage.py migrate

# Configure project/.env
dotenv="project/.env"
if [ ! -f dotenv ]; then
    touch ${dotenv}
    secret=$(python manage.py generate_secret_key)
    echo "DJANGO_SECRET_KEY=\"${secret}\"" >> ${dotenv}
    echo "DJANGO_DEBUG=true" >> ${dotenv}
    echo "BOOTSTRAP=bs5" >> ${dotenv}
fi

# Runserver and test
python manage.py runserver
```

## ENVIRONMENT

### Django

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_SITE_ID`
- `BOOTSTRAP=bs5`

### Database

- `DB_TYPE` = `[sqlite3|mysql]`
- `DB_NAME`
- `DB_USERNAME`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`

### wsgi.py

!! There is no reason to set these by default.

- `DJANGO_SETTINGS_MODULE`
- `DJANGO_PYTHON_PATH`

## Templates

### `_blank.html`

1. `qux_page_title_extra`: additional classes in heading
2. `qux_page_title`: page title
3. `qux_page_content`: page content
