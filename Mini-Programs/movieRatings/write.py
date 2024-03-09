import os
# program to write to a file
strName = "ratings.txt" # strName = "c:\\temp\\ratings.txt"

try :
    num = int(input("how many records? "))
    count = 0
    if os.path.exists(strName) :
        file = open(strName, "a")
        # file.write("\n")
        while (count < num) :
            print ("record", count + 1)
            for index in range(0, 7) :
                val = input("enter a value: ")
                if (index < 7 - 1) :
                    file.write(val + ", ")
                else :
                    file.write(val + "\n")
            count = count + 1
    else :
        file = open(strName, "w")
        field1 = "Member,"
        field2 = "Rating,"
        field3 = "Crew,"
        field4 = "Date,"
        field5 = "Gender,"
        field6 = "Age,"
        field7 = "Demographics"
        file.write(field1)
        file.write(field2)
        file.write(field3)
        file.write(field4)
        file.write(field5)
        file.write(field6)
        file.write(field7 + "\n")

        while (count < num) :
            print ("record", count + 1)
            for index in range(0, 7) :
                val = input("enter a value: ")
                if (index < 7 - 1) :
                    file.write(val + ", ")
                else :
                    file.write(val + "\n")
            count = count + 1

    file.close()
except IOError :
    print ("file appears to not exist!")