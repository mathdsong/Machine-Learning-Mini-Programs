from timeit import default_timer as timer

def main() :
    choice = int(input("enter your choice (1 or 2): "))
    maxReps = 31
    count = 0
    mult = 1
    nums = [1, 2, 3, 5, 6, 7, 8, 9]
    start = 0
    stop = 0
    # method 1
    if (choice == 1) :
        start = timer()
        for i in range(maxReps) :
            count = method1(count)
        stop = timer()
    # method 2
    elif (choice == 2) :
        start = timer()
        for i in range(maxReps) :
            mult = method2(mult)
        stop = timer()

    totalTime = stop - start
    print ("Total time: ", totalTime)
    print("count = " , count , " mult = " , mult)

def method1(count) :
    count += 2
    return count

def method2(mult) :
    mult *= 2
    return mult

main()




"""
related links:
1. https://www.guru99.com/timeit-python-examples.html
2. example from https://www.geeksforgeeks.org/timeit-python-examples/:

# importing the required module
import timeit

# code snippet to be executed only once
mysetup = "from math import sqrt"

# code snippet whose execution time is to be measured
mycode = '''
def example():
    mylist = []
    for x in range(100):
        mylist.append(sqrt(x))
'''

# timeit statement
print(timeit.timeit(setup=mysetup, stmt=mycode, number=10000))

3. https://stackoverflow.com/questions/63757763/timeit-and-its-default-timer-completely-disagree
"""

# from datetime import datetime
# import timeit
# s = '''
# def f():
#   myList = []
#   for n in range(5):
#       myList.append(n)
# '''
# t = timeit.timeit(stmt=s)
# print (t, "seconds")

# start_time = datetime.now()
# print("input some words:")
# x = input()

# time_elapsed = datetime.now() - start_time
# print(time_elapsed)
# print("Time elapsed(hh:mm:ss.ms): {}" . format(time_elapsed))
# print("Time elapsed(hh:mm:ss.ms):" , format(time_elapsed))