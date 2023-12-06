# Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova
# Date: 12/8/2023
# Desc: Class file for 'Snake' class. Inherits Creature class (superClass/parent). Not inherited by any other class.

from Creature import Creature

class Snake(Creature):
    """
    Class for defining the Snake() object. Inherits Creature class attributes.

    Attributes:

  :param xCoord: X-Coordinate of the Snake's location on the printed field.
  :type xCoord: int

  :param yCoord: Y-Coordinate of the Snake's location on the printed field.
  :type yCoord: int
    """
    def __init__(self, xCoord, yCoord):
        # Provide values to Creature's constructor
        Creature.__init__(self, "S", xCoord, yCoord)
