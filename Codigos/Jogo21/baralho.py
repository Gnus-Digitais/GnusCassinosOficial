import random

#melhor team: "G'NUS DIGITAIS"> Matheus Dias, Bruno Felipe, Rodrigo Rocca e Igor Ramos..
class Baralho:
    """Classe que manipula um baralho comum de 52 cartas"""

    def __init__(self):
        self.baralho = []
        self.naipes = ['copas', 'espadas', 'ouros', 'paus']
        self.embalharada = None

    def gerar_baralho(self):
        """Gera um baralho de 52 cartas, divididas em 4 naipes. as cartas são representadas por
        um vetor [a, b, c], sendo: a = inteiro representando o valor numerico da carta; b = string
        representando o valor facial da carta; c = string representando o naipe da carta. Matriz 52x3"""
        for i in self.naipes:
            for j in range(2, 12):
                if j < 10:
                    self.baralho.append([j, str(j), i])
                elif j == 10:
                    self.baralho.append([j, "Q", i])
                    self.baralho.append([j, "J", i])
                    self.baralho.append([j, "K", i])
                elif j == 11:
                    self.baralho.append([j, "A", i])

    def mostrar_baralho(self):
        """Retorna a matriz contendo o baralho"""
        return self.baralho

    def fisher_yates_shuffle(self, vet_ordenado):
        """Implementa o algoritmo avançado Fisher Yates Shuffle. Esse algoritmo embaralha os itens
        de uma sequencia finita (vetor) e a retorna"""
        vetor_ordenado = [i for i in vet_ordenado]
        a = len(vetor_ordenado)
        b = a - 1
        for d in range(b, 0, -1):
            e = random.randint(0, d)
            if e == d:
                continue
            vetor_ordenado[d], vetor_ordenado[e] = vetor_ordenado[e], vetor_ordenado[d]
        self.embalharada = vetor_ordenado
        return vetor_ordenado

    def pilha_embaralhar(self):
        """Embaralha a pilha de cartas"""
        self.fisher_yates_shuffle(self.baralho)
        return self.embalharada

    def topo_da_pilha(self):
        """Retira o topo da pilha e o retorna"""
        return self.embalharada.pop()
