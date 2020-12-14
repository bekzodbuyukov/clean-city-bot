import sqlite3

connection = None


def get_connection():
    global connection
    if connection is None:
        connection = sqlite3.connect('data.db')
    return connection


def init_db(force: bool = False):
    conn = get_connection()

    c = conn.cursor()

    if force:
        c.execute("DROP TABLE IF EXISTS user_data")

    c.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            id              INTEGER PRIMARY KEY,
            user_id         INTEGER NOT NULL,
            phone_number    INTEGER,
            language        TEXT NOT NULL
        )
    ''')

    conn.commit()


def add_data(user_id: int, phone_number: int, language: str):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO user_data (user_id, phone_number, language) VALUES (?, ?, ?)",
              (user_id, phone_number, language))
    conn.commit()


if __name__ == "__main__":
    init_db()

    add_data(user_id=123, phone_number=998936137878, language="oz")

# from tinydb import TinyDB, Query
#
#
# db = TinyDB('db.json')
# db_query = Query()
#
#
# class UserModel:
#     """ The model for creating and manipulating with Users' data """
#
#     def __init__(self):
#         """ The default initialization function """
#         self.id = 0
#         self.language = 'oz'
#         self.phone_number = 0
#
#     def set_id(self, user_id):
#         """ The function for setting user's id """
#         self.id = user_id
#
#     def set_language(self, user_language):
#         """ The function for setting the user's language """
#         self.language = user_language
#
#     def set_phone_number(self, user_phone_number):
#         """ The function for setting the user's phone number """
#         self.phone_number = user_phone_number
#
#
# def get_user_language(user_id):
#     user = db.get(db_query.id == user_id)
#     return user
