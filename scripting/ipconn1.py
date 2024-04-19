# prints the date and time fields of each line including headings "DATE" and "TIME"
f = open('connect.csv', 'r')
line = f.readline()
while line:
  tokens = line.split(",")
  print(tokens[1], " ", tokens[2])
  line = f.readline()
f.close()