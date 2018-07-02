import abc

#FABRICA ABSTRATA
class Montadora(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def criar_carro(self):
        pass

    @abc.abstractmethod
    def criar_moto(self):
        pass

#FABRICA CONCRETA 1
class Honda(Montadora):

    def criar_carro(self):
        return Carro_Honda()

    def criar_moto(self):
        return Moto_Honda()

#FABRICA CONCRETA 2
class Mercedes(Montadora):

    def criar_carro(self):
        return Carro_Mercedes()

    def criar_moto(self):
        return Moto_Mercedes()

#PRODUTO 1 ABSTRATO
class Carro(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def interface_carro(self):
        pass

#PRODUTO 1 CONCRETO
class Carro_Honda(Carro):

    def interface_carro(self):
        print('Carro da Honda')

#PRODUTO 1 CONCRETO
class Carro_Mercedes(Carro):

    def interface_carro(self):
        print('Carro da Mercedes')

#PRODUTO 2 ABSTRATO
class Moto(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def interface_moto(self):
        pass

#PRODUTO 2 CONCRETO
class Moto_Honda(Moto):

    def interface_moto(self):
        print('Moto da Honda')
        

#PRODUTO 2 CONCRETO
class Moto_Mercedes(Moto):

    def interface_moto(self):
        print('Moto da Mercedes')


def main():
    for fabrica in (Honda(), Mercedes()):
        automovel_1 = fabrica.criar_carro()
        automovel_2 = fabrica.criar_moto()
        automovel_1.interface_carro()
        automovel_2.interface_moto()


if __name__ == "__main__":
    main()