# Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova
# Date: 12/8/2023
# Desc: Class file for 'Veggie' class. Inherits FieldInhabitant class (superClass/parent). Not inherited by any other class.

from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):
  def __init__(self, sym, name, points):
    # Provide values to FieldInhabitant's constructor
    FieldInhabitant.__init__(self, sym)
    self.__name = name  # Full name of the veggie
    self.__points = points  # Number of points veggie is worth

  def setName(self, name):
    self.__name = name

  def setPoints(self, points):
    self.__points = points

  def getName (self):
    return self.__name
  
  def getPoints(self):
    return self.__points
  
  def __str__(self):
    return f"{self._symbol}: {self.__name}, {self.__points} points"
