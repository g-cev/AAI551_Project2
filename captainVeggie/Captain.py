# Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova
# Date: 12/8/2023
# Desc: Class file for 'Captain' class. Inherits Creature class (superClass/parent). Not inherited by any other class.

from Creature import Creature

class Captain(Creature):
  """
  Class that defines the Captain object. Inherits from Creature class


  Attributes:

  :param xCoord: X-Coordinate of the Captain's location on the printed field. This will be continuously updated as the game continues.
  :type xCoord: int

  :param yCoord: Y-Coordinate of the Captain's location on the printed field. This will be continuously updated as the game continues.
  :type yCoord: int

  :param Basket: List that will contain all of the Veggie objects collected by player from playing field. Will be used to calculate final score.
  :type Basket: List() object.


  """
  def __init__(self, xCoord, yCoord):
    """
    Initializes attributes of Captain class object.
    X-Coordinates and Y-Coordiantes for Captain will be filled with RNG values. 
    Symbol for Captain is fixed to "V", for Captain Veggie.
    Captain's "Basket" object is by default empty.
    """
    Creature.__init__(self, "V", xCoord, yCoord)
    self.__basket = []  # Empty list 'Basket' that will contain list of all veggies collected by Captain

  def addVeggie(self, veg): # veg is to be a Veggie-class object. Adds vegetable object to list of collected vegetables
    """
    Adds vegetable to Captain class object "Basket" attribute. This will be called when the player collects a Veggie object.

    :param veg: The vegetable that will be appended to the "Basket" list.
    :type veg: Veggie() Class Object.

    """
    self.__basket.append(veg)

  def checkBasket(self):  # Returns boolean. Asks if basket is empty or not (True = not empty, False = empty)
    """
    Checks if the Captain's basket is empty or not.

    :return: bool. 
      Returns FALSE if empty.
      Returns TRUE if not empty.

      - Eugene
    """
    if not self.__basket:
      return False
    else:
      return True

  def getBasket(self):  # Returns basket list
    """
    Fetches the List denoting the Captain's basket for external use.

    :return: List() Object (pointer)

    -Eugene
    """
    return self.__basket

  def getUniqueVeggies(self):
    """
    Creates and sends out a list of all of the unique vegetables in the Captain's basket. Used for point breakdown readability.

    :return: Set() object (pointer)

    -Eugene
    """
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