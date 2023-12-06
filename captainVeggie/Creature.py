# Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova
# Date: 12/8/2023
# Desc: Class file for 'Creature' class. Inherits FieldInhabitant class (superClass/parent). Will be inherited by
# 'Captain' and 'Rabbit' classes (subclasses/children).

from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
  """
  Class that defines Creature Object. Will be inherited by Captain and Rabbit classes.


  Attributes:

  :param sym: Symbol for the creature. This is the symbol with which the creature will be represented when the field is printed.
  :type sym: char

  :param xCoord: X-Coordinate of the Creature's location on the printed field. This will be continuously updated as the game continues. Will be RNG initialized.
  :type xCoord: int

  :param yCoord: Y-Coordinate of the Creature's location on the printed field. This will be continuously updated as the game continues. Will be RNG initialized.
  :type yCoord: int
  """
  def __init__(self, sym, xCoord, yCoord):  # Inherits "setSymbol"/"getSymbol" funcs
    """
    Constructor for the Creature class.
    "sym" parameter is passed to the parent FieldInhabitant class constructor.

    """
    FieldInhabitant.__init__(self, sym) 
    self._x = xCoord  # Protected variable to store x-coordinate on map
    self._y = yCoord  # Protected variable to store y-coordinate on map

  def setXCoord(self, xCoord):
    """
    Sets the x-coordinate of the Creature by user input.

    :param xCoord: x coordinate (row coordinate) of Creature's location.
    :type xCoord: int
    """
    self._x = xCoord
  
  def setYCoord(self, yCoord):
    """
    Sets the y-coordinate of the Creature by user input.

    :param yCoord: y coordinate (row coordinate) of Creature's location.
    :type yCoord: int
    """
    self._y = yCoord

  def getXCoord(self):
    """
    Returns the X-coordinate of the creature.

    :return: int Y
    """
    return self._x
  
  def getYCoord(self):
    """
    Returns the Y-coordinate (column coordinate) of the creature.

    :return: int Y
    """
    return self._y
