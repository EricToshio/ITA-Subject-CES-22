'''
Exercício:
Desenvolva um Decorador exemplo, crie um exemplo de função com lista de argumentos e dicionarios de argumentos
'''


def add_border(func):
    def func_wrapper(*arg, **dic):
        print(30*('<>'))
        print('{0}'.format(func(*arg, **dic)))
        print(30*('<>'))
    return func_wrapper

@add_border
def List_nicely(*arg, **dic):
    string = "There it are all your arguments:\n"
    for element in arg:
        string += "{0:^15}\n".format(str(element))
    string += (60*'=')+"\n"
    string += "There it are all your dictionaries(variables):\n"
    for key in dic:
        string += "{0:>8}:{1:<8}\n".format(str(key), str(dic[key]))
    return string

List_nicely('Joao', 'Pedro', 'Jose', Brasil = 'Bom' , Usa ='Otimo')