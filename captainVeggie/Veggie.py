# Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova
# Date: 12/8/2023
# Desc: Class file for 'Veggie' class. Inherits FieldInhabitant class (superClass/parent). Not inherited by any other class.

from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):
  """
  A class to represent the Veggie object. Inherits from FieldInhabitant class in FieldInhabitant.py

  
  Attributes:

  :param sym: Symbol for the Veggie object, which will be represented on the field when printed.
  :type sym: char

  :param name: The name of the vegetable. This will be used when the user is shown the breakdown of what vegetables they collected.
  :type name: string

  :param points: The number of points the veggie is worth. This will contribute to the user's final score.
  :type points: int
  """
  def __init__(self, sym, name, points):
    """
    Initializes sym parameter via FieldInhabitant constructor.
    Initializes name and points params.
    """
    FieldInhabitant.__init__(self, sym)
    self.__name = name  # Full name of the veggie
    self.__points = points  # Number of points veggie is worth

  def setName(self, name):
    """
    Sets the Veggie object's name.
    :param name: Name given by user.
    :type name: string
    """
    self.__name = name

  def setPoints(self, points):
    """
    Sets the Veggie object's point value.
    :param points: Point value given by user.
    :type points: int
    """
    self.__points = points

  def getName (self):
    """
    Returns veggie object's name.

    :return: string
    """
    return self.__name
  
  def getPoints(self):
    """
    Returns point value of Veggie object.

    :return: int
    """
    return self.__points
  
  def __str__(self):
    """
    Returns properly formatted string for use in print() function.

    :return: int

    Sample return: "O: Onion, 5 points"
    """
    return f"{self._symbol}: {self.__name}, {self.__points} points"
