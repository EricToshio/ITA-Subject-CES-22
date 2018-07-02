


class ControladorCompromissos:
    def __init__(self):
        self._membros = []
    
    def adicionar(self, membro):
        self._membros.append(membro)
    
    def advogados_livre(self):
        for membro in self._membros:
            if membro.profissao == 'Advogado'and not membro.ocupado:
                return membro.nome
        return None


class Advogado:
    def __init__(self, controlador,nome):
        self._controlador = controlador
        self.ocupado = False
        self.nome = nome
        self.profissao = 'Advogado'


class Engenheiro:
    def __init__(self, controlador,nome):
        self._controlador = controlador
        self.ocupado = False
        self.nome = nome
        self.profissao = 'Engenheiro'

    def procuro_advogado(self):
        nome=self._controlador.advogados_livre()
        if nome == None:
            print('Não existe advogados disponiveis.')
        else:
            print('Achei o advogado, ele se chama ', nome,'.')



def main():
    controlador = ControladorCompromissos()
    membro_1 = Advogado(controlador,'Joao')
    membro_2 = Engenheiro(controlador,'Pedro')
    controlador.adicionar(membro_1)
    controlador.adicionar(membro_2)

    print("Busca 1:")
    membro_2.procuro_advogado()

    print("Busca 2:")
    membro_1.ocupado=True
    membro_2.procuro_advogado()

if __name__ == "__main__":
    main()