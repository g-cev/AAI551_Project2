# Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova
# Date: 12/8/2023
# Desc: Class file for 'FieldInhabitant'. Will be inherited by subClasses (children) 'Creature' and 'Veggie' and
# sub-subClasses 'Captain' and 'Rabbit' (subclasses/children of Creature).

class FieldInhabitant:
  def __init__(self, sym = None):
    self._symbol = sym  # Protected variable denoting symbol representation on map. Default val set to 'None'

  def setSymbol(self, sym):
    self._symbol = sym

  def getSymbol(self):
    return self._symbol
  
  def __str__(self):
    return f"{self._symbol}"
