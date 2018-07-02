import abc


class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def description(self):
        pass


class Decorator(Component, metaclass=abc.ABCMeta):
    def __init__(self, component):
        self._component = component

    @abc.abstractmethod
    def description(self):
        pass


class Barata(Decorator):
    def description(self):
        print("Seja barata!")
        self._component.description()


class Grande(Decorator):
    def description(self):
        print("Seja grande!")
        self._component.description()


class Casa(Component):
    def description(self):
        print("Seja bonita!")


def main():
    
    casa = Casa()
    print("Quero uma casa que: ")
    Barata(Grande(casa)).description()
    print("Esta é a casa que eu quero =D")



if __name__ == "__main__":
    main()