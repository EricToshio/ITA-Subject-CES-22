'''
Execício:
Crie um exemplo usando métodos abstratos, métodos estáticos e métodos de classe.
O exemplo deve ilustrar as vantagens de cada tipo de método
'''
import abc


####################################################################################################

# Método Abstrato

class Menu():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_price(self):
        """Return the price of the food"""

    @abc.abstractmethod
    def get_descrition(self):
        """Return the description of the food"""


class Pizza(Menu):

    def get_price(self):
        return '16 reais'

    def get_descrition(self):
        return 'A deliciosa pizza de mussarela!'


'''
A vantagem do método abstrato é evitar que as classes filhas dele
sejam implementadas sem os metodos abstratos obrigatorios.
'''
Menu()
# print(Pizza().get_descrition())

####################################################################################################

# Método estático

class Cachorro():

    @staticmethod
    def numero_de_patas():
        return 4

Cachorro.numero_de_patas()

'''
A vantagem do método estático é abstrato e que não é necessário usar ele por meio de um objeto da classe.
Bem útil para metodos que são indiferentes ao estado da classe(variaveis)
'''
####################################################################################################

# Método de classe
class Aluno():

    def __init__(self, name, age, is_a_good_student):
        self.name = name
        self.age = age
        self.is_a_good_student = is_a_good_student

    @classmethod
    def Joao(cls):
        return cls('Joao', 17, True)

    @classmethod
    def Pedro(cls):
        return cls('Pedro', 18, False)

Joao = Aluno.Joao()

'''
A vatagem do método de classe é poder facilmente declarar objetos pre-definidos pela classe
'''