from analytica.db_reader import *
from analytica.constants import *
from analytica.utils import *
import h5py

class Access_data:

    def __init__(self):
        db_path = DATABASE_PATH

        self.db= Db_reader()
        self.db.dbname = db_path
        self.db.conn2db()

    def find(self, keyword, start_date=None, end_date=None):
        print_dict(self.db.match_keyword(keyword, start_date, end_date))

    def load(self, table, data_name):
        path2table= (self.db.fetch('SELECT * FROM ALLDATA WHERE table_name LIKE {}'.format(inquotes(table)))[0])[1]
        data_file= h5py.File(path2table, 'r')
        return data_file[data_name]

    def close(self):
        self.db.close()
