import sqlite3
import os

def connect():
    dirname = os.path.dirname(__file__)
    DATABASE_FILE_PATH = os.path.join(dirname, "..", "database.db")
    database = sqlite3.connect(DATABASE_FILE_PATH)
    return database

def initialize_users(database):
    database.execute("DROP TABLE IF EXISTS users;")
    database.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT);")
    database.execute("INSERT INTO users(username) VALUES('Test')")

def all_users(database):
    users = database.execute("SELECT * FROM users").fetchall()
    return users
