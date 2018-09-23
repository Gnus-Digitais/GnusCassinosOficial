import os
import random

class SlotMachine:
    def __init__(self):
        self.slot1 = None
        self.slot2 = None
        self.slot3 = None
        #self.imgs = ['arcanaine','corphish','electabuz','groundon','pikachu']
        self.imgs = ['ewert', 'kaio', 'mat', 'gnu']


    def spin(self):
        c = self.fisher_yates_shuffle(self.imgs)
        return random.choice(c)


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
'''
s = SlotMachine()
print(s.spin())
'''