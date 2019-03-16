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
