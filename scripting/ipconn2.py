# add a new field "TIMESTAMP" into connect-ts.csv file between TIME and DURATION fields
from datetime import datetime

f = open('connect.csv', 'r')
line = f.readline()
row = 0
col = 0

with open('connect-ts.csv', 'w') as file:
  while line:
    tokens = line.split(",")
    date = tokens[1]
    time = tokens[2]
    datetime_string = date + time
    written_string = ""

    for field in tokens:
      if col == 3:
        if row == 0:
          written_string += ("TIMESTAMP," + field + ",")
        else :
          date_obj = datetime.strptime(datetime_string, "%m/%d/%y%H:%M:%S %p")
          timestamp = int(date_obj.timestamp())
          written_string += (str(timestamp) + "," + field + ",")
      else :
        written_string += (field + ",")
      col += 1

    written_string = written_string[:-1]
    file.write(written_string)
    line = f.readline()
    col = 0
    row += 1
  f.close()


