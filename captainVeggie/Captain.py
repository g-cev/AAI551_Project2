from Creature import Creature

#Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova 
#Date: 11/18/2023
#Desc: Class file for 'Captain' class. Inherits FieldInhabitant class (superClass/parent). Will not be inherited by any other class.

class Captain(Creature):
  def __init__(self, xCoord, yCoord):
    Creature.__init__(self, "V", xCoord, yCoord)
    self.__basket = [] #empty list 'Basket' that will contain list of all veggies collected by captain.

  def addVeggie(self, veg): #veg is to be a Veggie-class object. adds vegetable object to list of collected vegetables.
    self.__basket.append(veg)

  #TODO: Need to test: are all appropriate getter/setter functions inherited already? Should be, but unsure.