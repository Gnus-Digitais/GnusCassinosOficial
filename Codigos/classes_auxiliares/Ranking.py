class Ranking:
    """Classe responsavel por gerenciar as buscas e registros no ranking dos jogos.
    Recebe por parâmetro o nome do jogo a se buscar o ranking."""
    def __init__(self, jogo):
        self.__jogo = jogo

    # GET jogo
    @property
    def jogo(self):
        return self.__jogo

    # SET jogo
    @jogo.setter
    def jogo(self, valor):
        self.__jogo = valor

    def __ler_ranking(self):
        """Metodo privado que faz a leitura do arquivo de Ranking"""
        arq = None
        try:  # Tenta abrir arquivo de ranking do jogo selecionado
            result = []
            # Escolhe o arquivo a partir do jogo informado
            if self.jogo == 'blackjack':
                arq = open("../Jogo21/rankings/" + self.__jogo + '.txt', "r", encoding="UTF-8")
            elif self.jogo == 'slotmachine':
                arq = open("../slotmachine/rankings/" + self.__jogo + '.txt', "r", encoding="UTF-8")
            elif self.jogo == 'megastacker':
                arq = open("../MegaStacker/rankings/"+self.__jogo + '.txt', "r", encoding="UTF-8")
            for linha in arq.read().split():
                colocacao = linha.split('|')
                result.append(colocacao)
            arq.close()
            if result != []:
                return result
            else:
                return [['0', 0, '0']]*10
        except FileNotFoundError:  # Caso o arquivo não exista
            # Cria arquivo de ranking
            arquivo = open("rankings/"+self.__jogo + '.txt', 'w+')
            arquivo.close()  # Fecha o arquivo criado
            self.__ler_ranking()  # chama recursivamente o Método __ler_ranking()

    def __gravar_ranking(self, vetor_ranking):
        """Metodo privado responsavel por salvar resultados no arquivo de Ranking.
        Recebe um vetor contendo as informações a serem gravadas"""
        arq = None
        # Escolhe o arquivo aonde deve gravar as informações
        if self.jogo == 'blackjack':
            arq = open("../Jogo21/rankings/" + self.__jogo + '.txt', "w", encoding="UTF-8")
        elif self.jogo == 'slotmachine':
            arq = open("../slotmachine/rankings/" + self.__jogo + '.txt', "w", encoding="UTF-8")
        elif self.jogo == 'megastacker':
            arq = open("../MegaStacker/rankings/" + self.__jogo + '.txt', "w", encoding="UTF-8")
        txt = ""
        for vetor in vetor_ranking:
            txt += vetor[0]+'|'+str(vetor[1])+'|'+vetor[2]+'\n'
        arq.write(txt)  # Escreve no arquivo os as informações sobre o ranking
        arq.close()

    def add_record(self, apelido, pontuacao):
        """Método responsável por coletar e tratar as informações a serem gravadas no ranking.
        Recebe os parâmetros apelido e pontuacao."""

        lista = self.__ler_ranking()  # Recebe uma matriz contendo as informações do ranking
        index_ranking = 0  # Váriavel de controle
        for i in lista:
            if pontuacao > int(i[1]):  # Caso a pontuação seja maior que o valor da linha i da matriz na posição 1
                lista.insert(index_ranking, [apelido, pontuacao])  # Insere dados do jogador como linha da matriz
                if len(lista) > 10:  # Se o tamanho da matriz for maior que 10
                    lista.pop()  # Apaga a ultima linha
                self.__gravar_ranking(lista)  # Chama o método __gravar_ranking() para salvar as alterações feitas

            index_ranking += 1  # incrementa váriavel de controle

    def retorna_ranking(self):
        """Metodo que retorna uma string contendo os 10 primeiros colocados no Ranking do jogo"""

        string = ""
        matriz_rank = self.__ler_ranking()  # Recebe uma matriz contendo as informações do ranking
        for i in range(len(matriz_rank)):
            string += matriz_rank[i][0] + "\t" + matriz_rank[i][1] + "\n"  # Adiciona dados da  da matriz em uma string
        return string.strip()  # retorna a string contendo o ranking
