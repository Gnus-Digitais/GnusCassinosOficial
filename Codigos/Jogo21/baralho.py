from Codigos.classes_auxiliares.RandInt import RandInt
from Codigos.Jogo21.Pilha import Pilha

#melhor team: "G'NUS DIGITAIS"> Matheus Dias, Bruno Felipe, Rodrigo Rocca e Igor Ramos..
class Baralho:
    """Classe que manipula um baralho francês de 52 cartas"""

    def __init__(self):
        self.baralho = []
        self.naipes = ['copas', 'espadas', 'ouros', 'paus']
        self.embalharada = None
        self.pilha=Pilha()

    def gerar_baralho(self):
        """Gera um baralho de 52 cartas, divididas em 4 naipes. as cartas são representadas por
        um vetor [a, b, c], sendo: a = inteiro representando o valor numerico da carta; b = string
        representando o valor facial da carta; c = string representando o naipe da carta. Matriz 52x3"""
        for i in self.naipes:
            for j in range(2, 12):
                if j < 10:
                    self.baralho.append([j, str(j), i])
                elif j == 10:
                    self.baralho.append([j, str(j), i])
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
        rand = RandInt()
        vetor_ordenado = [i for i in vet_ordenado]
        a = len(vetor_ordenado)
        b = a - 1
        for d in range(b, 0, -1):
            e = rand.numero_aleatorio(d)
            if e == d:
                continue
            vetor_ordenado[d], vetor_ordenado[e] = vetor_ordenado[e], vetor_ordenado[d]
        self.embalharada = vetor_ordenado
        return vetor_ordenado

    def pilha_embaralhar(self):
        """Embaralha a pilha de cartas"""
        self.fisher_yates_shuffle(self.baralho)
        for j in range(len(self.embalharada)):
            self.pilha.empilha(self.embalharada[j]) # Empilhando o baralho dentro da pilha.
        return self.pilha

    def topo_da_pilha(self):
        """Retira o topo da pilha e o retorna"""
        self.embalharada.pop()  # só para ficar igual a pilha de estrutura de dados...
        return self.pilha.desempilha() # retira o topo da pilha, usando função desempilha() da classe Pilha.
