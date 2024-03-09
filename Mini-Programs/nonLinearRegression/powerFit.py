import matplotlib.pyplot as mp
import math
import numpy as np

# (x, y) data points:
# (1, 8), (2, 11), (3, 19), (4, 20), (5, 18), (6, 22)
xList = [1, 2, 3, 4, 5, 6]
yList = [8, 11, 19, 20, 18, 22]
lnx = []
lny = []
l = len(xList)
mp.plot(xList, yList, "go")
# g = green colored markers
# o = markers without smooth line

# axis titles
mp.xlabel("index")
mp.ylabel("quantity")

# horizontal scale: 0 to 10
# vertical scale: 0 to 25
mp.axis([0, 10, 0, 25])
# mp.show()

# define a function to perform power fit:
def powerFit() :

  for i in range(l) :
    lnx.append(math.log(xList[i]))
    lny.append(math.log(yList[i]))
  np_lnx = np.array(lnx)
  np_lny = np.array(lny)

  b = (l * np.dot(np_lnx, np_lny) - np.sum(np_lnx) * np.sum(np_lny)) / (l * np.dot(np_lnx, np_lnx) - np.dot(np.sum(np_lnx), np.sum(np_lnx)))
  a = (np.sum(np_lny) - b * np.sum(np_lnx)) / l
  A = math.exp(a)

  print("the predicted power of the power fit model is: %0.3f" % b)
  print("the predicted coefficient of the power model is: %0.2f" % A)
  print("power fit model: y = %0.2fx^%0.3f" % (A, b))
powerFit()