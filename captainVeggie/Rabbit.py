# Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova
# Date: 12/8/2023
# Desc: Class file for 'Rabbit' class. Inherits Creature class (superClass/parent). Not inherited by any other class.

from Creature import Creature

class Rabbit(Creature):
  """
  Class for defining Rabbit() objects. Inherits Creature class attributes.

  Attributes:

  :param xCoord: X-Coordinate of the Rabbits's location on the printed field. This will be continuously updated at random as the game continues, to simulate random movement.
  :type xCoord: int

  :param yCoord: Y-Coordinate of the Rabbit's location on the printed field. This will be continuously updated at random as the game continues, to simulate random movement.
  :type yCoord: int
  """
  def __init__(self, xCoord, yCoord):
    """
    Constructor for the Rabbit class. Initializes parameters mentioned above.
    Symbol variable "sym" is set to the letter "R" for representation on printed field.
    """
    # Provide values to Creature's constructor
    Creature.__init__(self, "R", xCoord, yCoord)
