import abc


class Robo:
    def __init__(self, state):
        self._state = state

    def resposta_ao_sensor(self, sensor_obstaculo):
        self._state.acao(self,sensor_obstaculo)


class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def acao(self,robo,sensor_obstaculo):
        pass


class Andando(State):
    def acao(self,robo,sensor_obstaculo):
        print('O robo está andando')
        if sensor_obstaculo is True:
            robo._state=Desviando()
            print('Ele mudou para desviando')
        else:
            print('Ele continou andando')

class Desviando(State):
    def acao(self,robo,sensor_obstaculo):
        print('O robo está desviando')
        if sensor_obstaculo is False:
            robo._state=Andando()
            print('Ele mudou para andando')
        else:
            print('Ele continou desviando')


def main():
    robo = Robo(Andando())
    print("Sinal 1:")
    robo.resposta_ao_sensor(True)
    print("Sinal 2:")
    robo.resposta_ao_sensor(False)
    print("Sinal 3:")
    robo.resposta_ao_sensor(False)
    print("Sinal 4:")
    robo.resposta_ao_sensor(True)
    print("Sinal 5:")
    robo.resposta_ao_sensor(True)


if __name__ == "__main__":
    main()