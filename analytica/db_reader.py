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
        from analytica.utils import validate_query
        # Ideally, check the validity of the query
        self.cursor.execute(validate_query(query))
        return self.cursor.fetchall()

    def filter_by_date(self, start_date, end_date):
        query= 'SELECT * FROM ALLDATA WHERE data_date BETWEEN {} AND {}'.format(start_date, end_date)
        tables= self.fetch(query)
        return tables

    def match_keyword(self, tables):
        pass
