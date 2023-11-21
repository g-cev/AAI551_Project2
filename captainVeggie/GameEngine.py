import os
import random
from Captain import Captain
from Rabbit import Rabbit
from Veggie import Veggie


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

            col = int(line[1])
            row = int(line[2])

            # initialize the 2D list "field"
            self.__field = [[None for _ in range(row)] for _ in range(col)]

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
        # seed random
        random.seed(3)
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
                self.__field[x][y] = self.__vegetables[randVeggie]

    def initCaptain(self):
        # blahbloo
        return 1

    def initRabbits(self):
        # bloohblah
        return 1

    def initializeGame(self):
        self.initVeggies()
        # self.initCaptain()
        # self.initRabbits()


    def remainingVeggies(self):
      #TODO: define function to count number of veggies still in game.
      return 1

    def intro(self):
      print("Welcome to Captain Veggie!")

      print("The rabbits have invaded your garden and you must harvest")
      print("as many vegetables as possible before rabbits eat them")
      print("all! Each vegetable is worth a different number of points")
      print("so go for the high score!")

      #TODO: List all veggies in this instance of the game, their symbols, and point vals
      print("\nThe vegetables are: ")
      for veggie in self.__vegetables:
          print(veggie)

      #TODO: "Captain Veggie and Rabbits symbols are output" (?)
      print(f"\nCaptain Veggie is (call var here), and the rabbits are (enter var here)'s.")

      print("\nGood luck!")
      #TODO: create other appropriate descriptions

    def printField(self):
        # border
        width = len(self.__field[0])*3+2
        for i in range(width):
            print("#", end = "")
        print("")
        for i in range(len(self.__field)):
            print("#", end="")
            for h in range(len(self.__field[i])):
                if isinstance(self.__field[i][h], Veggie):
                    print(format(self.__field[i][h].getSymbol(), '^3s'), end="")
                elif self.__field[i][h] is None:
                    print(format("", '^3s'), end="")
                    # here we would add "if captain is here" and etc
            print("#")
        # border
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