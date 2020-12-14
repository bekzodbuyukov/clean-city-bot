# from . import strings
from db import db_controller


def get_string(key, user_id):
    # users = db.all()
    #
    # for user in users:
    #     if user["id"] == user_id:
    #         print(f"{user['phone_number']}")
    #
    # current_user = db.get(db_query.id == user_id)
    # print(f"til - {current_user}")

    print(f"{db_controller.get_user_language(user_id)}")


get_string("test", 1009755188)
