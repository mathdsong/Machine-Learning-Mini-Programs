# program for Linear Regression

# define the data lists and their lengths
xVals = [1, 2, 3, 4, 5, 6]
yVals = [10, 12, 15, 13, 21, 19]
m = len(xVals)
n = len(yVals)

# define a function to perform linear regression
def LinReg() :
    global xVals, yVals
    global m, n
    sumx = 0; sumy = 0; sumxy = 0; sumxx = 0
    slope = 0; yInt = 0

    for index in range(n) :
        sumx += xVals[index]
        sumy += yVals[index]
        sumxy += xVals[index] * yVals[index]
        sumxx += xVals[index] * xVals[index]
    slope = (n * sumxy - sumx * sumy) / (n * sumxx - sumx * sumx)
    yInt = (sumy * sumxx - sumx * sumxy) / (n * sumxx - sumx * sumx)

    print ("the predicted slope is: %0.2f" % slope)
    print ("the predicted intercept is: %0.2f" % yInt)
    print ("")
    print ("linear model: y = %0.2fx + %0.2f" % (slope, yInt))
    print ("")
    # perform interpolation and extrapolation here

# call the Linear Regression function
LinReg()
