import os
import dotenv

dirname = os.path.dirname(__file__)

try:
    dotenv.load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.db"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)
EXPORT_DIRECTORY = os.path.join(dirname,"..","exports")
