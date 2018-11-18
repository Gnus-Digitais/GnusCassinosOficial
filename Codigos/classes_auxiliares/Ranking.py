class Ranking:
    def __init__(self, jogo, dificuldade):
        self.__dificuldade = dificuldade
        self.__jogo = jogo

    @property
    def dificuldade(self):
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, valor):
        self.__dificuldade = valor
                             
    @property
    def jogo(self):
        return self.__jogo

    @jogo.setter
    def jogo(self, valor):
        self.__jogo = valor

    def __ler_ranking(self):
        """Metodo que faz a leitura do arquivo de Ranking"""
        try:
            result = []
            if self.jogo == 'blackjack':
                arq = open("../Jogo21/rankings/" + self.__jogo + '_' + self.__dificuldade + '.txt', "r", encoding="UTF-8")
            elif self.jogo == 'slotmachine':
                arq = open("../slotmachine/rankings/" + self.__jogo + '_' + self.__dificuldade + '.txt', "r", encoding="UTF-8")
            elif self.jogo == 'megastacker':
                arq = open("../MegaStacker/rankings/"+self.__jogo + '_' + self.__dificuldade + '.txt', "r",encoding="UTF-8")
            for linha in arq.read().split():
                colocacao = linha.split('|')
                result.append(colocacao)
            arq.close()
            if result != []:
                return result
            else:
                return [['0', 0, '0']]*10
        except FileNotFoundError:
            arquivo = open("rankings/"+self.__jogo + '_' + self.__dificuldade + '.txt', 'w+')
            arquivo.close()
            self.__ler_ranking()

    def __gravar_ranking(self, vetor_ranking):
        """Metodo responsavel por salvar resultados no arquivo de Ranking"""

        if self.jogo == 'blackjack':
            arq = open("../Jogo21/rankings/" + self.__jogo + '_' + self.__dificuldade + '.txt', "w", encoding="UTF-8")
        elif self.jogo == 'slotmachine':
            arq = open("../slotmachine/rankings/" + self.__jogo + '_' + self.__dificuldade + '.txt', "w", encoding="UTF-8")
        elif self.jogo == 'megastacker':
            arq = open("../MegaStacker/rankings/" + self.__jogo + '_' + self.__dificuldade + '.txt', "w", encoding="UTF-8")
        txt = ""
        for vetor in vetor_ranking:
            txt += vetor[0]+'|'+str(vetor[1])+'|'+vetor[2]+'\n'
        arq.write(txt)
        arq.close()

    def addRecord(self, nickname, pontuacao):
        """Método responsável por coletar e tratar as informações a serem gravadas no ranking"""

        lista = self.__ler_ranking()
        n = 0
        for i in lista:
            if pontuacao > int(i[1]):
                lista.insert(n, [nickname, pontuacao, self.__dificuldade])
                if len(lista) > 10:
                    lista.pop()
                self.__gravar_ranking(lista)
                return lista
            n += 1

    def retorna_ranking(self):
        """Metodo que retorna uma string contendo os 10 primeiros colocados no Ranking do jogo"""

        string = ""
        vetor_rank = self.__ler_ranking()
        for i in range(len(vetor_rank)):
            string = string + vetor_rank[i][0] + "\t" + vetor_rank[i][1] + "\n"
        return string.strip()


