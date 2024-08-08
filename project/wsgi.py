import os
import sys
from pathlib import Path

import dotenv
from django.core.wsgi import get_wsgi_application


CURR_DIR = Path(__file__).resolve(strict=True).parent
REPO_DIR = CURR_DIR.parent


def addpath(path):
    pathstr = path if hasattr(path, "lower") else str(path)
    if pathstr not in sys.path:
        print(f"addpath({pathstr})")
        sys.path.insert(0, pathstr)


dotenv.load_dotenv(Path(CURR_DIR, ".env"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
os.environ.setdefault("DJANGO_PYTHON_PATH", str(REPO_DIR))

addpath(REPO_DIR)

application = get_wsgi_application()
