class Raking:
    def __init__(self, nick, ponto, dificuldade):
        self.__nickname = nick
        self.__pontuacao = ponto
        self.__dificuldade = dificuldade
        
    
    @property
    def nickname(self):
        return self.__nickname
    
    @nickname.setter
    def nickname(self, valor):
        self.__nickname = valor

    @property
    def pontuacao(self):
        return self.__pontuacao

    @pontuacao.setter
    def pontuacao(self, valor):
        self.__pontuacao = valor

    @property
    def dificuldade(self):
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, valor):
        self.__dificuldade = valor

    def gerarRanking(self):
        pass