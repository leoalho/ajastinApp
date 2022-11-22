import sqlite3
import os

def connect():
  dirname = os.path.dirname(__file__)
  DATABASE_FILE_PATH = os.path.join(dirname, "..", "database.db")
  db = sqlite3.connect(DATABASE_FILE_PATH)
  return db

def initialize_users(db):
    db.execute("DROP TABLE IF EXISTS users;")
    db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT);")
    db.execute("INSERT INTO users(username) VALUES('Test')")

def all_users(db):
    users = db.execute("SELECT * FROM users").fetchall()
    return users





