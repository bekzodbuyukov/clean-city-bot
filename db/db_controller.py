from tinydb import TinyDB, Query

db = TinyDB('db.json')
db_query = Query()


class UserModel:
    """ The model for creating and manipulating with Users' data """

    def __init__(self):
        """ The default initialization function """
        self.id = 0
        self.language = 'kz'
        self.phone_number = 0

    def set_id(self, user_id):
        """ The function for setting user's id """
        self.id = user_id

    def set_language(self, user_language):
        """ The function for setting the user's language """
        self.language = user_language

    def set_phone_number(self, user_phone_number):
        """ The function for setting the user's phone number """
        self.phone_number = user_phone_number

