class Hdf_reader:

    def __init__(self):
        self.filename= None
        self.dbname= None
        self.csvpath= None


    def hdf2csv(self):
        """
        Reads the hdf file at self.filename and stores its csv details equivalent at
        the output directory
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

    def csv2db(self):
        import sqlite3
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        # Create table if it does not exist
        # c.execute('''CREATE TABLE alldata3 (location text, type text, size real, shape text, data_type text, unit_time text)''')
        unix_time =  (self.filename.split('/')[-1])[0:19]
        # Store all entries from the csv file or go for direct storage
        c.execute('''INSERT INTO alldata3 VALUES ('AwakeEventData/XUCL-SPECTRO/BinningSetting/hend','Dataset',1,"(1,)",'int32', %s)'''%(unix_time))
        conn.commit()
        conn.close()
