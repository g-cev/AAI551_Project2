from FieldInhabitant import FieldInhabitant

#Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova 
#Date: 11/18/2023
#Desc: Class file for 'Creature' class. Inherits FieldInhabitant class (superClass/parent). Will be inherited by 'Captain' and 'Rabbit' classes (subclasses/children)

class Creature(FieldInhabitant):
  def __init__(self, sym, xCoord, yCoord): #inherits "setSymbol"/"getSymbol" funcs. 
    FieldInhabitant.__init__(self, sym) 
    self._x = xCoord #protected variable _x to store x-coordinate on map.
    self._y = yCoord #protected variable _y to store y-coordinate on map.

  def setXCoord(self, xCoord):
    self._x = xCoord
  
  def setYCoord(self, yCoord):
    self._y = yCoord

  def getXCoord(self):
    return self._x
  
  def getYCoord(self):
    return self._y

  #Should there be another function that returns both coords at once?


  