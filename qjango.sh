account="quxdev"
repo="qjango"

function display_help {
    echo "Usage: $0 [OPTIONS]"
    echo "Options:"
    echo "  -a, --account ACCOUNT_NAME   Specify account name"
    echo "  -r, --repo REPOSITORY_NAME   Specify repository name"
    echo "  -h, --help                   Display this help message"
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        -a|--account)
            account="$2"
            shift 2
            ;;
        -r|--repo)
            repo="$2"
            shift 2
            ;;
        -h|--help)
            display_help
            exit 0
            ;;
        *)
            echo "Unknown argument: $1"
            display_help
            exit 1
            ;;
    esac
done

# Check if git is configured for use with ssh.
# ssh is our preferred method of authentication.
ssh -T git@github.com > /dev/null 2>&1
if [ $? -eq 1 ]; then
    git clone git@github.com:${account}/${repo}.git
else
    git clone https://github.com/${account}/${repo}.git
fi

cd ${repo}

# Update submodules
git submodule update --init

# Create virtual environment
python3.8 -m venv venv

if [[ $OSTYPE == darwin* ]]; then
    sed -i '' 's/PS1=\"(venv)/PS1=\"(venv:$repo)/g' venv/bin/activate
else
    sed -i 's/PS1=\"(venv)/PS1=\"(venv:$repo)/g' venv/bin/activate
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip and install packages
pip install --upgrade pip
pip install -r requirements.txt

echo $(pwd)

echo $(which python)

# Migrate models to db.sqlite3
python manage.py migrate

# Configure project/.env
dotenv="project/.env"
if [ ! -f dotenv ]; then
    touch ${dotenv}
    secret=$(venv/bin/python manage.py generate_secret_key)
    echo "DJANGO_SECRET_KEY=\"${secret}\"" >> ${dotenv}
    echo "DJANGO_DEBUG=true" >> ${dotenv}
    echo "BOOTSTRAP=bs5" >> ${dotenv}
fi

# Runserver and test
python manage.py runserver
