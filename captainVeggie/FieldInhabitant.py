#Name: Genesis Cevallos, Eugene Kozlakov, Aleese Mukhamedjanova 
#Date: 11/18/2023
#Desc: Class file for 'FieldInhabitant' Will be inherited by subClasses (children) 'Creature' and 'Veggie' and sub-subClasses 'Captain' and 'Rabbit' (subclasses/children of Creature)

class FieldInhabitant:
  def __init__(self, sym = None):
    self._symbol = sym #protected variable 'symbol' meant to denote symbol representation that will be shown on map. Default val set to 'None' (NULL)

  #TODO: Investigate whether more functions/vars/attributes are needed for this class.

  def setSymbol(self, sym):
    self._symbol = sym

  def getSymbol(self):
    return self._symbol
  
  def __str__(self): #TODO: double check necessity
    return f"{self._symbol}"
