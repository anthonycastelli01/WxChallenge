## Anthony Castelli WxChallenge Data Aggregator

import urllib
from time import gmtime, strftime

# Getting the current date
timestamp = strftime("%d%m%Y%H")
day = timestamp[:2]
month = timestamp[2:4]
year = timestamp[4:8]

# Dealing with hour conversions
hour = 3*((int(timestamp[8:10])/3) + 1)

if hour < 10:
    hour = "0" + str(hour)
else:
    hour = str(hour)

# Setting up data retrieval
city = raw_input("What is the city code you are forecasting for? >> ")

# Formatting the URLs where the data is stored
nam_data_url = year + month + day + hour + '_' + city + '.nam.html'
nam_url = 'http://www.meteo.psu.edu/data/weather/model/interpolated/' + nam_data_url

gfs_data_url = year + month + day + hour + '_' + city + '.gfs.html'
gfs_url = 'http://www.meteo.psu.edu/data/weather/model/interpolated/' + gfs_data_url

# Retrieving HTML pages
urllib.urlretrieve(nam_url, 'nam_data.html')
urllib.urlretrieve(gfs_url, 'gfs_data.html')

print("Data pages retrieved.\n")
