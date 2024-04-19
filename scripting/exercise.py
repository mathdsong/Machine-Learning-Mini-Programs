# Read in the file
with open('connect.csv', 'r') as file :
  filedata = file.read()
# Replace the target string
filedata = filedata.replace(',', ' ')
# Write the file out
with open('connect2.csv', 'w') as file:
  file.write(filedata)

# copy the contents of the file "connect2.csv" to the output including the header
f = open('connect2.csv', 'r')
line = f.readline()
while line :
  print(line.strip())
  line = f.readline()
f.close()

# header and the last line are excluded
f = open('connect2.csv', 'r')
while f.readline() :
  line = f.readline()
  print(line.strip)
f.close()

# timestamp
import time
import datetime
import os
print("Time in seconds since the epoch: %s" %time.time())
now = datetime.datetime.now()
print(now.strftime("%a %b %d %H: %M: %S %Z %Y"))
print("or using the system call")
os.system("date")
