from random import randint as randomGen
dList = []
sb = ""
vertices = ["A", "B", "C", "D", "E", "F"]
discover = [" " for x in range(6)]
discover[0] = "located the hidden books"
discover[1] = "found the perpetrator's cigar ashes"
discover[2] = "discovered the missing lead pencil"
discover[3] = "seen the mysterious light"
discover[4] = "visited the favorite bakery"
discover[5] = "examined the stolen credit card"
clues = ["books", "cigar", "pencil", "light", "bakery", "credit card"]
for j in range(1, len(clues)) :
  dList.append(clues[j])
edges = {"AB", "AE", "AF", "BC", "BD", "BE", "CD", "CE", "DE", "EF"}
currVertex = "A"
nextVertex = ""
check = False
occur = set()
path = "A"

while (len(dList) > 0) :
  occur.add(currVertex)
  index = randomGen(1, 5)
  nextVertex = vertices[index]
  print("next vertext is: " + nextVertex)
  # check if path exists
  edge1 = edge2 = ""
  edge1 = currVertex + nextVertex
  edge2 = nextVertex + currVertex
  if (edge1 in edges) :
    print("travel to ..." + edge1 + " is OK")
    check = True
  elif (edge2 in edges) :
    print("travel to ..." + edge2 + " is OK")
    check = True
  else :
    print("edge doesn't exist")

  if (check == True) :
    path += " --> " + nextVertex
    # remove the clue from dList if never occured
    if (nextVertex not in occur) :
      dList.remove(clues[index])
      # find the corresponding clue
      print("Well done! You have" + discover[index])
      # obtain significance of the clue
      sb += clues[index]
      print("thus far we have these clues: " + sb)
      sb += ", "
    else :
      print("Clue '" + clues[index] +"' exists")
    currVertex = nextVertex
    check = False
    print(path)
  print()

