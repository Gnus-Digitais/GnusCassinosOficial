import pygame, sys, time
from tkinter import *
from pygame.locals import *
from Codigos.classes_auxiliares.Ranking import Raking

class TelaMegaStacker:
    def __init__(self):
        pygame.init()

        # GNUS DIGITAIS> BRUNO, RODRIGO, MATHEUS E IGOR
        # Cores
        self.verde = (0, 100, 0)
        self.am = (255, 255, 0)
        self.vermelho = (255, 0, 0)
        self.preto = (0, 0, 0)
        self.branco = (255, 255, 255)
        self.corrank = (200, 171, 55)
        #definiçaõ de largura e altura da janela
        self.largura = 910
        self.altura = 600
        #definição da tela
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("MegaStacker")
        pygame.display.set_icon(pygame.image.load("imagens/logoSistema.ico"))
        #definição do relógico FPS
        self.relogio = pygame.time.Clock()
        #carregar as imagens do jogo
        self.fundo = pygame.image.load('imagens/megaStacker.png')
        self.btnPare = pygame.image.load('imagens/spacebtn.png')
        self.btnReinicia = pygame.image.load('imagens/restart2.png')
        self.imgWin = pygame.image.load('imagens/ganhou2.png')
        self.carteira = pygame.image.load('imagens/carteira2.png')
        self.saldoCarteira = pygame.image.load("imagens/qtdcarteira.png")
        self.soma = pygame.image.load('imagens/SOMA.png')
        self.aposta = pygame.image.load('imagens/aposta3.png')
        self.cinco = pygame.image.load('imagens/cinco.png')
        self.dez = pygame.image.load('imagens/dez.png')
        self.vinteCinco = pygame.image.load('imagens/vintecinco.png')
        self.cinquenta = pygame.image.load('imagens/cinquenta.png')
        self.cem = pygame.image.load('imagens/cem.png')
        self.perdeuimagem = pygame.image.load('imagens/perdeu1.png')
        self.btnOk = pygame.image.load('imagens/btnOk.png')
        self.headrank = pygame.image.load('imagens/quadroRanking.png')
        #carregar os sons do jogo
        self.somperdeu = pygame.mixer.Sound('sounds/perdeu.ogg')
        self.somwin = pygame.mixer.Sound('sounds/ganhou .ogg')
        self.musicafundo = pygame.mixer.Sound('sounds/musicafundo.ogg')
        self.subirLinha = pygame.mixer.Sound('sounds/subir.wav')
        self.sombotao = pygame.mixer.Sound('sounds/teste.wav')
        self.sommoeda = pygame.mixer.Sound('sounds/moeda2.wav')

        # Something
        self.stop = True
        self.moneyaposta = 0
        self.moneycarteira = 250
        self.rank = Raking("megastacker", "f")
        self.exibirRank = self.rank.retorna_ranking()
        self.teste = 0
        self.x = 280
        self.y = 445
        self.v = True
        self.sair = True
        self.subir = False
        self.subir2 = False
        self.subir3 = False
        self.subir4 = False
        self.subir5 = False
        self.subir6 = False
        self.subir7 = False
        self.subir8 = False
        self.reiniciar()
        self.juiz = [0]
        self.inicio(self.btnOk)

    def amarelo(self, lista):
        self.relogio.tick(60)
        for i in range(len(lista)):
            pygame.draw.rect(self.tela, self.preto, [lista[i][0], lista[i][1], 46, 47])
        pygame.display.update()

    def texto(self, msg, cor, tam, x, y):
        font = pygame.font.SysFont("Arial", tam, "bold")
        texto1 = font.render(msg, True, cor)
        self.tela.blit(texto1, [x, y])
        pygame.display.update()

    def dinheiro(self):
        self.texto(str(self.moneycarteira),self.preto, 14, 715, 44)

    def reiniciar(self):

        self.moneyaposta = 0
        self.tela.fill(self.verde)
        self.tela.blit(self.fundo, (260, 40))
        self.tela.blit(self.btnPare, (373, 530))
        self.tela.blit(self.carteira, (800, 15))
        self.tela.blit(self.saldoCarteira, (707, 39))
        self.tela.blit(self.aposta, (657, 340))
        self.tela.blit(self.cinco, (600, 500))
        self.tela.blit(self.dez, (660, 500))
        self.tela.blit(self.vinteCinco, (720, 500))
        self.tela.blit(self.cinquenta, (780, 500))
        self.tela.blit(self.cem, (840, 500))
        self.dinheiro()
        mat = [[280, 102], [329, 102], [378, 102], [427, 102], [476, 102], [280, 151], [329, 151], [378, 151],
               [427, 151], [476, 151], [280, 200], [329, 200], [378, 200], [427, 200], [476, 200], [280, 249],
               [329, 249], [378, 249], [427, 249], [476, 249], [280, 298], [329, 298], [378, 298], [427, 298],
               [476, 298], [280, 347], [329, 347], [378, 347], [427, 347], [476, 347], [280, 396], [329, 396],
               [378, 396], [427, 396], [476, 396], [280, 445], [329, 445], [378, 445], [427, 445], [476, 445]]
        self.amarelo(mat)

    def showmensage(self, msg):
        pygame.draw.rect(self.tela, self.corrank, [690, 440, 150, 20])
        pygame.display.update()
        self.texto(msg, self.preto, 15, 690, 440)
        time.sleep(1)
        pygame.draw.rect(self.tela, self.verde, [690, 440, 150, 20])
        pygame.display.update()

    def rank2(self, palavra):
        vet = palavra.split('\n')
        y = 50
        for x in vet:
            saida = x.split('\t')
            self.texto(saida[0], self.preto, 15, 40, y)
            self.texto(saida[1], self.preto, 15, 90, y)
            y += 15



    def variaveis(self):
        self.subir = False
        self.subir2 = False
        self.subir3 = False
        self.subir4 = False
        self.subir5 = False
        self.subir6 = False
        self.subir7 = False
        self.subir8 = False
        self.linha1 = []
        self.linha2 = []
        self.linha3 = []
        self.linha4 = []
        self.linha5 = []
        self.linha6 = []
        self.linha7 = []
        self.linha8 = []
        self.juiz = [0]
        self.sair = True

    def inicio(self, botao):
        self.tela.blit(botao, (575, 375))
        pygame.draw.rect(self.tela, self.corrank, [35, 43, 130, 270])
        # texto(exibirRank,preto,15,40,50)
        self.rank2(self.exibirRank)
        self.tela.blit(self.headrank, (25, 10))
        pygame.display.update()
        while self.sair:
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.MOUSEBUTTONDOWN:  # TODO - Criar função para todos os botões
                    xm = pygame.mouse.get_pos()[0]
                    ym = pygame.mouse.get_pos()[1]
                    print(pygame.mouse.get_pos())

                    if xm > 600 and ym > 500 and xm < 655 and ym < 555 and botao == self.btnOk:
                        if self.moneycarteira >= 5:
                            self.sommoeda.play()
                            self.moneyaposta += 5
                            self.moneycarteira -= 5
                            self.tela.blit(self.saldoCarteira, (707, 39))
                            self.tela.blit(self.aposta, (657, 340))
                            self.dinheiro()
                            self.apostar(self.moneyaposta)
                        else:
                            self.showmensage('Saldo insuficiente!')
                    elif xm > 660 and ym > 500 and xm < 715 and ym < 555 and botao == self.btnOk:
                        if self.moneycarteira >= 10:
                            self.sommoeda.play()
                            self.moneyaposta += 10
                            self.moneycarteira -= 10
                            self.tela.blit(self.saldoCarteira, (707, 39))
                            self.tela.blit(self.aposta, (657, 340))
                            self.dinheiro()
                            self.apostar(self.moneyaposta)
                        else:
                            self.showmensage('Saldo insuficiente!')
                    elif xm > 720 and ym > 500 and xm < 775 and ym < 555 and botao == self.btnOk:
                        if self.moneycarteira >= 25:
                            self.sommoeda.play()
                            self.moneyaposta += 25
                            self.moneycarteira -= 25
                            self.tela.blit(self.saldoCarteira, (707, 39))
                            self.tela.blit(self.aposta, (657, 340))
                            self.dinheiro()
                            self.apostar(self.moneyaposta)
                        else:
                            self.showmensage('Saldo insuficiente!')
                    elif xm > 780 and ym > 500 and xm < 835 and ym < 555 and botao == btnOk:
                        if self.moneycarteira >= 50:
                            self.sommoeda.play()
                            self.moneyaposta += 50
                            self.moneycarteira -= 50
                            self.tela.blit(self.saldoCarteira, (707, 39))
                            self.tela.blit(self.aposta, (657, 340))
                            self.dinheiro()
                            self.apostar(self.mself.oneyaposta)
                        else:
                            self.showmensage('Saldo insuficiente!')
                    elif xm > 840 and ym > 500 and xm < 895 and ym < 555 and botao == self.btnOk:
                        if self.moneycarteira >= 100:
                            self.sommoeda.play()
                            self.moneyaposta += 100
                            self.self.moneycarteira -= 100
                            self.tela.blit(self.saldoCarteira, (707, 39))
                            self.tela.blit(self.aposta, (657, 340))
                            self.dinheiro()
                            self.apostar(self.moneyaposta)
                        else:
                            self.showmensage('Saldo insuficiente!')
                    elif xm > 575 and ym > 375 and xm < 635 and ym < 435:
                        if self.moneyaposta > 0 and self.teste != 1:
                            self.play(True)
                        else:
                            if botao == self.btnOk:  # TODO Bug dedo nervoso
                                self.showmensage('Efetue uma aposta!')

                            self.play(False)
                        if self.teste > 0:
                            teste = 0
                            self.variaveis()
                            self.reiniciar()
                            self.inicio(self.btnOk)

    def play(self, bool):
        while bool:
            self.musicafundo.play()
            if self.sair:
                linha1, self.subir = self.linha(2, self.x, self.y)
                self.juiz[0] = len(linha1)
            if self.subir:
                if len(self.linha1) == 0:
                    self.loser = [1, 2]
                    self.perdeu(self.loser)
                else:
                    self.subirLinha.play()
                    linha2, subir2 = self.linha(4, self.x, 396)
                    self.juiz.append(len(self.linha2))
                self.perdeu(self.juiz)
            if self.subir2 and len(self.linha1) == len(self.linha2):
                self.linha3, self.subir3 = self.linha(6, self.x, 347)
                self.juiz.append(len(self.linha3))
                self.perdeu(self.juiz)
            if self.subir3 and len(self.linha2) == len(self.linha3):
                self.linha4, self.subir4 = self.linha(8, self.x, 298)
                self.juiz.append(len(self.linha4))
                self.perdeu(self.juiz)
            if self.subir4 and len(self.linha3) == len(self.linha4):
                self.linha5, self.subir5 = self.linha(10, self.x, 249)
                self.juiz.append(len(self.linha5))
                self.perdeu(self.juiz)
            if self.subir5 and len(self.linha4) == len(self.linha5):
                self.linha6, self.subir6 = self.linha(12, self.x, 200)
                self.juiz.append(len(self.linha6))
                self.perdeu(self.juiz)
            if self.subir6 and len(self.linha5) == len(self.linha6):
                self.linha7, self.subir7 = self.linha(14, self.x, 151)
                self.juiz.append(len(self.linha7))
                self.perdeu(self.juiz)
            if self.subir7 and len(self.linha6) == len(self.linha7):
                self.linha8, self.subir8 = self.linha(20, self.x, 102)
                self.juiz.append(len(self.linha8))
                self.perdeu(self.juiz)

            if self.subir8 and len(self.linha7) == len(self.linha8):
                self.juiz.append(len(self.linha8))
                self.ganhou()
        self.moneyaposta = 0

    def apostar(self, valor):
        self.texto(str(valor), self.preto, 14, 700, 415)

    def perdeu(self, lista):
        print(lista)
        self.vago = lista[0]
        if any(Elemento != self.vago for Elemento in lista):
            self.tela.blit(self.perdeuimagem, (300, 100))
            self.musicafundo.stop()
            self.somperdeu.play()
            self.moneyaposta = 0
            teste = 1
            print(teste)
            self.play(False)
            self.inicio(self.btnReinicia)
        else:
            self.subirLinha.play()

    def ganhou(self):
        self.tela.blit(self.imgWin, (300, 100))
        pygame.display.update()
        self.musicafundo.stop()
        self.somwin.play()
        self.moneycarteira += self.moneyaposta * 10
        self.moneyaposta = 0
        self.teste = 1
        self.play(False)
        self.inicio(self.btnReinicia)

    def quadrado(self, lista):
        for xy in lista:
            pygame.draw.rect(self.tela, self.vermelho, [xy[0], xy[1], 46, 47])

    def quadrado2(self, x, y):
        if self.stop:
            pygame.draw.rect(self.tela, self.vermelho, [x, y, 46, 47])
            pygame.display.update()

    def linha(self, velocidade, x, y):
        self.frames = pygame.time.Clock()
        self.vet = []
        self.stop = True
        self.xx = x
        self.v = False
        while self.stop and self.moneyaposta > 0:
            self.frames.tick(velocidade)
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        v = True
                        stop = False
                        return self.vet, True
                if evento.type == pygame.MOUSEBUTTONDOWN:  # TODO - Criar função para todos os botões
                    xm = pygame.mouse.get_pos()[0]
                    ym = pygame.mouse.get_pos()[1]
                    print(pygame.mouse.get_pos())
                    if xm > 373 and ym > 530 and xm < 428 and ym < 590:
                        v = True
                        stop = False
                        return self.vet, True

            if self.v:
                break
            else:

                if self.stop and len(self.vet) < 5:
                    self.atual = [self.xx, y]
                    self.vet.append(self.atual)
                    self.quadrado2(self.atual[0], self.atual[1])
                    self.xx += 49
                else:
                    self.amarelo(self.vet)
                    self.vet.clear()
                    self.xx = x


jogo = TelaMegaStacker()