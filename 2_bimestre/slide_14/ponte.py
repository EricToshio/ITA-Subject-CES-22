class AbstractInterface:
    def arrumar(self):
        raise NotImplemented()

class Bridge(AbstractInterface):
    def __init__(self):
        self.__implementation = None

class furou_roda(Bridge):
    def __init__(self, implementation):
        self.__implementation = implementation
    def arrumar(self):
        print ("foram arrumadas ", self.__implementation.rodas, " rodas")
        self.__implementation.estado()

class queimou_luz(Bridge):
    def __init__(self, implementation):
        self.__implementation = implementation
    def arrumar(self):
        print ("foram arrumados ", self.__implementation.farois, " farois")
        self.__implementation.estado()

class ImplementationInterface:
    def estado(self):
        raise NotImplemented

class Carro(ImplementationInterface):
    rodas = 4
    farois = 5
    def estado(self):
        print("Motorista do carro está feliz!")
        

class Moto(ImplementationInterface):
    rodas = 2
    farois = 3
    def estado(self):
        print("Motorista da moto está feliz!")

def main():
    motorista1 = Carro()
    motorista2 = Moto()

    # Couple of variants under a couple
    # of operating systems.
    useCase = furou_roda(motorista1)
    useCase.arrumar()
    useCase = furou_roda(motorista2)
    useCase.arrumar()
    useCase = queimou_luz(motorista1)
    useCase.arrumar()
    useCase = queimou_luz(motorista2)
    useCase.arrumar()

if __name__ == '__main__':
    main()