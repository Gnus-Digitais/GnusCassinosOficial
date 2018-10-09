class NodoArvore:
	"""Esta classe representa um nodo de uma árvore."""
	def __init__(self, dado=0, esquerda=None, direita=None):
		self.dado = dado
		self.esquerda = esquerda
		self.direita = direita

	def __repr__(self, espacamento=0):
		"""String de retorno"""
		ret = ""

		# Imprime o(s) nó(s) da direita
		if self.direita != None:
			ret += self.direita.__repr__(espacamento + 1)

		# Imprime o valor que está no nó
		ret += "\n" + ("    "*espacamento) + str(self.dado)

		# Imprime o(s) nó(s) da esquerda
		if self.esquerda != None:
			ret += self.esquerda.__repr__(espacamento + 1)

		return ret

class ArvoreBinaria:
	"""Esta classe representa uma árvore binária."""
	def __init__(self):
		self.raiz = None

	def __repr__(self):
		return "*** Árvore ***\n"+str(self.raiz)

	def insere(self, nodo_partida, valor):
		"""Insere um nodo em uma árvore binária de pesquisa."""
		# Cria um nodo_temporário com o valor passado
		nodo_temp = NodoArvore(valor)
		# Nodo deve ser inserido na raiz.
		# Caso a árvore esteja vazia
		if nodo_partida == None:
			self.raiz = nodo_temp
		# Nodo deve ser inserido na subárvore direita.
		elif nodo_temp.dado > nodo_partida.dado:
			if nodo_partida.direita == None:
				nodo_partida.direita = nodo_temp
			else:
				self.insere(nodo_partida.direita, valor)
		# Nodo deve ser inserido na subárvore esquerda.
		else:
			if nodo_partida.esquerda == None:
				nodo_partida.esquerda = nodo_temp
			else:
				self.insere(nodo_partida.esquerda, valor)

	def busca(self,nodo_partida,valor):
		if nodo_partida==None:
			return None
		elif valor==nodo_partida.dado:
			return nodo_partida.dado
		elif valor>nodo_partida.dado:
			return self.busca(nodo_partida.direita,valor)
		else:
			return self.busca(nodo_partida.esquerda,valor)

	def maximo(self):
		nodo_temp=self.raiz
		while nodo_temp.direita!=None:
			nodo_temp=nodo_temp.direita
		return nodo_temp.dado

	def minimo(self):
		nodo_temp=self.raiz
		while nodo_temp.esquerda!=None:
			nodo_temp=nodo_temp.esquerda
		return nodo_temp.dado

	def altura(self):
		if self.raiz==None:
			return 0
		else:
			#maior
			nd=0
			ne=0
			nodo_temp=self.raiz
			while(nodo_temp.direita!=None):
				nodo_temp=nodo_temp.direita
				nd=nd+1
			#menor
			nodo_temp = self.raiz
			while (nodo_temp.esquerda != None):
				nodo_temp = nodo_temp.esquerda
				ne = ne + 1
			if nd>=ne:
				return nd+1
			else:
				return ne+1
	# menor

def verifica_igualdade(x,y):
	#vou verificar se a arvore x é igual a arvore y..
	if x ==None and y==None:
		return True
	elif x!=None and y!=None:
		if (x.dado == y.dado) and (verifica_igualdade(x.esquerda, y.esquerda)) and  (verifica_igualdade(x.direita, y.direita)):
			return True
		else:
			 return False
	else:
		return False

def testeArvore():

    arvore=ArvoreBinaria()
    arvore.insere(arvore.raiz,10)
    arvore.insere(arvore.raiz,13)
    arvore.insere(arvore.raiz,12)
    arvore.insere(arvore.raiz,16)
    arvore.insere(arvore.raiz,15)
    arvore.insere(arvore.raiz,8)
    arvore.insere(arvore.raiz,9)
    arvore.insere(arvore.raiz,5)
    arvore.insere(arvore.raiz,3)
    arvore.insere(arvore.raiz, 209)
    arvore.insere(arvore.raiz,18)
    arvore.insere(arvore.raiz,6)
    arvore.insere(arvore.raiz,13)
    #arvore.insere(arvore.raiz,209)
    arvore.insere(arvore.raiz,10)

    print(arvore)
    print(arvore.altura())
    print(arvore.busca(arvore.raiz,35))
    print(arvore.maximo())#sem nodo partida(raiz)
    print(arvore.minimo())#sem nodo partida(raiz)

    #arvore 2
    arvore2 = ArvoreBinaria()
    arvore2.insere(arvore2.raiz, 10)
    arvore2.insere(arvore2.raiz, 13)
    arvore2.insere(arvore2.raiz, 12)
    arvore2.insere(arvore2.raiz, 16)
    arvore2.insere(arvore2.raiz, 15)
    arvore2.insere(arvore2.raiz, 8)
    arvore2.insere(arvore2.raiz, 9)
    arvore2.insere(arvore2.raiz, 5)
    arvore2.insere(arvore2.raiz, 3)
    arvore2.insere(arvore2.raiz, 209)
    arvore2.insere(arvore2.raiz, 18)
    arvore2.insere(arvore2.raiz, 6)
    arvore2.insere(arvore2.raiz, 13)
    arvore2.insere(arvore2.raiz, 10)
    arvore2.insere(arvore2.raiz,2)
    print(arvore2)
    print(arvore2.altura())
    print(arvore2.busca(arvore2.raiz, 35))
    print(arvore2.maximo())  # sem nodo partida(raiz)
    print(arvore2.minimo())  # sem nodo partida(raiz)
    print(verifica_igualdade(arvore.raiz,arvore2.raiz))


testeArvore()
