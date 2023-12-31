# Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova
# Date: 12/8/2023
# Desc: Main function for Captain Veggie game. Will import GameEngine class with inheritances and instantiate game.

from GameEngine import GameEngine


def main():
  """
  This function serves as the driver to the game's functions.
  """
  game = GameEngine()
  game.initializeGame()
  game.intro()

  # Variable to store the number of remaining vegetables in the game
  veggies_left = game.remainingVeggies()

  while veggies_left != 0:
    # Output the number of remaining veggies and the player's score
    print(f"\n{veggies_left} veggies remaining. Current score: {game.getScore()}.", end=" ")

    # Print out the field
    game.printField()

    # Move the rabbits
    game.moveRabbits()

    # Move the captain
    game.moveCaptain()

    # Move the snake
    game.moveSnake()

    # Determine the new number of remaining veggies
    veggies_left = game.remainingVeggies()

  # Display the Game Over information
  game.gameOver()

  # Handle the High Score function
  game.highScore()


main()
