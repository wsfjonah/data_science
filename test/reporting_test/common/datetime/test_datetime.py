import datetime
import time

timestr = '10/Jun/2019:07:06:52 +0800'
timestr = '10/Jun/2019:07:06:52'

t = time.strptime(timestr, '%d/%b/%Y:%H:%M:%S')
dt = datetime.datetime.fromtimestamp(time.mktime(t))
print(type(t))
print(dt.replace(minute=0, second=0))
