import os
from os.path import dirname, join

from dotenv import load_dotenv

load_dotenv(verbose=True)

envs_dir = join(dirname(__file__), ".envs")

common_env = join(envs_dir, "common.env")
load_dotenv(common_env)

dotenv_path = join(envs_dir, "{}.env".format(os.environ.get("environment")))
load_dotenv(dotenv_path, override=True)

DB_DRIVER = os.environ.get("DB_DRIVER")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
BUCKET_NAME = os.environ.get("BUCKET_NAME")
REGION_NAME = os.environ.get("REGION_NAME")

# debug
print(os.environ.get("environment"))
print(BUCKET_NAME)
print(REGION_NAME)
