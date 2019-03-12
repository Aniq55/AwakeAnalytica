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

        unix_time =  (self.filename.split('/')[-1])[0:19]

        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        c.execute('''CREATE TABLE alldata0 (location text, type text, size text, shape text, data_type text, unit_time text)''')

        input_file = h5py.File(self.filename, 'r')

        def traverse(path, element):
            if isinstance(element, h5py.Dataset):
                try:
                    data_type = element.dtype
                except Exception as e:
                    data_type = str(e)

                c.execute('''INSERT INTO alldata0 VALUES (?,'Dataset',?,?,?,?)''', (str(path), str(element.size), str(element.shape), str(data_type), unix_time))
            else:
                c.execute('''INSERT INTO alldata0 VALUES (?,'Group','','','',?)''',(str(path), unix_time))

        input_file.visititems(traverse)

        conn.commit()
        conn.close()
