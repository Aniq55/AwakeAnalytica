from analytica.constants import *
from analytica.hdf_reader import Hdf_reader
import glob
import pytz
from datetime import datetime

def file2utc(filepath):
    """
    Converts the first 19 digits of the hdf filename (filepath) to UNIX time
    and returns the UTC timestamps.
    """
    filename = (filepath.split('/')[-1])[0:19]
    time_ns = float(filename)/(10**9)
    return pytz.utc.localize(datetime.fromtimestamp(time_ns))

def validate_query(query):
    """
    Checks whether the sqlite query is valid or not
    """
    return query

def print_list(result):
    """
    Prints a list of tuples
    """
    for row in result:
        print(row)

def print_dict(result):
    """
    Prints a dictionary
    """
    for x in result.keys():
        print(x)
        print('--------------------------------')
        for y in result.get(x):
            print(y[0])
        print('================================')


def inquotes(s):
    return '"'+ s + '"'

def setup_database():
    """
    Sets up the databse from hdf file entries
    """
    h= Hdf_reader()
    h.dbname = DATABASE_PATH

    all_files = glob.glob(HDF_PATH +'*.h5')

    for file_name in all_files:
        h.filename = file_name
        h.hdf2db()
