class Component(object):
    def __init__(self, *args, **kw):
        self.name=kw['name']
        pass
    
    def listar_elementos(self): 
        pass

class Arquivo(Component):
    def __init__(self, *args, **kw):
        Component.__init__(self, *args, **kw)
    
    def listar_elementos(self):
        print(self.name)

class Dir(Component):
    def __init__(self, *args, **kw):
        Component.__init__(self, *args, **kw)
        self.children = []

    def adicione_diretorio(self, child):
        self.children.append(child)

    def listar_elementos(self):
        print(self.name,' [')
        for x in self.children:
            x.listar_elementos()
        print(']')

def main():
    diretorio_fotos = Dir(name='fotos')
    diretorio_outubro = Dir(name='outubro')
    diretorio_novembro = Dir(name='novembro')
    diretorio_fotos.adicione_diretorio(diretorio_outubro)
    diretorio_fotos.adicione_diretorio(diretorio_novembro)
    
    foto1 = Arquivo(name='foto001.jpg')
    foto2 = Arquivo(name='foto002.jpg')
    foto3 = Arquivo(name='foto003.jpg')

    diretorio_fotos.adicione_diretorio(foto1)
    diretorio_outubro.adicione_diretorio(foto2)
    diretorio_novembro.adicione_diretorio(foto3)

    diretorio_fotos.listar_elementos()

if __name__ == '__main__':
    main()