# program for Linear Regression
import math
import matplotlib.pyplot as mp
# define the data lists and their lengths
xVals = [1, 2, 3, 4, 5, 6]
yVals = [10, 12, 15, 13, 2, 19]
m = len(xVals)
n = len(yVals)
# plotting data:
mp.plot(xVals, yVals, "go")
mp.xlabel("index")
mp.ylabel("quantity")
mp.axis([0, 10, 0, 30])
mp.show()

# define a function to perform linear regression
def LinReg() :
    global xVals, yVals
    global m, n
    sumx = 0; sumy = 0; sumxy = 0; sumxx = 0; sumyy = 0
    slope = 0; yInt = 0

    for index in range(n) :
        sumx += xVals[index]
        sumy += yVals[index]
        sumxy += xVals[index] * yVals[index]
        sumxx += pow(xVals[index], 2)
        sumyy += pow(yVals[index], 2)
    # Predict slope, y-intercept, and compute correlation coefficient:
    slope = (n * sumxy - sumx * sumy) / (n * sumxx - sumx * sumx)
    yInt = (sumy * sumxx - sumx * sumxy) / (n * sumxx - sumx * sumx)
    r = (n * sumxy - sumx * sumy) / math.sqrt((n * sumxx - pow(sumx, 2)) * (n * sumyy - pow(sumy, 2)))
    rSquare = r ** 2
    print ("the predicted slope is: %0.2f" % slope)
    print ("the predicted intercept is: %0.2f" % yInt)
    print ("")
    print ("linear model: y = %0.2fx + (%0.2f)" % (slope, yInt))
    print ("the correlation coefficient is: %0.2f" % r)
    print ("the coefficient of Determination is: %0.3f" % rSquare)
    if (r >= 0.80 and r <= 1.00) :
        print("analysis: strong positive correlation")
    if (r <= -0.80 and r >= -1.00) :
        print("analysis: strong negative correlation")
    if (abs(r) < 0.80) :
        print("analysis: weak correlation")
    print("**************************************************************")
    # perform interpolation and extrapolation here
    xInterp = 0
    yInterp = 0
    msg = "please provide an x-value for interpolation: "
    xInterp = float(input(msg))
    yInterp = slope * xInterp + yInt
    print("interpolation results: %0.2f" % yInterp)
    print("**************************************************************")
    xExtrap = 0
    yExtrap = 0
    msg = "please provide an x-value for extrapolation: "
    xExtrap = float(input(msg))
    yExtrap = slope * xExtrap + yInt
    print("interpolation results: %0.2f" % yExtrap)



# call the Linear Regression function
LinReg()
