'''
Exercício:
Crie extensões no exemplo de classes de polígonos regulares de modo a avaliar os diferentes MROs possiveis
'''

#Exemplo de poligonos Regulares


class Shape:
    geometric_type = 'Generic Shape'


class Plotter:
    pass


class Polygon(Shape, Plotter):
    geometric_type = 'Polygon'


class RegularPolygon(Polygon):
    geometric_type = 'Regular Polygon'


class RegularHexagon(RegularPolygon):
    geometric_type = 'Regular Hexagon'


class Square(RegularPolygon):
    geometric_type = 'Square'

# Extensoes

class Extension1(RegularPolygon):
    pass

class Extension2(Plotter, Shape):
    pass

class Extension3(Extension2):
    pass

class Extension4(RegularHexagon, Square):
    pass

# MROS


print('MRO da classe square:', Square.__mro__)

print('MRO da classe extension1:', Extension1.__mro__)

print('MRO da classe extension2:', Extension2.__mro__)

print('MRO da classe extension3:', Extension3.__mro__)

print('MRO da classe extension4:', Extension4.__mro__)

