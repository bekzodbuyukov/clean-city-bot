from .strings import strings
from db import db_controller


def get_string(key, user_id):
    """ Function for returning needed text for User interface """
    language = db_controller.get_data(user_id=user_id, needed_column="language")
    if not language:
        language = "oz"
    return strings[language][key]


def get_string_by_language(key, language):
    """ Function for returning needed text for User interface just by language code """
    if not language:
        language = "oz"
    return strings[language][key]


if __name__ == "__main__":
    pass
    # get_string("test", 1009755188)
