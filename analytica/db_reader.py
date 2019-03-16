from analytica.utils import *

class Db_reader:

    def __init__(self):
        self.dbname= None
        self.connection= None
        self.cursor= None

    def conn2db(self):
        import sqlite3
        self.connection = sqlite3.connect(self.dbname)
        self.cursor = self.connection.cursor()

    def fetch(self, query):
        self.cursor.execute(validate_query(query))
        return self.cursor.fetchall()

    def filter_by_date(self, start_date, end_date):
        query= 'SELECT * FROM ALLDATA WHERE data_date BETWEEN {} AND {}'.format(inquotes(start_date), inquotes(end_date))
        return self.fetch(query)

    def match_keyword(self, keyword, start_date=None, end_date=None):
        if start_date is not None and end_date is not None:
            tables_list = [x[0] for x in self.filter_by_date(start_date, end_date)]
        else:
            tables_list = [x[0] for x in self.fetch('SELECT * FROM ALLDATA')]

        results= {}
        keyword= '%'+keyword+'%'

        for table in tables_list:
            results[table]= self.fetch('SELECT * FROM {} WHERE location LIKE {}'.format(table, inquotes(keyword)))

        return results

    def close(self):
        self.connection.close()
