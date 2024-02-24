import os
import sys
from pathlib import Path

import dotenv
from django.core.wsgi import get_wsgi_application


def addpath(path):
    if path not in sys.path:
        print(f"--- PATH +{path}")
        sys.path.insert(0, path)


CURR_DIR = Path(__file__).resolve(strict=True).parent
dotenv.load_dotenv(Path(CURR_DIR, ".env"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
os.environ.setdefault("DJANGO_PYTHON_PATH", str(CURR_DIR.parent))

addpath(CURR_DIR.parent)

application = get_wsgi_application()
