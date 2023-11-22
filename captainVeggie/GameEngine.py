import os
import random
from Captain import Captain
from Rabbit import Rabbit
from Veggie import Veggie
from FieldInhabitant import FieldInhabitant
# Aleese: I added this import statement because I edited printField() to just check if the current position has a
# FieldInhabitant rather than individually checking if it has a rabbit, captain, veg. However, Python would not
# recognize FieldInhabitant without importing it -- unsure why. I feel there should be a way to check this w/o importing.


# Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova
# Date: 11/18/2023
# Desc: Class file for 'GameEngine' class. This will contain initialization and running functions for the actual "Captain Veggie" game. Will be called in main.py

# Genesis: "commenting out function calls for input/output file testing


class GameEngine:
    __NUMBEROFVEGGIES = 30
    __NUMBEROFRABBITS = 5
    __HIGHSCOREFILE = "highscore.data"

    def __init__(self):
        self.__field = []
        self.__rabbitList = []
        self.__captain = None
        self.__vegetables = []
        self.__score = 0

    def initVeggies(self):
        fileName = ""

        while not os.path.exists(fileName):
          fileName = input("Please input the name of the Veggie file you would like to use: ")

        with open(fileName, 'r') as file:
            line = file.readline()
            line = line.split(",")

            row = int(line[1])
            col = int(line[2])

            # initialize the 2D list "field"
            # debug: switching around col and row
            self.__field = [[None for _ in range(col)] for _ in range(row)]

            # for each row in file, create veggie object and append to list
            for line in file:
                # strip row of newline char
                line = line.strip("\n")
                line = line.split(",")

                # create new veggie object
                # i.e. object = Veggie(symbol, name, point val)
                veggie = Veggie(line[1], line[0], line[2])

                # append to list of vegetables
                self.__vegetables.append(veggie)

        # set to hold "occupied" veggie spaces
        occupied = set()
        # seed random -- have been using 3
        random.seed(4)
        while len(occupied) < self.__NUMBEROFVEGGIES:
            # generate a random xy position within field bounds
            xPos = random.randrange(0, col)
            yPos = random.randrange(0, row)
            veggiePos = (xPos, yPos)

            # if this position is NOT occupied, add to set
            if veggiePos not in occupied:
                occupied.add(veggiePos)

        # with set of positions, populate "field" list
        for pos in occupied:
            x, y = pos
            if x < col and y < row:
                # pick a random vegetable from vegetables list
                randVeggie = random.randrange(len(self.__vegetables))
                # populate that coord with veggie object
                self.__field[y][x] = self.__vegetables[randVeggie]

    def initCaptain(self):

        # Generate a random xy-position within field bounds
        x_pos = random.randrange(0, len(self.__field[0]))
        y_pos = random.randrange(0, len(self.__field))

        # While the chosen xy-position is filled...
        while self.__field[y_pos][x_pos] is not None:
            # Generate a new random xy-position within field bounds
            x_pos = random.randrange(0, len(self.__field[0]))
            y_pos = random.randrange(0, len(self.__field))

        # Create a new Captain object
        cap = Captain(x_pos, y_pos)

        # Stores Captain object in member variable
        self.__captain = cap

        # Fills spot in field with the Captain object
        self.__field[y_pos][x_pos] = cap

    def initRabbits(self):

        # For each rabbit...
        for i in range(self.__NUMBEROFRABBITS):

            # Generate a random xy-position within field bounds
            x_pos = random.randrange(0, len(self.__field[0]))
            y_pos = random.randrange(0, len(self.__field))

            # While the chosen xy-position is filled...
            while self.__field[y_pos][x_pos] is not None:
                # Generate a new random xy-position within field bounds
                x_pos = random.randrange(0, len(self.__field[0]))
                y_pos = random.randrange(0, len(self.__field))

            # Create a new Rabbit object
            rabbit = Rabbit(x_pos, y_pos)

            # Stores Rabbit object in member variable List
            self.__rabbitList.append(rabbit)

            # Fills spot in field with the Rabbit object
            self.__field[y_pos][x_pos] = rabbit

    def initializeGame(self):
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()


    def remainingVeggies(self):
      #TODO: define function to count number of veggies still in game.
      return 1

    def intro(self):
      print("Welcome to Captain Veggie!")

      print("The rabbits have invaded your garden and you must harvest")
      print("as many vegetables as possible before rabbits eat them")
      print("all! Each vegetable is worth a different number of points")
      print("so go for the high score!")

      print("\nThe vegetables are: ")
      for veggie in self.__vegetables:
          print(veggie)

      print(f"\nCaptain Veggie is {self.__captain.getSymbol()}, and the rabbits are {self.__rabbitList[0].getSymbol()}'s.")

      print("\nGood luck!")
      #TODO: create other appropriate descriptions

    def printField(self):

        # Top border
        width = len(self.__field[0])*3+2
        for i in range(width):
            print("#", end = "")
        print("")

        for i in range(len(self.__field)):

            # Left border
            print("#", end="")

            for h in range(len(self.__field[i])):

                # If there is any FieldInhabitant at the current position, print its symbol
                if isinstance(self.__field[i][h], FieldInhabitant):
                    print(format(self.__field[i][h].getSymbol(), '^3s'), end="")

                # Else do not print anything
                elif self.__field[i][h] is None:
                    print(format("", '^3s'), end="")

            # Right border
            print("#")

        # Bottom border
        for i in range(width):
            print("#", end="")


    def getScore(self):
      #return score
      return self.__score

    def moveRabbits(self):
      return 1

    def moveCptVertical(self):
      return 1

    def moveCptHorizontal(self):
      return 1

    def moveCaptain(self):
      return 1

    def gameOver(self):
      #outputs gameover message
      return 1

    def highScore(self):
      return 1
