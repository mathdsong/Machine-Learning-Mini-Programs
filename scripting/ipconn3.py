from time import time
from datetime import datetime
import math

f = open('connect-ts.csv', 'r')
first_timestamp = int(time()) #set as current timestamp
last_timestamp = 0

line = f.readline()
count = 0

while line:
  tokens = line.split(",")
  # find the first timestamp (smallest) and the last timestamp (largest)
  if (count > 0) :
    timestamp = int(tokens[3])
    if (timestamp < first_timestamp) :
      first_timestamp = timestamp
    if (timestamp > last_timestamp) :
      last_timestamp = timestamp
  line = f.readline()
  count += 1

f.close()
print(datetime.fromtimestamp(first_timestamp))
print(datetime.fromtimestamp(last_timestamp))

# convert the difference between first timestamp and last timestamp into "hh:mm:ss" format
def converter(timestamp1, timestamp2) :
  diff = abs(timestamp1 - timestamp2)
  hours = math.floor(diff / 3600)
  diff -= hours * 3600
  minutes = math.floor(diff / 60)
  seconds = diff - minutes * 60
  hms = 'The difference between these two timestamps in the form of "hh:mm:ss" is: {}:{}:{}'.format(hours, minutes, seconds)
  return hms


print(converter(first_timestamp, last_timestamp))
