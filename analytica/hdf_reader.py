class Hdf_reader:

    def __init__(self):
        self.filename= None
        self.dbname= None
        self.csvpath= None

    def hdf2csv(self):
        """
        Reads the hdf file at self.filename and stores its csv details equivalent at
        the output directory.
        """
        import h5py
        import pandas as pd

        output_path = self.csvpath + ((self.filename.split('/')[-1]).split('.'))[0] +'.csv'
        input_file = h5py.File(self.filename, 'r')

        rows = dict()

        def traverse(path, element):
            if isinstance(element, h5py.Dataset):
                try:
                    data_type = element.dtype
                except Exception as e:
                    data_type = str(e)

                rows[path] = ['Dataset', element.size, element.shape, data_type]
            else:
                rows[path] = ['Group', '','','']

        input_file.visititems(traverse)
        df = pd.DataFrame.from_dict(rows, orient='index', columns = ['type', 'size', 'shape', 'data_type'])
        df.to_csv(output_path, sep=',')


    def hdf2db(self):
        """
        Reads the hdf file at self.filename and stores its details in the database.
        """
        import h5py
        import pandas as pd
        import sqlite3
        from analytica.utils import file2utc

        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()

        table_name = 'T_'+(self.filename.split('/')[-1])[:-3]
        c.execute('''CREATE TABLE IF NOT EXISTS ALLDATA (table_name text, data_path text, data_date date)''')
        c.execute("INSERT INTO ALLDATA VALUES ( ?, ?, ? )",(table_name, self.filename, file2utc(self.filename)))
        conn.commit()

        c.execute('CREATE TABLE IF NOT EXISTS {} (location text, type text, size text, shape text, data_type text)'.format(table_name))

        input_file = h5py.File(self.filename, 'r')

        def traverse(path, element):
            if isinstance(element, h5py.Dataset):
                try:
                    data_type = element.dtype
                except Exception as e:
                    data_type = str(e)

                c.execute('''INSERT INTO {}  VALUES (?,'Dataset',?,?,?)'''.format(table_name),(str(path), str(element.size), str(element.shape), str(data_type)))
            else:
                c.execute('''INSERT INTO {}  VALUES (?,'Group','','','')'''.format(table_name),(str(path),))

        input_file.visititems(traverse)

        conn.commit()
        conn.close()
