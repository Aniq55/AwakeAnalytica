""" TASK
Search keyword: streakImage
Date range: 2018-11-10 to 2018-11-12

Display: all results, table wise.

"""

from analytica.access_data import *
from analytica.utils import *

# Setup the database
setup_database()

adata= Access_data()

# Finding data
adata.find(keyword='streakImage', start_date="2018-11-10", end_date="2018-11-13")

# Loading data
x= adata.load(table='T_1541962108935000000_167_838', data_name='AwakeEventData/XMPP-STREAK/StreakImage/streakImageData')
