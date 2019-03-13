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

        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        # Create table if not created
        table_name = 'T'+(self.filename.split('/')[-1])[0:19]
        c.execute('''CREATE TABLE IF NOT EXISTS ALLDATA (table_name text)''')
        c.execute("INSERT INTO ALLDATA VALUES ( ? )",(table_name,))

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
