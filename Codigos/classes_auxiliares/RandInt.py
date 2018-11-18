import time


class RandInt:
    """Classe que gera numeros pseudo aleatorios"""
    def __init__(self):
        # CONSTANTES
        self.A = 17
        self.B = 13
        self.M = 21

    def numero_aleatorio(self, limite):
        """Metodo que gera um vetor de numeros pseudo aleatorios, usando congruências lineares,
         e seleciona 1 aleatoriamente e o retorna"""

        # cria vetor que receberá os valores gerados
        seq = []

        # Captura a parte inteira do timestamp corrente
        x0 = int(time.time())

        # Laço que preenche o vetor de números aleatorios
        for i in range(1000):
            # Formula das congruências lineares
            xi = ((self.A*x0)+self.B) % limite
            # Appenda o resultado de xi no vetor
            seq.append(xi)
            x0 = xi

        # Seleciona um item do vetor
        xi = ((self.A * x0) + self.B) % self.M
        Yi = 1 + (xi % len(seq))
        return seq[Yi]