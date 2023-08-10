import os
import pathlib

# Application

APP_NAME = "My App"
APP_ROOT = pathlib.Path(__file__).parent
API_V1_STR = "/api/v1"

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