from FieldInhabitant import FieldInhabitant

#Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova 
#Date: 11/18/2023
#Desc: Class file for 'Veggie' class. Inherits FieldInhabitant class (superClass/parent). Will not be inherited by any other class.

class Veggie(FieldInhabitant):
  def __init__(self, sym, name, points): #"a parameter representing the name and symbol of the vegetable... what?"
    FieldInhabitant.__init__(self, sym)
    self.__name = name #name of the actual vegetable. not sure how we can combine this into one.
    self.__points = points #number of points veggie is worth

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
    

