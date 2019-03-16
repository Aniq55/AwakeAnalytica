# db_path = 'data/db/example.db'
#
# from analytica.db_reader import Db_reader
#
# db= Db_reader()
#
# db.dbname = db_path
# db.conn2db()
# # T_1541962108935000000_167_838
# # q= 'SELECT * FROM ALLDATA WHERE data_date BETWEEN "2015-01-01" AND "2016-01-01"'
#
# from analytica.utils import *
#
# # print_result(db.fetch(q))
#
# # tables_filtered = db.filter_by_date(start_date= "2018-11-11", end_date= "2018-11-12")
# tables_filtered= db.match_keyword('streakImage')
# print_dict(tables_filtered)

""" TASK
Search keyword: streakImage
Date range: 2018-11-10 to 2018-11-12

Display: all results, table wise.

"""

from analytica.access_data import *

ad= Access_data()

ad.find('streakImage')











# conn= sq.connect(db_path)
#
# c= conn.cursor()
#
# # Ideally, fetch tables filtered by date and time
# c.execute('SELECT * FROM ALLDATA')
#
# table_name, data_path, _ = c.fetchone()
#
# print(table_name)
# print(data_path)
#
# # Ideally, filter by search keyword
# c.execute('SELECT * FROM {}'.format(table_name))
# print(c.fetchone())
