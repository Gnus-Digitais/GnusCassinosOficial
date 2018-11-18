import pygame, sys, time
from tkinter import *
from tkinter import messagebox
from pygame.locals import *
from Codigos.classes_auxiliares.Ranking import Ranking
#from Codigos.tela_principal.Jogo import Jogo
import os

class TelaMegaStacker:
    def __init__(self,user,janela):
        self.janela=janela
        self.x_telaPrincipal = (self.janela.winfo_screenwidth() // 2) - (910 // 2)
        self.y_telaPrincipal = (self.janela.winfo_screenheight() // 2) - (600 // 2)
        self.janela.geometry("0x0+{}+{}".format(0, 0))  # largura x altura + esquerda + topo
        self.janela.overrideredirect(True)  # retira bordas
        self.__user = user
        #command para centralizar a tela
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()

        # GNUS DIGITAIS> BRUNO, RODRIGO, MATHEUS E IGOR
        # Cores
        self.azul = (0,0,128)
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
        pygame.display.set_icon(pygame.image.load("imagem/icone2.png"))
        #definição do relógico FPS
        self.relogio = pygame.time.Clock()
        #carregar as imagens do jogo
        self.fundo = pygame.image.load('../MegaStacker/imagens/megaStacker.png')
        self.btnPare = pygame.image.load('../MegaStacker/imagens/spacebtn.png')
        self.btnReinicia = pygame.image.load('../MegaStacker/imagens/restart2.png')
        self.imgWin = pygame.image.load('../MegaStacker/imagens/ganhou2.png')
        self.carteira = pygame.image.load('../MegaStacker/imagens/carteira2.png')
        self.saldoCarteira = pygame.image.load("../MegaStacker/imagens/qtdcarteira.png")
        self.soma = pygame.image.load('../MegaStacker/imagens/SOMA.png')
        self.aposta = pygame.image.load('../MegaStacker/imagens/aposta3.png')
        self.cinco = pygame.image.load('../MegaStacker/imagens/cinco.png')
        self.dez = pygame.image.load('../MegaStacker/imagens/dez.png')
        self.vinteCinco = pygame.image.load('../MegaStacker/imagens/vintecinco.png')
        self.cinquenta = pygame.image.load('../MegaStacker/imagens/cinquenta.png')
        self.cem = pygame.image.load('../MegaStacker/imagens/cem.png')
        self.perdeuimagem = pygame.image.load('../MegaStacker/imagens/perdeu1.png')
        self.btnOk = pygame.image.load('../MegaStacker/imagens/btnOk.png')
        self.headrank = pygame.image.load('../MegaStacker/imagens/quadroRanking.png')
        self.btnRetornar = pygame.image.load('../MegaStacker/imagens/voltar2.png')
        self.btnHowToPlay = pygame.image.load('imagem/howtoplaybutton.png')
        self.howToPlay = pygame.image.load('imagem/howtoplaymegastacker.png')
        #carregar os sons do jogo
        self.somperdeu = pygame.mixer.Sound('../MegaStacker/sounds/perdeu.ogg')
        self.somwin = pygame.mixer.Sound('../MegaStacker/sounds/ganhou .ogg')
        self.musicafundo = pygame.mixer.Sound('../MegaStacker/sounds/musicafundo.ogg')
        self.subirLinha = pygame.mixer.Sound('../MegaStacker/sounds/subir.wav')
        self.sombotao = pygame.mixer.Sound('../MegaStacker/sounds/teste.wav')
        self.sommoeda = pygame.mixer.Sound('../MegaStacker/sounds/moeda2.wav')

        #Something
        self.stop = True
        self.moneyaposta = 0
        self.moneycarteira = 250
        self.rank = Ranking("megastacker", "f")

        self.teste = 0
        self.x = 280
        self.y = 445
        self.v = True
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
        self.controle_howtoplay = False
        self.juiz = [0]
        self.sair = True
        self.reiniciar()
        self.juiz = [0]
        self.inicio(self.btnOk)


    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, valor):
        self.__user = valor

    def desenha_varios_quadrados(self, lista):
        """Função para desenhar vários quadrados na tela
        a partir de uma lista que em canda posição contém uma
        coordeanda x e y"""
        self.relogio.tick(60)
        for i in range(len(lista)):
            pygame.draw.rect(self.tela, self.preto, [lista[i][0], lista[i][1], 46, 47])
        pygame.display.update()

    def texto(self, msg, cor, tam, x, y):
        font = pygame.font.SysFont("Arial", tam, "bold")
        texto1 = font.render(msg, True, cor)
        self.tela.blit(texto1, [x, y])
        pygame.display.update()


    def inserir_no_ranking(self, score):
        """este metodo adiciona o usuario do game ao ranking"""
        self.rank.addRecord(self.user, int(score))
    def dinheiro(self):
        self.texto(str(self.moneycarteira),self.preto, 16, 715, 44)

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
        self.tela.blit(self.btnRetornar,(2,530))
        self.tela.blit(self.btnHowToPlay,(2,465))
        self.dinheiro()
        mat = [[280, 102], [329, 102], [378, 102], [427, 102], [476, 102], [280, 151], [329, 151], [378, 151],
               [427, 151], [476, 151], [280, 200], [329, 200], [378, 200], [427, 200], [476, 200], [280, 249],
               [329, 249], [378, 249], [427, 249], [476, 249], [280, 298], [329, 298], [378, 298], [427, 298],
               [476, 298], [280, 347], [329, 347], [378, 347], [427, 347], [476, 347], [280, 396], [329, 396],
               [378, 396], [427, 396], [476, 396], [280, 445], [329, 445], [378, 445], [427, 445], [476, 445]]
        self.desenha_varios_quadrados(mat)

    def showmensage(self, msg,x,y):
        pygame.draw.rect(self.tela, self.vermelho, [x, y, 150, 20])
        pygame.display.update()
        self.texto(msg, self.branco, 16, x, y)
        self.ligado = True
        time.sleep(1)
        pygame.draw.rect(self.tela, self.verde, [x, y, 150, 20])
        pygame.display.update()

    def rank2(self, palavra):
        vet = palavra.split('\n')
        y = 50
        for x in vet:
            saida = x.split('\t')
            self.texto(saida[0], self.preto, 15, 40, y)
            self.texto(saida[1], self.preto, 15, 90, y)
            y += 17

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
        self.controle_howtoplay = False
    def inicio(self, botao):
        self.tela.blit(botao, (575, 375))
        pygame.draw.rect(self.tela, self.corrank, [35, 43, 130, 190])
        self.exibirRank = self.rank.retorna_ranking()
        self.rank2(self.exibirRank)
        self.tela.blit(self.headrank, (25, 10))
        pygame.display.update()
        while self.sair:
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    self.janela.destroy()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:  # TODO - Criar função para todos os botões
                    xm = pygame.mouse.get_pos()[0]
                    ym = pygame.mouse.get_pos()[1]

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
                            self.showmensage('Saldo insuficiente!',690,440)
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
                            self.showmensage('Saldo insuficiente!',690,440)
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
                            self.showmensage('Saldo insuficiente!',690,440)
                    elif xm > 780 and ym > 500 and xm < 835 and ym < 555 and botao == self.btnOk:
                        if self.moneycarteira >= 50:
                            self.sommoeda.play()
                            self.moneyaposta += 50
                            self.moneycarteira -= 50
                            self.tela.blit(self.saldoCarteira, (707, 39))
                            self.tela.blit(self.aposta, (657, 340))
                            self.dinheiro()
                            self.apostar(self.moneyaposta)
                        else:
                            self.showmensage('Saldo insuficiente!',690,440)
                    elif xm > 840 and ym > 500 and xm < 895 and ym < 555 and botao == self.btnOk:
                        if self.moneycarteira >= 100:
                            self.sommoeda.play()
                            self.moneyaposta += 100
                            self.moneycarteira -= 100
                            self.tela.blit(self.saldoCarteira, (707, 39))
                            self.tela.blit(self.aposta, (657, 340))
                            self.dinheiro()
                            self.apostar(self.moneyaposta)
                        else:
                            self.showmensage('Saldo insuficiente!',690,440)

                    #Botão howtoplay
                    elif xm > 2 and ym > 465 and xm < 62 and ym < 525:
                        self.tela.fill(self.azul)
                        self.tela.blit(self.howToPlay, (90, 20))
                        self.tela.blit(self.btnRetornar,(2,530))
                        pygame.display.update()
                        self.controle_howtoplay = True
                    #Botão retornar fora do howtoplay
                    elif xm > 2 and ym > 530 and xm < 62 and ym < 590 and self.controle_howtoplay == False:
                        self.janela.geometry("910x600+{}+{}".format(self.x_telaPrincipal, self.y_telaPrincipal))  # largura x altura + esquerda + topo
                        self.janela.overrideredirect(False)  # coloca bordas
                        self.teste = 1
                        self.sair = False
                        self.v = True
                        #self.play(True)
                        print('Qualquer coisa'+1)
                        break
                    #Botão retornar dentro do howtoplay
                    elif xm > 2 and ym > 530 and xm < 62 and ym < 590 and self.controle_howtoplay == True:
                        self.reiniciar()
                        self.variaveis()
                        self.inicio(self.btnOk)
                    #Botão Play
                    elif xm > 575 and ym > 375 and xm < 635 and ym < 435:
                        if self.moneyaposta > 0 and self.teste != 1:
                            pygame.draw.rect(self.tela, self.verde, [570, 370, 70, 70])
                            pygame.draw.rect(self.tela, self.verde, [590, 500, 310, 70])
                            self.play(True)
                        else:
                            if botao == self.btnOk:  # TODO Bug dedo nervoso
                                self.showmensage('Efetue uma aposta!',690,440)
                            self.play(False)
                        if self.teste > 0:
                            self.teste = 0
                            self.variaveis()
                            self.reiniciar()
                            self.inicio(self.btnOk)

    def play(self, bool):
        while bool:
            self.musicafundo.play()
            if self.sair:
                self.linha1, self.subir = self.linha(2, self.x, self.y)
                self.juiz[0] = len(self.linha1)
            if self.subir:
                if len(self.linha1) == 0:
                    self.loser = [1, 2]
                    self.perdeu(self.loser)
                else:
                    self.subirLinha.play()
                    self.linha2, self.subir2 = self.linha(4, self.x, 396)
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
        self.texto(str(valor), self.preto, 16, 700, 415)

    def perdeu(self, lista):
        self.vago = lista[0]
        if any(Elemento != self.vago for Elemento in lista):
            self.tela.blit(self.perdeuimagem, (300, 100))
            self.musicafundo.stop()
            self.somperdeu.play()
            self.moneyaposta = 0
            if self.moneycarteira <  1:
                Tk().withdraw()
                messagebox.showinfo("Que pena!", "Perdeu tudo!")
                self.janela.geometry("910x600+{}+{}".format(self.x_telaPrincipal, self.y_telaPrincipal))  # largura x altura + esquerda + topo
                self.janela.overrideredirect(False)#coloca bordas
                self.teste = 1
               #self.play(False)
                self.sair = False
                self.v = True
                #pygame.quit()


            self.teste = 1
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
        self.inserir_no_ranking(self.moneycarteira)
        self.moneyaposta = 0
        self.teste = 1
        self.play(False)
        self.inicio(self.btnReinicia)


    def desenha_quadrado(self, x, y):
        """Função para desenhar um quadrado na tela, a partir das
        coordenadas x e y"""
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
                    self.janela.destroy()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        self.v = True
                        self.stop = False
                        return self.vet, True
                if evento.type == pygame.MOUSEBUTTONDOWN:  # TODO - Criar função para todos os botões
                    xm = pygame.mouse.get_pos()[0]
                    ym = pygame.mouse.get_pos()[1]
                    if xm > 373 and ym > 530 and xm < 428 and ym < 590:
                        self.v = True
                        self.stop = False
                        return self.vet, True
                    elif xm > 15 and ym > 530 and xm < 75 and ym < 590:
                        self.showmensage('Finalize o jogo!',78,550)

            if self.v:
                break
            else:
                if self.stop and len(self.vet) < 5:
                    self.atual = [self.xx, y]
                    self.vet.append(self.atual)
                    self.desenha_quadrado(self.atual[0], self.atual[1])
                    self.xx += 49
                else:
                    self.desenha_varios_quadrados(self.vet)
                    self.vet.clear()
                    self.xx = x



