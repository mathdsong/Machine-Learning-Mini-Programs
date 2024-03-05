# # What I modified:
# 1. Assign some treasure points if a Hero player reaches the secret portal.
# 2. Incorporate a looping structure with the game application to allow
#    for repeated player interaction. The loop can exit once a Hero reaches the secret portal.
# 3. Diminish a Hero player’s health if they come into proximity with a Zombie.
# 4. Using the NumPy library, alter some of the original functions that exhibit vector operations,
#    such as vector norm and the dot product, to now use intrinsic NumPy operations.


import random
import numpy as np

# Bots and Heroes: Cartesian Positioning with Arrays / Vectors

# Part 1: the initial settings
size = 2
## initialized treasure and healthPoint
treasure = 0
healthPoint = 100

# bots: initial 2D positions (x, y)
Zombie = np.array([random.choice(range(1, 3)) for i in range(0, size)])

# protagonists: initial 2D positions (x, y)
Hero = np.array([random.choice(range(1, 3)) for i in range(0, size)])

# portal: the secret location of the treasure
portal = np.array([random.choice(range(1, 3)) for i in range(0, size)])

# Part 2: the function definitions

# function to change player position
def movePlayer(vecA, vecB) :
    pass

# compute the distance between players
def vecDistance(vecA, vecB) :
    dist = np.dot(vecA - vecB, vecA - vecB)**(0.5)
    return dist

# the length of the vector
def vecLength(vec) :
    norm = np.dot(vec, vec)**(0.5)
    return norm

# determine player's position
def whereAmI(player, vecA) :
    msg = "" + player
    print (msg, "(", vecA[0], ",", vecA[1], ")")

# Part 3: the game play

# the starting locations
whereAmI("Initial location for Zombie:", Zombie)
whereAmI("Initial location for Hero:", Hero)
whereAmI("portal location:", portal)

# distances between players and the portal
zombieDist = vecDistance(Zombie, portal)
heroDist = vecDistance(Hero, portal)
heroZombieDist = vecDistance(Hero, Zombie)


# Incorporate a looping structure with the game application to allow
# for repeated player interaction. The loop can exit once a Hero
# reaches the secret portal.
round = 0
while (healthPoint > 0 and heroDist > 0) :
  round += 1
  # Diminish a Hero player’s health point by 20 if they come into proximity with a Zombie.
  if (heroZombieDist == 0):
    whereAmI("Zombie at round " + str(round) + ":", Zombie)
    whereAmI("Hero at around " + str(round) + ":", Hero)
    healthPoint -= 20
    print("Hero health points left:", healthPoint)
    if (healthPoint <= 0):
      print("Hero has been defeated!")
      break
  else:
    # otherwise, we regenerate Hero and Zombie's location
    Hero = np.array([random.choice(range(1, 3)) for i in range(0, size)])
    Zombie = np.array([random.choice(range(1, 3)) for i in range(0, size)])
    zombieDist = vecDistance(Zombie, portal)
    heroDist = vecDistance(Hero, portal)
    heroZombieDist = vecDistance(Hero, Zombie)
    whereAmI("Zombie at round " + str(round) + ":", Zombie)
    whereAmI("Hero at around " + str(round) + ":", Hero)



# Assign some treasure points if a Hero player reaches the secret portal.
if (heroDist == 0) :
    treasure = 10000000
    print("Hero got: " + str(treasure) + " treasure points!")
