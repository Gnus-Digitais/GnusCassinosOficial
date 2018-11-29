class Ranking:
    """Classe responsavel por gerenciar as buscas e registros no ranking dos jogos.
    Recebe por parâmetro o nome do jogo a se buscar o ranking."""
    def __init__(self, jogo):
        self.__jogo = jogo  # Nome do Jogo

    # GET jogo
    @property
    def jogo(self):
        return self.__jogo

    # SET jogo
    @jogo.setter
    def jogo(self, valor):
        self.__jogo = valor

    def __insertion_sort_matriz(self, matriz_entrada):
        """Método que implementa o algoritmo Insertion Sort. Resposável por ordenar a matriz de ranking.
        Recebe uma matriz_entrada contendo o ranking quase ordenado e retorna uma matriz totalmente ordenada.
        OBS: Foi realizada uma modificação para que a ordenação seja decrescente"""

        lista = [[int(i[1]), i[0]] for i in matriz_entrada]  # Inverte as posições dos itens de cada linha da matriz
        for i in range(1, len(lista)):  # Loop que vai de 1 ao tamanho do vetor menos 1
            chave = lista[i]  # Atribui o item da matriz lista na posição i a variável chave
            k = i  # Varável K recebe índice i.
            while k > 0 and chave > lista[k - 1]:  # Enquanto k for maior 0 e chave maior que matriz na posição k-1
                lista[k] = lista[k - 1]  # A posição k da lista recebe lista na posição k - 1
                k -= 1  # Decresce o valor de k
            lista[k] = chave  # A posição k da lista recebe o valor de chave
        return [i[::-1] for i in lista]  # Inverte as posições dos itens de cada linha da matriz e retorna

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
                return [['0', 0]]*10
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
            txt += vetor[0]+'|'+str(vetor[1])+'\n'
        arq.write(txt)  # Escreve no arquivo os as informações sobre o ranking
        arq.close()

    def add_record(self, apelido, pontuacao):
        """Método responsável por coletar e tratar as informações a serem gravadas no ranking.
        Recebe os parâmetros apelido e pontuacao."""

        lista = self.__ler_ranking()  # Recebe uma matriz contendo as informações do ranking
        lista.append([apelido, str(pontuacao)])
        ordenado = self.__insertion_sort_matriz(lista)
        ordenado.pop()
        self.__gravar_ranking(ordenado)

    def retorna_ranking(self):
        """Metodo que retorna uma string contendo os 10 primeiros colocados no Ranking do jogo"""

        string = ""
        matriz_rank = self.__ler_ranking()  # Recebe uma matriz contendo as informações do ranking
        for i in range(len(matriz_rank)):
            string += matriz_rank[i][0] + "\t" + str(matriz_rank[i][1]) + "\n"  # Adiciona dados da matriz em uma string
        return string.strip()  # retorna a string contendo o ranking
