class Viga:
    def __init__(self, base, altura, comprimento):
        self.__base = base
        self.__altura = altura
        self.__comprimento = comprimento

    def calcular_volume(self):
        return self.__base * self.__altura * self.__comprimento
