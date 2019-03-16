def file2utc(filepath):
    """
    Converts the first 19 digits of the hdf filename (filepath) to UNIX time
    and returns the UTC timestamps.
    """
    import pytz
    from datetime import datetime
    filename = (filepath.split('/')[-1])[0:19]
    time_ns = float(filename)/(10**9)
    return pytz.utc.localize(datetime.fromtimestamp(time_ns))

def validate_query(query):
    """
    Checks whether the sqlite query is valid or not
    """
    return query

def print_result(result):
    """
    Prints the result row by row
    """
    for row in result:
        print(row)

def inquotes(s):
    return '"'+ s + '"'
