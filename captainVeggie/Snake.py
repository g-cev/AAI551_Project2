from Creature import Creature

#Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova
#Date: 11/24/2023
#Desc: Class file for 'Snake' class. Inherits FieldInhabitant class (superClass/parent) 'Creature'.
#       Will not be inherited by any other class.


class Snake(Creature):
    def __init__(self, xCoord, yCoord):
        # Provide values to Creature's constructor
        Creature.__init__(self, "S", xCoord, yCoord)