class Ficha:
    def __init__(self):
        self.__valor = None
        self.__cor = None

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, valor):
        self.__cor = valor

    def gerar_ficha(self):
        pass