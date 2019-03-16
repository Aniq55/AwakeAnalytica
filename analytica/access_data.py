from analytica.db_reader import Db_reader
from analytica.utils import *

class Access_data:

    def __init__(self):
        db_path = 'data/db/example.db'

        self.db= Db_reader()

        self.db.dbname = db_path
        self.db.conn2db()


    def find(self, keyword, start_date=None, end_date=None):
        print_dict(self.db.match_keyword(keyword, start_date, end_date))

    def load(self, table, data_name):
        pass
