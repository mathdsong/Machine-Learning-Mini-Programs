# program to read from a file
# strName = "c:\\temp\\ratings.txt"
strName = "ratings.txt"

def checkIfMale(gender) :
  if (gender == 'M') :
    return True
  else :
    return False

try :
    file = open(strName, "r")
    field1 = ""; field2 = ""; field3 = ""
    field4 = ""; field5 = ""; field6 = ""; field7 = ""

    count = 0; total_rating = 0; avg_rating = 0; male_voters = 0; female_voters = 0; range40To49 = 0

    countForDifferentGroupsDict = {
      # for each array, the 0 index will be the total count for this age group, the index 1 will be the male count for this age group
      # for example, "3" : [9, 5] means that for the age group of 30 to 39, total count is 9, and 5 are male.
      "1": [0, 0],
      "2": [0, 0],
      "3": [0, 0],
      "4": [0, 0],
      "5": [0, 0],
      "6": [0, 0],
      "7": [0, 0],
      "8": [0, 0]
    }

    countForDifferentMonthDict = {
      # count for different month period of votings
      "1" : [0, "01/01 - 01/31"],
      "2" : [0, "02/01 - 02/29"],
      "3" : [0, "03/01 - 03/31"],
      "4" : [0, "04/01 - 04/30"],
      "5" : [0, "05/01 - 05/31"],
      "6" : [0, "06/01 - 06/30"],
      "7" : [0, "07/01 - 07/31"],
      "8" : [0, "08/01 - 08/31"],
      "9" : [0, "09/01 - 09/30"],
      "10" : [0, "10/01 - 10/31"],
      "11" : [0, "11/01 - 11/30"],
      "12" : [0, "12/01 - 12/31"]
    }

    for line in file :
        count += 1
        fields = line.split(",")
        field1 = fields[0]
        field2 = fields[1].lstrip()
        field3 = fields[2].lstrip()
        field4 = fields[3].lstrip()
        field5 = fields[4].lstrip()
        field6 = fields[5].lstrip()
        field7 = fields[6].lstrip()

        if (count > 1) :
          total_rating += float(field2)
          if (checkIfMale(field5)) :
            male_voters += 1
          else :
            female_voters += 1

          if (int(field6) <= 49 and int(field6) >= 40) :
            range40To49 += 1

          # update the dictionary to collect total amout of voters and male voters for each age group:
          for i in range(1, 9) :
            if (int(field6) // 10 == i) :
              countForDifferentGroupsDict[str(i)][0] += 1
              if checkIfMale(field5):
                countForDifferentGroupsDict[str(i)][1] += 1
              break

          # update the dictionary of each month ratings:
          month = field4[0: 2]
          for i in range(1, 13) :
            if (month[0] == '0' and int(month) == i) :
              countForDifferentMonthDict[month[1]][0] += 1
            if (month[0] == '1'and int(month) == i) :
              countForDifferentMonthDict[month][0] += 1


        print (field1 + "\t" + field2 + "\t" + field3 + "\t" +
               field4 + "\t" + field5 + "\t" + field6 + "\t" + field7)

    avg_rating = total_rating / (count-1)

    print("****************************************************")
    print()
    print("Data Analysis: ")
    print()
    print("total rating: " , total_rating)
    print("total people: " , count - 1)
    print("average rating: " , avg_rating)
    print("male voters: " , male_voters)
    print("female voters: " , female_voters)
    print("range 40 to 49: " , range40To49)
    # print("total voters and male voters for different age groups: ", countForDifferentGroupsDict)
    # print("rating counts for each month period: ", countForDifferentMonthDict)
    print("****************************************************")
    print()
    print("Artificial Intelligence: prediction on the genre for different age groups:")
    print()
    for key, value in countForDifferentGroupsDict.items():
      if (value[0] > 2 * value[1]) :
        # if total voters more than double of male voters for this age group, means female ratio is higher for this age group:
        print(key + ". romance movies preffered by group of age between " + key + "0 and " + key + "9")
      elif (value[0] < 2 * value[1]) :
        print(key + ". action movies preffered by group of age between " + key + "0 and " + key + "9")
      else :
        if (value[0] > 0) :
          print(key + ". both romance and action movies are popular between " + key + "0 and " + key + "9")
        else :
          print(key + ". no data avaliable between " + key + "0 and " + key + "9")
    print("****************************************************")
    print()
    print("Aritificial Intelligence: prediction on the movie releasing year:")
    print()
    for value in countForDifferentMonthDict.values():
      if (value[0] / (count - 1) >= 0.75) :
        print("Movie year likely to be within last 2 years for post dates: " + value[1])
      elif (value[0] / (count - 1) < 0.75 and value[0] / (count - 1) >= 0.5) :
        print("Movie year likely to be within last 7 years for post dates: " + value[1])
      else :
        if (value[0] > 0) :
          print("Movie year likely to be within beyond 7 years for post dates: " + value[1])
        else :
          print("No data avaliable for post dates: " + value[1])
    print("****************************************************")


    file.close()

except IOError :
    print ("file appears to not exist!")


