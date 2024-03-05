import random
import datetime
import matplotlib.pyplot as pyplot

# display the current date
currentDate = datetime.datetime.today().strftime ("%B %d %Y")
print ("Report Date: " + str(currentDate) )
print ("***************Welcome***************")
print ("-------------------------------------\n")
#random.seed ()
# define the list of categories
categories = ["ambience", "cuisine", "location", "menu", "prices", "service", "Décor"]
# decor
# print (categories)
# set the number of patron responses
size = 50
# initialize the customer ratings list
custRatings = [0] * size
# print (custRatings)
# generate the random ratings
custRatings = [random.choice(range(1, 8)) for i in range(0, size)]
print ("[ customer responses ]")
print (custRatings)
# copy the categories and include spaces ( for printing purposes )
cats = ["ambience", "cuisine ", "location", "menu", "prices", "service", "Décor"]
# groupings
print ()

# summarize the customer ratings
summary = [0, 0, 0, 0, 0, 0, 0]
asterisks = ["", "", "", "", "", "", ""]
for i in range(len(custRatings)) :
  summary[custRatings[i] - 1] += 1
  asterisks[custRatings[i] - 1] += "*"
print ("[ grouped responses ]")
print (summary)
print ("\n")
print ("[ tally ]", "\n")
print ("-------------------------------------")
# display the frequency chart
for i in range(len(asterisks)) :
  print (cats[i], "\t", asterisks[i], sep = "")
print ()

print ("-------------------------------------")
# summary of data analysis
summary_max = max(summary)
summary_min = min(summary)
print ("[ greatest category ]")
print (summary_max)
print ("[ least category ]")
print (summary_min)
# the range compares the highest value to the lowest value
summary_range = summary_max - summary_min
print("The range is: ", summary_range)
max_labels = ""
min_labels = ""
for i in range(len(cats)) :
  if summary[i] == summary_max :
    max_labels += cats[i] + ", "
  elif summary[i] == summary_min :
    min_labels += cats[i] + ", "
print("the label of least is(are): ", max_labels[:len(max_labels) - 2])
print("the label of greatest is(are): ", min_labels[:len(min_labels) - 2])
print ("-------------------------------------")
# assign weights for the ratings
weights = [0.09, 0.21, 0.22, 0.14, 0.13, 0.18, 0.03]
weighted_avg = 0
for i in range(len(weights)) :
  weighted_avg += weights[i] * summary[i]
print ("the weighted average is: ", weighted_avg)

# matplotlib plot
pyplot.scatter(categories, summary, label="Scatter Plot", color="m")
pyplot.xlabel("Categories")
pyplot.ylabel("Summary")
pyplot.title("Categories - Summary plot")
pyplot.show()
