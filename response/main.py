import os

real_file = open("real.txt", "r")
fake_file = open("fake.txt", "r")

print("enter a letter")
letter = input().upper()
print("<your letter>", letter)
if (letter.isalpha() and len(letter) == 1) :
  print("yes")
else :
  print("No")


print("enter an integer")
number = input()
print("<your number>", number)
try :
  number = float(number)
  if (number % 1 == 0) :
    print("it's an integer")
  else :
    print("it's a decimal")
except ValueError:
  print("it can't be converted into a number")


print("enter a Yes or No")
answer = input().upper()
print("<your answer>", answer)
if (answer == 'YES' or answer == 'NO') :
  print("yes")
else :
  print("no")


food_category = ['FRUITS', 'VEGETABLES', 'NUTS', 'DIARY']
print("enter one of your favorite food categories from: " + food_category[0] + ", " + food_category[1] + ", " + food_category[2] + ", " + food_category[3])
food = input().upper()
print("<your choice of lunch>", food)
if (food in food_category) :
  print("yes")
else :
  print("no")


sports_teams = ['MLB', 'NBA', 'NFL', 'NHL']
print("enter a sports team")
team = input().upper()
print("<your sports team>", team)
if (team in sports_teams) :
  print("yes")
else :
  print("no")




