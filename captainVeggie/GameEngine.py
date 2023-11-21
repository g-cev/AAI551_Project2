import os
from Captain import Captain
from Rabbit import Rabbit
from Veggie import Veggie

#Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova
#Date: 11/18/2023
#Desc: Class file for 'GameEngine' class. This will contain initialization and running functions for the actual "Captain Veggie" game. Will be called in main.py


class GameEngine:
  __NUMBEROFVEGGIES = 30
  __NUMBEROFRABBITS = 5
  __HIGHSCOREFILE = "highscore.data"

  def __init__(self):
    # self.__field = [] #TODO: MAKE 2D SOMEHOW?
    self.__col = 0
    self.__row = 0
    self.__field = [[None for _ in range(self.__col)] for _ in range(self.__row)]
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

      #in theory, should parse and create 2d list of field size with all units initialized to None.
      for i in range(int(line[1])):
        for j in range(int(line[2])):
          self.__field[i][j] = None

      #not sure if this next loop will skip past the "field size" line. #TODO: test intakes
      for line in file:
        line = line.split(",")
        self.__vegetables.append(Veggie(line[2], line[1], line[3]))

      #TODO: for initVeggies(): create randomized veggie placement routine.

  def initCaptain(self):
    #blahbloo
    return 1

  def initRabbits(self):
    #bloohblah
    return 1

  def initializeGame(self):
    self.initVeggies()
    self.initCaptain()
    self.initRabbits()

  def remainingVeggies(self):
    #TODO: define function to count number of veggies still in game.
    return 1

  def intro(self):
    print("Welcome to Captain Veggie!")
    #TODO: explain game
    #TODO: List all veggies in this instance of the game, their symbols, and point vals
    #TODO: "Captain Veggie and Rabbits symbols are output" (?)
    #TODO: create other appropriate descriptions
    #NORETURNVAL

  def printField(self):
    #prints the field
    return 1

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
