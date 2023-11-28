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

  #returns bool. asks if basket is empty or not (True = not empty, False = empty)
  def checkBasket(self):
    if not self.__basket:
      return False
    else:
      return True

  #returns basket list
  def getBasket(self):
    return self.__basket
  
  #returns the length of basket list to find total number of veggies collected
  def getBasketVeggieCount(self):
    return len(self.__basket)
  
  #returns set of unique vegetables collected by captain. will be used in gameOver function.
  def getUniqueVeggies(self):
    uniqueVeggies = set()
    #for every single vegetable in cap's basket
    for veg in self.__basket:
      #add veg to set. repeats will not be added.
      uniqueVeggies.add(veg)

    return uniqueVeggies

  def removeVeggie(self, num):
    # BONUS: removeVeggie function for Snake feature (steals Captain's veggies)
    removed_count = 0
    points_lost = 0

    for i in range(num):
      # If the basket is not empty
      if self.__basket:
        # Remove veggie
        removed_count += 1
        points_lost += self.__basket[-1].getPoints()
        self.__basket.pop(-1)

    return removed_count, points_lost