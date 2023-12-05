# Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova
# Date: 12/8/2023
# Desc: Class file for 'GameEngine' class. This will contain initialization and running functions for the actual
# "Captain Veggie" game. Will be called in main.py

import os
import random
import pickle
from Creature import Creature
from Captain import Captain
from Rabbit import Rabbit
from Snake import Snake
from Veggie import Veggie


class GameEngine:
    __NUMBEROFVEGGIES = 30
    __NUMBEROFRABBITS = 5
    __HIGHSCOREFILE = "highscore.data"

    # Colors for output
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

    def __init__(self):
        self.__field = []
        self.__rabbitList = []
        self.__captain = None
        self.__vegetables = []
        self.__score = 0

        # Bonus: Snake
        self.__snake = None

    def initVeggies(self):
        """
        This function prompts the user for a valid configuration file.
        Using the data from that file, a field is populated with Veggie objects,
        all at random, unique locations.
        - Genesis
        """
        # Ask for config file
        fileName = input("Please input the name of the Veggie file you would like to use: ")

        # Until we receive a valid file, keep asking
        while not os.path.exists(fileName):
            fileName = input("Invalid filename. Please input the name of the Veggie file you would like to use: ")

        # Open file
        with open(fileName, 'r') as file:
            # Take in first line, split by commas
            line = file.readline()
            line = line.split(",")

            # First line represents dimensions - place those into row and col
            row = int(line[1])
            col = int(line[2])

            # Initialize the 2D list "field" based on row and col
            self.__field = [[None for _ in range(col)] for _ in range(row)]

            # For each row in file, create veggie object and append to list
            for line in file:
                # Strip row of newline char
                line = line.strip("\n")
                line = line.split(",")

                # Create new veggie object
                # i.e. object = Veggie(symbol, name, point val)
                veggie = Veggie(line[1], line[0], int(line[2]))

                # Append to list of vegetables
                self.__vegetables.append(veggie)

        # Set to hold "occupied" veggie spaces
        occupied = set()
        random.seed(3)

        while len(occupied) < self.__NUMBEROFVEGGIES:
            # Generate a random xy position within field bounds
            xPos = random.randrange(0, col)
            yPos = random.randrange(0, row)
            veggiePos = (xPos, yPos)

            # If this position is NOT occupied, add to set
            if veggiePos not in occupied:
                occupied.add(veggiePos)

        # With set of positions, populate "field" list
        for pos in occupied:
            x, y = pos
            if x < col and y < row:
                # Pick a random vegetable from vegetables list
                randVeggie = random.randrange(len(self.__vegetables))
                # Populate that coord with veggie object
                self.__field[y][x] = self.__vegetables[randVeggie]

    def initCaptain(self):
        """
        Instantiates a Captain object at a random empty position in the field.
        Primarily written by Aleese.
        """

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
        """
        Instantiates a given number of Rabbit objects at random empty positions in the field.
        Primarily written by Aleese.
        """

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
        """
        This function checks the field and returns the number of
        remaining veggies.
        - Genesis
        :return: The total count of remaining veggies.
        """
        # Examine the field and returns the number of veggies left
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
        """
        This function welcomes the user and describes the game.
        - Genesis
        """
        # Output welcome + game description
        print("Welcome to Captain Veggie!")
        print("The rabbits have invaded your garden and you must harvest")
        print("as many vegetables as possible before rabbits eat them")
        print("all! Each vegetable is worth a different number of points")
        print("so go for the high score!")
        print("BONUS: Avoid the snake, or else it'll steal your veggies!")

        # Output veggies using appropriate "str" function
        print("\nThe vegetables are: ")
        for veggie in self.__vegetables:
            print(veggie)

        # Output symbols for each field inhabitant
        print(f"\nCaptain Veggie is {self.BLUE}{self.__captain}{self.RESET}, the snake is {self.RED}{self.__snake}{self.RESET}, ", end="")
        print(f"and the rabbits are {self.YELLOW}{self.__rabbitList[0]}{self.RESET}'s.")

        print("\nGood luck!")

    def printField(self):
        """
        This function outputs a neat, 2D field with borders, as well as the number of
        veggies in Captain Veggie's basket.
        - Genesis
        """

        # Sanity check for number of veggies in basket
        print(f"{len(self.__captain.getBasket())} veggie(s) in basket!")

        # Calculate border width based of number of columns
        width = len(self.__field[0]) * 3 + 2

        # Top border
        for i in range(width):
            print("#", end="")
        print("")

        # For this row
        for i in range(len(self.__field)):
            # Left border char
            print("#", end="")
            # For each position
            for h in range(len(self.__field[i])):
                # Print color-coded symbols based on field inhabitant
                if isinstance(self.__field[i][h], Captain):
                    print(f"{self.BLUE}{format(self.__field[i][h].getSymbol(), '^3s')}{self.RESET}", end="")
                elif isinstance(self.__field[i][h], Rabbit):
                    print(f"{self.YELLOW}{format(self.__field[i][h].getSymbol(), '^3s')}{self.RESET}", end="")
                elif isinstance(self.__field[i][h], Veggie):
                    print(f"{self.GREEN}{format(self.__field[i][h].getSymbol(), '^3s')}{self.RESET}", end="")
                elif isinstance(self.__field[i][h], Snake):
                    print(f"{self.RED}{format(self.__field[i][h].getSymbol(), '^3s')}{self.RESET}", end="")

                # Else do not print anything
                elif self.__field[i][h] is None:
                    print(format("", '^3s'), end="")
            # Right border char
            print("#")

        # Bottom border
        for i in range(width):
            print("#", end="")

    def getScore(self):
        # Return score
        return self.__score

    def moveRabbits(self):
        """
        Moves each rabbit up to 1 space in a random direction. Rabbit will forfeit its move if it tries to move out of
        bounds or on top of another Creature.
        Primarily written by Aleese.
        """

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
            if x_new < 0 or y_new < 0 or x_new >= len(self.__field[0]) or y_new >= len(self.__field):
                continue

            # Else if the new position is another rabbit, the Captain, or the snake, forfeit the movement
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

    def moveCptVertical(self, w_or_s):
        """
        Moves the Captain up or down depending on parameter w_or_s. Captain picks up veggies they may encounter.
        Captain forfeits their move if they try to move on top of a rabbit.
        Primarily written by Aleese.
        :param w_or_s: Represents user's input "w" or "s" (up or down, respectively)
        :type w_or_s: str
        """

        # Get current position of Captain
        x_current = self.__captain.getXCoord()
        y_current = self.__captain.getYCoord()

        # Determine whether Captain moves up or down based on function parameter w_or_s
        if w_or_s == "w":
            y_move = -1
        else:
            y_move = 1

        # Determine potential new position of Captain after moving
        x_new = x_current
        y_new = y_current + y_move

        # If the new position is empty, move the Captain there
        if self.__field[y_new][x_new] is None:

            # Set new xy-position of the Captain object
            self.__captain.setXCoord(x_new)
            self.__captain.setYCoord(y_new)

            # Move Captain to new position in the field and set their previous location to None
            self.__field[y_new][x_new] = self.__captain
            self.__field[y_current][x_current] = None

        # Else if the new position is a vegetable, move the Captain there and pick up the veggie
        elif isinstance(self.__field[y_new][x_new], Veggie):

            # Set new xy-position of the Captain object
            self.__captain.setXCoord(x_new)
            self.__captain.setYCoord(y_new)

            # Output that a delicious veggie has been found
            print(f"Yummy! A delicious {self.__field[y_new][x_new].getName()}")

            # Add veggie to the Captain's basket
            self.__captain.addVeggie(self.__field[y_new][x_new])

            # Increment the score by the veggie's point value
            self.__score += self.__field[y_new][x_new].getPoints()

            # Move Captain to new position in the field and set their previous location to None
            self.__field[y_new][x_new] = self.__captain
            self.__field[y_current][x_current] = None

        # Else if there is a rabbit at the new position, warn against stepping on rabbits
        elif isinstance(self.__field[y_new][x_new], Rabbit):
            print("Don't step on the bunnies!")

    def moveCptHorizontal(self, a_or_d):
        """
        Moves the Captain left or right depending on parameter a_or_d. Captain picks up veggies they may encounter.
        Captain forfeits their move if they try to move on top of a rabbit.
        Primarily written by Aleese.
        :param a_or_d: Represents user's input "a" or "d" (left or right, respectively)
        :type a_or_d: str
        """

        # Get current position of Captain
        x_current = self.__captain.getXCoord()
        y_current = self.__captain.getYCoord()

        # Determine whether Captain moves left or right based on function parameter a_or_d
        if a_or_d == "d":
            x_move = 1
        else:
            x_move = -1

        # Determine potential new position of Captain after moving
        x_new = x_current + x_move
        y_new = y_current

        # If the new position is empty, move the Captain there
        if self.__field[y_new][x_new] is None:

            # Set new xy-position of the Captain object
            self.__captain.setXCoord(x_new)
            self.__captain.setYCoord(y_new)

            # Move Captain to new position in the field and set their previous location to None
            self.__field[y_new][x_new] = self.__captain
            self.__field[y_current][x_current] = None

        # Else if the new position is a vegetable, move the Captain there and pick up the veggie
        elif isinstance(self.__field[y_new][x_new], Veggie):

            # Set new xy-position of the Captain object
            self.__captain.setXCoord(x_new)
            self.__captain.setYCoord(y_new)

            # Output that a delicious veggie has been found
            print(f"Yummy! A delicious {self.__field[y_new][x_new].getName()}")

            # Add veggie to the Captain's basket
            self.__captain.addVeggie(self.__field[y_new][x_new])

            # Increment the score by the veggie's point value
            self.__score += self.__field[y_new][x_new].getPoints()

            # Move Captain to new position in the field and set their previous location to None
            self.__field[y_new][x_new] = self.__captain
            self.__field[y_current][x_current] = None

        # Else if there is a rabbit at the new position, warn against stepping on rabbits
        elif isinstance(self.__field[y_new][x_new], Rabbit):
            print("Don't step on the bunnies!")

    def moveCaptain(self):
        """
        Prompts user to move the Captain using WASD. If the movement does not put the Captain outside the field,
        moveCptVertical() and moveCptHorizontal() are called appropriately. Captain forfeits their move if they try to
        move out of bounds.
        Primarily written by Aleese.
        """

        # Have user input direction to move using WASD
        movement = input("\nWould you like to move up (W), down (S), left (A), or right (D): ").lower()

        # If user chooses up, check if there is room to move up and then move the Captain if there is
        if movement == "w":
            if self.__captain.getYCoord() == 0:
                print("You can't move that way!")
            else:
                self.moveCptVertical("w")

        # If user chooses down, check if there is room to move down and then move the Captain if there is
        elif movement == "s":
            if self.__captain.getYCoord() == len(self.__field) - 1:
                print("You can't move that way!")
            else:
                self.moveCptVertical("s")

        # If user chooses left, check if there is room to move left and then move the Captain if there is
        elif movement == "a":
            if self.__captain.getXCoord() == 0:
                print("You can't move that way!")
            else:
                self.moveCptHorizontal("a")

        # If user chooses right, check if there is room to move right and then move the Captain if there is
        elif movement == "d":
            if self.__captain.getXCoord() == len(self.__field[0]) - 1:
                print("You can't move that way!")
            else:
                self.moveCptHorizontal("d")

        # Else inform the user that they input an invalid direction
        else:
            print(f"{movement} is not a valid option.")

    def gameOver(self):
        
        def keyFunc(veg):   # Key function for sorting set: key is to sort by veggie name, in alphabetical order
            return veg.getName()
        
        print(f"\n{self.RED}GAME OVER{self.RESET}")
        print("Basket Contents:")

        # If basket IS NOT empty
        if self.__captain.checkBasket():
          # Retrieve pointers
          # Retrieve the list containing vegetables captain picked up
          basket = self.__captain.getBasket() 
          # Return set of names of unique vegetables picked up by Captain, then sort them
          uniqueVeggies = sorted(self.__captain.getUniqueVeggies(), key = keyFunc) 

          # TODO: Eugene: QOL: figure out how to update scores of initials already present on scoreboard.

          # For every unique vegetable picked up by the player
          for veg in uniqueVeggies:
              # Print out the name, point value, quantity, and total points earned from that veggie
              # Sample output: Potato, 5 points (x5) = 25 pts
              print(f"{veg} (x{basket.count(veg)}) = {veg.getPoints() * basket.count(veg)} pts") 

        # If basket IS empty
        else: 
          print("Your basket is empty.")
        
        # Printing final score
        print(f"{self.BLUE}Final score: {self.__score}{self.RESET}")
    
    def highScore(self):
      """
      Prompts the user for their initials in order to store and pickle their score in descending order.
      Stores data in (Initial, Score) Tuple Format, which is put into a list.
      List is sorted by score in descending order. Accomplished using .sort() and key function keyFunc.

      :param self: Refers to specific instance of instantiated object -- "itself."
      :type self: GameEngine() obj.
      
      -Eugene

      """
      
      # "Key Function" used for sorting list. Given that the list is loaded back as
      # a list of tuple pairs (name, highscore), I had to define a "Key Function" for
      # the .sort() function "key" parameter so that it would sort descending by high score,
      # not by alphabetical order.
      # Had to define within highScore function, as it would not recognize outside of it.

      def keyFunc(userPair):
        """
        Key Function for sorting by the second element of a User's "Highcore Tuple" pair, since the Tuple cannot be modified for easier sorting.
        
        :param userPair: Tuple containing initials and score in a Tuple (init, score) in that order.
        :type userPair: Tuple.
        :return: int score by which sorting will occur.
        """
        # When called, return the score as the sort key, which is the second item in the Tuple pair
        return userPair[1]
      
      # Initializing list which will be pickled/dumped into
      playerData = []

      # If the file exists, load it
      if os.path.exists(self.__HIGHSCOREFILE):
        with open(self.__HIGHSCOREFILE, "rb") as file:
          playerData = pickle.load(file)

      # Reading in user initials, and then retrieving the first 3 letters
      userInitials = input("\nPlease input three letters for your initials: ")
      userInitials = userInitials[:3].upper()   # Slicing in only first 3 characters of user input, in case they get funny

      # Appending a tuple to the list of scores
      playerData.append(tuple((userInitials, self.__score)))
      # Sorting the data based on score, descending
      playerData.sort(key = keyFunc, reverse = True)

      print("Name | Score")
      for pair in playerData: 
          # For every tuple pair in the list, print out the name (center aligned with 5 reserved chars and the score)
          print(f"{format(pair[0],'^5s')}| {pair[1]}")

      # Following printing, open the file "highscore.data" and dump list into it, in binary
      with open(self.__HIGHSCOREFILE, "wb") as file:
          pickle.dump(playerData, file)
      # Closeout

    def initSnake(self):
        """
        This function initiates a Snake object on a random, unique
        position on the field. - Genesis
        """

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

    def nextMoveNotOk(self, xCoord, yCoord):
        """
        This function checks whether the proposed position is a valid next move
        for the snake in the field. - Genesis
        :param xCoord: The proposed x position.
        :param yCoord: The proposed y position.
        :return: True if the next move is not possible, false otherwise.
        """
        # Assume that the next move is ok
        outOfBounds = False
        obstacleExists = False

        # If it is out of bounds
        if xCoord < 0 or yCoord < 0 or xCoord >= len(self.__field[0]) or yCoord >= len(self.__field):
            # Not ok
            outOfBounds = True
        # If it is either out of bounds OR not null AND not the captain
        if outOfBounds or (self.__field[yCoord][xCoord] is not None and not isinstance(self.__field[yCoord][xCoord], Captain)):
            # Then it is an obstacle, so we can't move there -- Not ok
            obstacleExists = True
        # Return bool
        return obstacleExists

    def moveSnake(self):
        """
        This function allows the snake to chase Captain Veggie. If it is
        stuck between obstacles, it will check ways to go around the obstacle
        to continue chasing Captain Veggie. - Genesis
        """

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
        x_difference = snake_x - captain_x
        if x_difference < 0:
            # If snake's x is less than captain's, move right
            x_direction = 1
        elif x_difference > 0:
            # If snake's x is more than captain's, move left
            x_direction = -1
        else:
            # Stay the same
            x_direction = 0

        y_difference = snake_y - captain_y
        if y_difference < 0:
            # If snake's y is less than captain's, move up
            y_direction = 1
        elif y_difference > 0:
            # If snake's y is more than captain's, move down
            y_direction = -1
        else:
            # Stay the same
            y_direction = 0

        # Move left/right

        # If snake is in a different column than captain
        if x_direction != 0:
            # Move 1 square towards the captain in x dir
            x_new += x_direction
            # If snake is in the same row as captain
            if y_direction == 0:
                # We always want to move in the y direction if x is blocked
                y_direction = -1
            # We now have a proposed set of coord based on conditions
            # If these new coordinates are not ok (obstacle or out of bounds),
            if self.nextMoveNotOk(x_new, y_new):
                # Can't move diagonally, so prioritize a y-move
                x_new = snake_x
                y_new += y_direction
                # If THESE new coord are not ok,
                if self.nextMoveNotOk(x_new, y_new):
                    # Can't move diagonally, so prioritize an x-move
                    y_new = snake_y
                    # Move opposite direction of x attempt
                    x_new -= x_direction
                    # If THESE new coord are not ok,
                    if self.nextMoveNotOk(x_new, y_new):
                        # Try moving in opposite direction of y attempt
                        x_new = snake_x
                        y_new -= y_direction
                        if self.nextMoveNotOk(x_new, y_new):
                            # Blocked on all directions, don't move
                            y_new = snake_y

        # Move up/down

        # If snake is in a different row than captain
        elif y_direction != 0:
            # Move 1 square towards the captain in y dir
            y_new += y_direction
            # If snake is in the same col as captain
            if x_direction == 0:
                # We always want to move in the x direction if y is blocked
                x_direction = -1
            if self.nextMoveNotOk(x_new, y_new):
                # Revert back to original, something in the way
                y_new = snake_y
                x_new += x_direction
                if self.nextMoveNotOk(x_new, y_new):
                    # Something in the way again, not possible to move closer to captain
                    x_new = snake_x
                    # Move opposite direction of original
                    y_new -= y_direction
                    if self.nextMoveNotOk(x_new, y_new):
                        # Something blocking us yet again
                        y_new = snake_y
                        x_new -= x_direction
                        if self.nextMoveNotOk(x_new, y_new):
                            # Blocked on all directions, don't move
                            x_new = snake_x

        # If the snake touches the captain
        if isinstance(self.__field[y_new][x_new], Captain):

            # Output snake message
            if len(self.__captain.getBasket()) >= 5:
                # Pop 5 veggies out of Captain's basket
                count, points_lost = self.__captain.removeVeggie(5)
                print(f"Oh no! The snake ate {count} veggie(s) from the basket...you lost {points_lost} points!")
            elif len(self.__captain.getBasket()) > 0:
                # Pop all remaining veggies out of Captain's basket
                count, points_lost = self.__captain.removeVeggie(len(self.__captain.getBasket()))
                print(f"Oh no! The snake ate {count} veggie(s) from the basket...you lost {points_lost} points!")
            else:
                points_lost = 0
                print("Oh no, the snake got you! Your basket is empty, you lost no points.")

            # Subtract points from score
            self.__score -= points_lost

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
