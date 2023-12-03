# Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova
# Date: 12/8/2023
# Desc: Class file for 'Captain' class. Inherits Creature class (superClass/parent). Not inherited by any other class.

from Creature import Creature

class Captain(Creature):
  def __init__(self, xCoord, yCoord):
    # Provide values to Creature's constructor
    Creature.__init__(self, "V", xCoord, yCoord)
    self.__basket = []  # Empty list 'Basket' that will contain list of all veggies collected by Captain

  def addVeggie(self, veg): # veg is to be a Veggie-class object. Adds vegetable object to list of collected vegetables
    self.__basket.append(veg)

  def checkBasket(self):  # Returns boolean. Asks if basket is empty or not (True = not empty, False = empty)
    if not self.__basket:
      return False
    else:
      return True

  def getBasket(self):  # Returns basket list
    return self.__basket

  def getUniqueVeggies(self): # Returns set of unique vegetables collected. Will be used in gameOver function
    uniqueVeggies = set()
    # For every single vegetable in Captain's basket
    for veg in self.__basket:
      # Add veg to set. Repeats will not be added
      uniqueVeggies.add(veg)
    return uniqueVeggies

  def removeVeggie(self, num):
    """
    This function removes veggies from the captain's basket. - Genesis
    :param num: The number of veggies to be removed.
    :return: The number of veggies that were removed and the points lost.
    """
    # Initialize return variables
    removed_count = 0
    points_lost = 0

    for i in range(num):
      # If the basket is not empty
      if self.__basket:
        # Add to removed_count
        removed_count += 1
        # Add up total points lost
        points_lost += self.__basket[-1].getPoints()
        # Pop veggie from basket list
        self.__basket.pop(-1)

    return removed_count, points_lost