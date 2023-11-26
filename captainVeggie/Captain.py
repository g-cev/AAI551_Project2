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

  def removeVeggie(self, num):
    # BONUS: removeVeggie function for Snake feature (steals Captain's veggies)
    # "num": the number of veggies to remove from Captain's basket
    for i in range(num):
      # If the basket is not empty
      if self.__basket:
        # Remove veggie
        self.__basket.pop()