import os

realTxt = "real.txt"
fakeTxt = "fake.txt"

try :
  num = int(input("how many records?"))
  count = 0
  if os.path.exists(realTxt) and os.path.exists(fakeTxt) :
    real_file = open(realTxt, "a")
    fake_file = open(fakeTxt, "a")
  else :
    real_file = open(realTxt, "w")
    fake_file = open(fakeTxt, "w")
    fields = ["Q1,", "Q2,", "Q3,", "Q4,", "Q5"]
    for i in range(5):
      real_file.write(fields[i])
      fake_file.write(fields[i])
    real_file.write("\n")
    fake_file.write("\n")

  while (count < num) :
    print("record #", count + 1)

    print("Q1. enter a letter")
    letter = input()
    print("<your letter>", letter)
    if (letter.isalpha() and len(letter) == 1) :
      real_file.write(letter + ",")
      fake_file.write(" ,")
    else :
      fake_file.write(letter + ",")
      real_file.write(" ,")
    print("*******************************************")

    print("Q2. enter an integer")
    number = input()
    print("<your number>", number)
    try :
      toNumber = float(number)
      if (toNumber % 1 == 0) :
        real_file.write(number + ",")
        fake_file.write(" ,")
      else :
        fake_file.write(number + ",")
        real_file.write(" ,")
    except ValueError:
      fake_file.write(number + ",")
      real_file.write(" ,")
    print("*******************************************")

    print("Q3. enter a Yes or No")
    answer = input().upper()
    print("<your answer>", answer)
    if (answer == 'YES' or answer == 'NO') :
      real_file.write(answer + ",")
      fake_file.write(" ,")
    else :
      fake_file.write(answer + ",")
      real_file.write(" ,")
    print("*******************************************")

    food_category = ['FRUITS', 'VEGETABLES', 'NUTS', 'DIARY']
    print("Q4. enter one of your favorite food categories from: " + food_category[0] + ", " + food_category[1] + ", " + food_category[2] + " and " + food_category[3])
    food = input()
    food_upperCase = food.upper()
    print("<your choice of lunch>", food_upperCase)
    if (food_upperCase in food_category) :
      real_file.write(food_upperCase + ",")
      fake_file.write(" ,")
    else :
      fake_file.write(food + ",")
      real_file.write(" ,")
    print("*******************************************")

    sports_teams = ['MLB', 'NBA', 'NFL', 'NHL']
    print("Q5. enter a sports team from: " + sports_teams[0] + ", " + sports_teams[1] + ", " + sports_teams[2] + " and " + sports_teams[3])
    team = input().upper()
    print("<your sports team>", team)
    if (team in sports_teams) :
      real_file.write(team + "\n")
      fake_file.write("\n")
    else :
      fake_file.write(team + "\n")
      real_file.write("\n")
    print("*******************************************")
    count += 1
except IOError:
  print("file appears to not exist!")