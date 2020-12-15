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
    
    print(f"{db_controller.get_data(user_id=user_id, needed_column='language')}")


if __name__ == "__main__":
    get_string("test", 1009755188)
