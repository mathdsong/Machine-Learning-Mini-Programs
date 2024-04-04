import math
import pandas as pd
# data frames and the Rule of 72

# available investment amounts
deposits = [1000, 2000, 3000, 4000, 5000, 7800]
# available annual interest rates
rates = [0.03, 0.04, 0.045, 0.0510, 0.06]
# list of current clients
investors = ["Sally", "Barnabas", "Donald", "Lisa", "Julio"]

# routine for simple interest
def simpInt(principal, rate, time) :
    futureVal = principal * (1 + rate * time)
    return futureVal

# routine for compound interest
def compInt(principal, rate, freq, time) :
    cmpAmt = principal * (1 + rate / freq) ** (freq * time)
    return cmpAmt

# routine for precise formula to double investment
def doubleTime(rate, freq) :
    dblMe = math.log(2) / math.log(1 + rate / freq)
    return dblMe

# routine for precise formula to triple investment
def tripleTime(rate, freq) :
    tripleMe = math.log(3) / math.log(1 + rate / freq)
    return tripleMe

def ruleOf72(rate) :
    doubleYr = 72 / (rate * 100)
    return doubleYr

# variables for the data frame
# cash = 0
# time = 0
rows = 5
cols = 5

# create an original data which contains name, principals, ruleOf72 result, precise double time, precise triple time:
data = []
total_time = 0

for r in range(rows) :
  data.append([investors[r], deposits[r], rates[r], ruleOf72(rates[r]), doubleTime(rates[r], 1), tripleTime(rates[r], 1)])
  total_time += ruleOf72(rates[r])

avg_time = total_time / 5

# generate a data frame
df = pd.DataFrame(data, columns = ["name", "principals", "rates", "ruleOf72", "preciseDoubleTime", "preciseTripleTime"])

# average time of doubling 5 investors' time:

print("*******************************************************")
print("original data: ")
print(data)
print("*******************************************************")
print("original data frame: ")
print(df)
print("*******************************************************")
print("average time: ")
print(avg_time)
print("*******************************************************")
print("slicing the first 3 rows: ")
df1 = df.iloc[0:3]
print(df1)
print("*******************************************************")
print("slicing the first 3 columns: ")
df2 = df.iloc[:, 0:3]
print(df2)
print("*******************************************************")
print("slicing the first 2 row and first 2 columns: ")
df3 = df.iloc[0:2, 0:2]
print(df3)
print("*******************************************************")

# # display the data frame
# for r in range(rows) :
#     print (r + 1, "\t", end = "")
#     for c in range(cols) :
#         print (dff[r][c], "\t", end = "")
#     print ()
# print ()


