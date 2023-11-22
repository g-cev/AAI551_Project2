from GameEngine import GameEngine

#Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova 
#Date: 11/18/2023
#Desc: Main function for Captain Veggie game. Will import GameEngine class with inheritances and instantiate game.


def main():
  game = GameEngine()
  game.initializeGame()
  game.intro()
  #TODO: handle remaining Veggies changes, Captain, and Rabbit movement while reprinting field. Maybe a while loop?

  choice = "Y"
  while choice != "N":
    # genesis: using print field for testing - feel free to grab and change as needed
    game.printField()
    choice = (input("\nContinue? Y/N - "))

  # game.gameOver()
  # game.highScore()


main()