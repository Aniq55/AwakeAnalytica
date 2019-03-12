"""
HDF to CSV conversion
"""

from analytica.hdf_reader import Hdf_reader


h= Hdf_reader()

# Provding Absolute Paths
h.filename = '/media/aniq55/WORK/GSOC2019/AwakeAnalytica/data/hdf/1541962108935000000_167_838.h5'
h.csvpath = '/media/aniq55/WORK/GSOC2019/AwakeAnalytica/data/csv/'

# h.hdf2csv()

"""
CSV to Mongo # DEBUG:
"""
