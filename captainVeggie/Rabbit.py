from Creature import Creature

#Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova 
#Date: 11/18/2023
#Desc: Class file for 'Rabbit' class. Inherits FieldInhabitant class (superClass/parent). Will not be inherited by any other class.

class Rabbit(Creature):
  def __init__(self, xCoord, yCoord):
    Creature.__init__(self, "R", xCoord, yCoord)

    #TODO: Need to test: are all appropriate getter/setter functions inherited already? Should be, but unsure.