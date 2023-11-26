from GameEngine import GameEngine

#Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova 
#Date: 11/18/2023
#Desc: Main function for Captain Veggie game. Will import GameEngine class with inheritances and instantiate game.


def main():
  game = GameEngine()
  game.initializeGame()
  game.intro()

  # Variable to store the number of remaining vegetables in the game
  veggies_left = game.remainingVeggies()

  while veggies_left != 0:
    # Output the number of remaining veggies and the player's score
    print(f"\n{veggies_left} veggies remaining. Current score: {game.getScore()}")

    # Print out the field
    game.printField()

    # Move the rabbits
    game.moveCaptain()

    game.moveRabbits()

    # Move the snake
    game.moveSnake()

    # Determine the new number of remaining veggies
    veggies_left = game.remainingVeggies()

  # Display the Game Over information
  # game.gameOver()

  # Handle the High Score function
  # game.highScore()


main()
