import os
import pathlib

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader

load_dotenv()
TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../templates")

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

# Application
APP_NAME = "TIZA" + " " + os.environ.get("DEBUG")
APP_ROOT = pathlib.Path(__file__).parent
API_V1_STR = "/api/v1"

admin_login = os.environ.get("ADMIN_LOGIN")
admin_password = os.environ.get("ADMIN_PASSWORD")

# Database

# db_main
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASS")
db_host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")
db_port = os.environ.get("DB_PORT")

# Otherwise

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG_ADMIN = os.environ.get("DEBUG_ADMIN", False)

#BTK
link_lk_btk = os.environ.get("BTK_LINK")
qr_link_1c = os.environ.get("QR_LINK_1C")