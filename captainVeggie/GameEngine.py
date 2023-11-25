import os
import random
import pickle
from Captain import Captain
from Rabbit import Rabbit
from Veggie import Veggie
from FieldInhabitant import FieldInhabitant
from Creature import Creature
from Snake import Snake


# Aleese: I added this import statement because I edited printField() to just check if the current position has a
# FieldInhabitant rather than individually checking if it has a rabbit, captain, veg. However, Python would not
# recognize FieldInhabitant without importing it -- unsure why. I feel there should be a way to check this w/o importing.


# Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova
# Date: 11/18/2023
# Desc: Class file for 'GameEngine' class. This will contain initialization and running functions for the actual "Captain Veggie" game. Will be called in main.py


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

        # Bonus: Snake
        self.__snake = None

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
        self.initSnake()

    def remainingVeggies(self):
        # examines the field and returns the number of veggies left
        veggie_count = 0

        # As we go through the field
        for i in range(len(self.__field)):
            for h in range(len(self.__field[i])):
                if isinstance(self.__field[i][h], Veggie):
                    # If this is a veggie object, add to count
                    veggie_count += 1

        # Return count after checking the field
        return veggie_count

    def intro(self):
        print("Welcome to Captain Veggie!")

        print("The rabbits have invaded your garden and you must harvest")
        print("as many vegetables as possible before rabbits eat them")
        print("all! Each vegetable is worth a different number of points")
        print("so go for the high score!")

        print("\nThe vegetables are: ")
        for veggie in self.__vegetables:
            print(veggie)

        print(
            f"\nCaptain Veggie is {self.__captain.getSymbol()}, and the rabbits are {self.__rabbitList[0].getSymbol()}'s.")

        print("\nGood luck!")
        # TODO: create other appropriate descriptions

    def printField(self):

        # Top border
        width = len(self.__field[0]) * 3 + 2
        for i in range(width):
            print("#", end="")
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
        # return score
        return self.__score

    def moveRabbits(self):

        # For each rabbit...
        for i in range(self.__NUMBEROFRABBITS):

            # Get current position of rabbit
            x_current = self.__rabbitList[i].getXCoord()
            y_current = self.__rabbitList[i].getYCoord()

            # Randomly choose whether to move one position left, right, or neither
            x_move = random.randint(-1, 1)

            # Randomly choose whether to move one position down, up, or neither
            y_move = random.randint(-1, 1)

            # Determine potential new position of rabbit after moving
            x_new = x_current + x_move
            y_new = y_current + y_move

            # If the new position is out of bounds, forfeit the movement
            # TODO: Check this condition actually works as intended
            if x_new < 0 or y_new < 0 or x_new >= len(self.__field[0]) or y_new >= len(self.__field):
                continue

            # Else if the new position is another rabbit or the Captain, forfeit the movement
            elif isinstance(self.__field[y_new][x_new], Creature):
                continue

            # Else, the new position should either be empty or have a vegetable, and the rabbit will move
            else:

                # Set new xy-position of the rabbit object
                self.__rabbitList[i].setXCoord(x_new)
                self.__rabbitList[i].setYCoord(y_new)

                # Move rabbit to new position in the field and set its previous location to None
                self.__field[y_new][x_new] = self.__rabbitList[i]
                self.__field[y_current][x_current] = None

    def moveCptVertical(self):
        return 1

    def moveCptHorizontal(self):
        return 1

    def moveCaptain(self):
        return 1

    def gameOver(self):
        #retrieve pointers
        basket = self.__captain.getBasket() #retrieve the list containing vegetables captain picked up
        uniqueVeggies = self.__captain.getUniqueVeggies() #return set of names of unique vegetables picked up by Captain

        print("GAME OVER")
        print("Basket Contents:")

        #for every unique vegetable picked up by the player
        for veg in uniqueVeggies:
            #print out the name, point value, quantity, and total points earned from that veggie
            print(f"{veg} (x{basket.count(veg)}) = {veg.getPoints() * basket.count(veg)} pts") #Sample output: Potato, 5 points (x5) = 25 pts
        
        #printing final score
        print(f"Final score: {self.__score}")
        #deleting new objects, so that they're not just hanging around. Not sure if it nukes object or pointer to object
        #del uniqueVeggies
        #del basket    
        #commenting out bc unsure if data leakge would be a problem or not.
    
    def highScore(self):
      
      #"Key Function" used for sorting list. Given that the list is loaded back as 
      #a list of tuple pairs (name, highscore), i had to define a "Key Function" for
      #the .sort() function "key" parameter so that it would sort descending by high score,
      #not by alphabetical order.
      #Had to define within highScore function, as it would not recognize outside of it.
      def keyFunc(userPair):
        #when called, return the score as the sort key, which is the second item in the Tuple pair.
        return userPair[1]
      
      #initializing list which will be pickled/dumped into.
      playerData = []

      #"if the file exists, load it."
      if os.path.exists(self.__HIGHSCOREFILE):
        with open(self.__HIGHSCOREFILE, "rb") as file:
          playerData = pickle.load(file)

      #reading in user initials, and then retrieving the first 3 letters.
      userInitials = input("Please input three letters for your initials: ")
      userInitials = userInitials[:3].upper() #slicing in only first 3 characters of user input, in case they get funny. 

      #appending a tuple the list of scores
      playerData.append(tuple((userInitials, self.__score)))
      #sorting the data based on score. Sorted descensding.
      playerData.sort(key = keyFunc, reverse = True)

      print("Name | Score")
      for pair in playerData: 
          #for every tuple pair in the list, print out the name (center aligned with 5 reserved chars and the score)
          print(f"{format(pair[0],'^5s')}| {pair[1]}")

      #following printing, open the file "highscore.data" and dump list into it, in binary.
      with open(self.__HIGHSCOREFILE, "wb") as file:
          pickle.dump(playerData, file)
      #closeout
      

    # genesis: bonus content starts here
    def initSnake(self):
        # Randomize coordinates
        xPos = random.randrange(0, len(self.__field[0]))
        yPos = random.randrange(0, len(self.__field))

        while self.__field[yPos][xPos] is not None:
            # Keep looking for an unfilled spot to generate a snake in
            xPos = random.randrange(0, len(self.__field[0]))
            yPos = random.randrange(0, len(self.__field))

        # Instantiate snake object
        snake = Snake(xPos, yPos)

        # Store Snake object
        self.__snake = snake

        # Place snake in field
        self.__field[yPos][xPos] = snake

    def moveSnake(self):
        # TODO: Mostly done, just need a better way to go around obstacles cause right now it just stops
        # Get current position of snake
        snake_x = self.__snake.getXCoord()
        snake_y = self.__snake.getYCoord()

        # Get current position of Captain Veggie
        captain_x = self.__captain.getXCoord()
        captain_y = self.__captain.getYCoord()

        # Start at the current position
        x_new = snake_x
        y_new = snake_y

        # Determine new position snake should move to
        if snake_x < captain_x:
            # If captain is to the right, move to the right
            x_new = snake_x + 1
        elif snake_x > captain_x:
            # If captain is to the left, move to the left
            x_new = snake_x - 1
        elif snake_y < captain_y:
            # If captain is north, move up
            y_new = snake_y + 1
        elif snake_y > captain_y:
            # If captain is south, move down
            y_new = snake_y - 1
        else:
            # Leave it as is
            y_new = snake_y
            x_new = snake_x

        # Check if out of bounds
        if x_new < 0 or y_new < 0 or x_new >= len(self.__field[0]) or y_new >= len(self.__field):
            return

        # Check if there is an obstacle at the new position
        if isinstance(self.__field[y_new][x_new], Veggie) or isinstance(self.__field[y_new][x_new], Rabbit):
            # Determine if the snake should move horizontally or vertically to bypass the obstacle
            if x_new != snake_x and y_new != snake_y:
                # Prioritize horizontal movement over vertical
                if snake_x < captain_x:
                    x_new = snake_x + 1
                else:
                    x_new = snake_x - 1
                y_new = snake_y  # Stay in the same row
            else:
                # Stay in the same column if moving horizontally, or vice versa
                if x_new == snake_x:
                    x_new = snake_x
                if y_new == snake_y:
                    y_new = snake_y

            # Check if new position is out of bounds
            if x_new < 0 or y_new < 0 or x_new >= len(self.__field[0]) or y_new >= len(self.__field):
                return

            # Check if new position is an inhabitant other than captain
            if isinstance(self.__field[y_new][x_new], Veggie) or isinstance(self.__field[y_new][x_new], Rabbit):
                return

        elif isinstance(self.__field[y_new][x_new], Captain):
            # Pop 5 veggies out of Captain's basket
            self.__captain.removeVeggie(5)

            # Randomize new snake coordinates after trying to touch Captain
            x_new = random.randrange(0, len(self.__field[0]))
            y_new = random.randrange(0, len(self.__field))

            while self.__field[y_new][x_new] is not None:
                # Keep looking for an unfilled spot to generate a snake in
                x_new = random.randrange(0, len(self.__field[0]))
                y_new = random.randrange(0, len(self.__field))

        # Set snake's new coordinates
        self.__field[snake_y][snake_x] = None
        self.__snake.setXCoord(x_new)
        self.__snake.setYCoord(y_new)

        # Move snake to new spot
        self.__field[y_new][x_new] = self.__snake

#Commented out, for future re-use

#    def injectList(self): #creating function to inject list of veggies into basket. made to test gameOver function
#      potato = Veggie("p", "potato", 5)
#      onion = Veggie("o", "onion", 5)
#      testCaptain = self.__captain = Captain(0,0)
#
#      for i in range(0,5):
#        testCaptain.addVeggie(potato)
#        self.__score += potato.getPoints()
#        testCaptain.addVeggie(onion)
#        self.__score += onion.getPoints()
#
#
#        
#
##Eugene: Adding test main so I can run the game engine file directly, and test individual functions.
#def main():
#    #breakpoint()
#    test = GameEngine()
#    test.injectList()
#    test.gameOver()
#    test.highScore()
#
#main()