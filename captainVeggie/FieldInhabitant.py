# Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova
# Date: 12/8/2023
# Desc: Class file for 'FieldInhabitant'. Will be inherited by subClasses (children) 'Creature' and 'Veggie' and
# sub-subClasses 'Captain' and 'Rabbit' (subclasses/children of Creature).

class FieldInhabitant:
  """
  Class defining FieldInhabitant object. Will be inherited by Veggie and Creature classes.

  
  Attributes:

  :param sym: Symbol of the field inhabitant. Will be printed on screen to represent position in field.
  :type sym: char
  """
  def __init__(self, sym = None):
    """
    Constructor for FieldInhabitant.
    Initializes sym.
    Default value of sym is None (NULL). Otherwise, will be char defined by input file.
    """
    self._symbol = sym  # Protected variable denoting symbol representation on map. Default val set to 'None'

  def setSymbol(self, sym):
    """
    Sets the FieldInhabitant object's symbol on user input sym.

    :param sym: User input for FieldInhabitant symbol represenation
    :type sym: char
    """
    self._symbol = sym

  def getSymbol(self):
    """
    Returns the symbol of the FieldInhabitant object, or it's inheritor.
    
    :return: char
    """
    return self._symbol
  
  def __str__(self):
    """
    Returns a formatted string to be used in the print() function.

    :return: string/char(?)
    """
    return f"{self._symbol}"
