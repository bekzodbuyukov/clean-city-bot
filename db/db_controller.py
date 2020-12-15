import sqlite3

connection = None


def ensure_connection(function):
    """ Function for ensuring database connection """
    def make_connection(*args, **kwargs):
        with sqlite3.connect('/home/bek/myFiles/clean-city-bot/data.db') as conn:
            result = function(*args, conn=conn, ** kwargs)
            return result
    return make_connection


@ensure_connection
def init_db(conn, force: bool = False):
    """ Function for initializing database
    if force = True, then database will be dropped
    and new one will be created
    """
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


@ensure_connection
def add_data(conn, user_id: int, phone_number: int, language: str):
    """ Function for adding data of current User """
    c = conn.cursor()
    c.execute("INSERT INTO user_data (user_id, phone_number, language) VALUES (?, ?, ?)",
              (user_id, phone_number, language))
    conn.commit()


@ensure_connection
def update_data(conn, user_id: int, updating_column: str, updating_value):
    """ Function for Updating information of current User """
    c = conn.cursor()

    c.execute(f"UPDATE user_data SET {updating_column} = ? WHERE user_id = ?",
              (updating_value, user_id))
    conn.commit()


@ensure_connection
def get_data(conn, user_id: int, needed_column: str):
    """ Function for getting information of current User """
    c = conn.cursor()

    c.execute(f"SELECT {needed_column} FROM user_data WHERE user_id = ?",
              (user_id,))

    (result, ) = c.fetchone()
    return result


@ensure_connection
def find_user(conn, user_id: int):
    """ Function for checking if user exists """
    c = conn.cursor()

    c.execute(f"SELECT EXISTS (SELECT * FROM user_data WHERE user_id = ?)",
              (user_id,))

    (result, ) = c.fetchone()
    return result


@ensure_connection
def delete_data(conn, user_id: int):
    c = conn.cursor()

    c.execute(f"DELETE FROM user_data WHERE user_id = {user_id}")
    conn.commit()


if __name__ == "__main__":
    init_db()

    # add_data(user_id=123, phone_number=0, language="oz")
    # update_data(user_id=123, updating_column="language", updating_value="uz")
    # print(get_data(user_id=123, needed_column="phone_number"))
    # print(find_user(user_id=1009755188))
    # delete_data(user_id=1009755188)
