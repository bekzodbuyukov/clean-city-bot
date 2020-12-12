from db.db_controller import db, db_query


def get_string(key, user_id):
    current_user = db.get(db_query.id == user_id)

    print(current_user[0]["language"])


get_string("test", 1009755188)
