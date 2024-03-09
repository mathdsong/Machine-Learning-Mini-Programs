import matplotlib.pyplot as mp

# (x, y) data points:
# (1, 8), (2, 11), (3, 19), (4, 20), (5, 18), (6, 22)
xList = [1, 2, 3, 4, 5, 6]
yList = [8, 11, 19, 20, 18, 22]
mp.plot(xList, yList, "go")
# g = green colored markers
# o = markers without smooth line

# axis titles
mp.xlabel("index")
mp.ylabel("quantity")

# horizontal scale: 0 to 10
# vertical scale: 0 to 25
mp.axis([0, 10, 0, 25])
mp.show()