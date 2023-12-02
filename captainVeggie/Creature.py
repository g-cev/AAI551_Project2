# Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova
# Date: 12/8/2023
# Desc: Class file for 'Creature' class. Inherits FieldInhabitant class (superClass/parent). Will be inherited by
# 'Captain' and 'Rabbit' classes (subclasses/children).

from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
  def __init__(self, sym, xCoord, yCoord):  # Inherits "setSymbol"/"getSymbol" funcs
    FieldInhabitant.__init__(self, sym) 
    self._x = xCoord  # Protected variable to store x-coordinate on map
    self._y = yCoord  # Protected variable to store y-coordinate on map

  def setXCoord(self, xCoord):
    self._x = xCoord
  
  def setYCoord(self, yCoord):
    self._y = yCoord

  def getXCoord(self):
    return self._x
  
  def getYCoord(self):
    return self._y
