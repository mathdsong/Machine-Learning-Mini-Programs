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

    for field in tokens:
      if row == 0 :
        if col == 3:
          file.write("TIMESTAMP," + field + ",")
        else :
          file.write(field + ",")
      else :
        if col == 3:
          date_obj = datetime.strptime(datetime_string, "%m/%d/%y%H:%M:%S %p")
          timestamp = int(date_obj.timestamp())
          file.write(str(timestamp) + "," + field + ",")
        else :
          file.write(field + ",")
      col += 1

    line = f.readline()
    col = 0
    row += 1
  f.close()


