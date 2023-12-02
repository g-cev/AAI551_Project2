# Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova
# Date: 12/8/2023
# Desc: Class file for 'Rabbit' class. Inherits Creature class (superClass/parent). Not inherited by any other class.

from Creature import Creature

class Rabbit(Creature):
  def __init__(self, xCoord, yCoord):
    # Provide values to Creature's constructor
    Creature.__init__(self, "R", xCoord, yCoord)
