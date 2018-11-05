import pygame, sys, time
from tkinter import messagebox
# tentar implementar cor gradativa
from pygame.locals import *

from Codigos.classes_auxiliares.Ranking import Raking
pygame.init()
#mudança de teste bitbucket
#GNUS DIGITAIS> BRUNO, RODRIGO, MATHEUS E IGOR
verde = (0,100,0)
am = (255,255,0)
vermelho = (255,0,0)
preto = (0,0,0)
branco = (255,255,255)
corrank = (200, 171, 55)
tamanho = 43
fundo = pygame.image.load('imagens/megaStacker.png')
btnPare = pygame.image.load('imagens/spacebtn.png')
btnReinicia = pygame.image.load('imagens/restart2.png')
imgWin = pygame.image.load('imagens/ganhou2.png')
largura = 910
altura = 600
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("MegaStacker")
pygame.display.set_icon(pygame.image.load("imagens/logoSistema.ico"))
relogio = pygame.time.Clock()
carteira = pygame.image.load('imagens/carteira2.png')
saldoCarteira = pygame.image.load("imagens/qtdcarteira.png")
soma = pygame.image.load('imagens/SOMA.png')
aposta = pygame.image.load('imagens/aposta3.png')
cinco = pygame.image.load('imagens/cinco.png')
dez = pygame.image.load('imagens/dez.png')
vinteCinco = pygame.image.load('imagens/vintecinco.png')
cinquenta = pygame.image.load('imagens/cinquenta.png')
cem = pygame.image.load('imagens/cem.png')
perdeuimagem = pygame.image.load('imagens/perdeu1.png')
btnOk = pygame.image.load('imagens/btnOk.png')
headrank = pygame.image.load('imagens/quadroRanking.png')
somperdeu = pygame.mixer.Sound('sounds/perdeu.ogg')
somwin = pygame.mixer.Sound('sounds/ganhou .ogg')
musicafundo = pygame.mixer.Sound('sounds/musicafundo.ogg')
subirLinha = pygame.mixer.Sound('sounds/subir.wav')
sombotao = pygame.mixer.Sound('sounds/teste.wav')
sommoeda = pygame.mixer.Sound('sounds/moeda2.wav')
stop = True
moneyaposta = 0
moneycarteira = 250
rank = Raking("megastacker","f")
exibirRank = rank.retorna_ranking()


def amarelo(lista):
    global relogio
    relogio.tick(60)
    for i in range(len(lista)):
        pygame.draw.rect(tela, preto, [lista[i][0], lista[i][1], 46, 47])
    pygame.display.update()

def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont("Arial", tam,"bold")
    texto1 = font.render(msg, True, cor)
    tela.blit(texto1, [x, y])
    pygame.display.update()

def dinheiro():
    global moneycarteira, moneyaposta
    texto(str(moneycarteira), preto, 14, 715, 44)

def reiniciar():
    global moneyaposta, moneycarteira
    moneyaposta = 0
    tela.fill(verde)
    tela.blit(fundo, (260, 40))
    tela.blit(btnPare, (373, 530))
    tela.blit(carteira, (800, 15))
    tela.blit(saldoCarteira, (707, 39))
    tela.blit(aposta, (657, 340))
    tela.blit(cinco, (600, 500))
    tela.blit(dez, (660, 500))
    tela.blit(vinteCinco, (720, 500))
    tela.blit(cinquenta, (780, 500))
    tela.blit(cem, (840, 500))
    dinheiro()
    mat = [[280, 102], [329, 102], [378, 102], [427, 102], [476, 102], [280, 151], [329, 151], [378, 151], [427, 151], [476, 151], [280, 200], [329, 200], [378, 200], [427, 200], [476, 200], [280, 249], [329, 249], [378, 249], [427, 249], [476, 249], [280, 298], [329, 298], [378, 298], [427, 298], [476, 298], [280, 347], [329, 347], [378, 347], [427, 347], [476, 347], [280, 396], [329, 396], [378, 396], [427, 396], [476, 396], [280, 445], [329, 445], [378, 445], [427, 445], [476, 445]]
    amarelo(mat)

def showmensage(msg):
    pygame.draw.rect(tela,corrank,[690,440,150,20])
    pygame.display.update()
    texto(msg, preto, 15, 690, 440)
    time.sleep(1)
    pygame.draw.rect(tela, verde, [690, 440, 150, 20])
    pygame.display.update()

def rank(palavra):
    vet = palavra.split('\n')
    y = 50
    for x in vet:
        saida = x.split('\t')
        texto(saida[0],preto,15,40,y)
        texto(saida[1],preto,15,90,y)
        y+=15

teste = 0
x = 280
y = 445
v = True
sair = True
subir = False
subir2 = False
subir3 = False
subir4 = False
subir5 = False
subir6 = False
subir7 = False
subir8 = False
reiniciar()
juiz = [0]
def variaveis():
    global subir,subir2,subir3,subir4,subir5,subir6,subir7,subir8
    global linha1,linha2,linha3,linha4,linha5,linha6,linha7,linha8,juiz,sair
    subir = False
    subir2 = False
    subir3 = False
    subir4 = False
    subir5 = False
    subir6 = False
    subir7 = False
    subir8 = False
    linha1 = []
    linha2 = []
    linha3 = []
    linha4 = []
    linha5 = []
    linha6 = []
    linha7 = []
    linha8 = []
    juiz = [0]
    sair = True
def inicio(botao):
    global subir, subir2, subir3, subir4, subir5, subir6, subir7, subir8
    global linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, juiz, sair
    global moneyaposta, moneycarteira,teste
    tela.blit(botao,(575,375))
    pygame.draw.rect(tela, corrank, [35, 43, 130, 270])
    #texto(exibirRank,preto,15,40,50)
    rank(exibirRank)
    tela.blit(headrank,(25,10))
    pygame.display.update()
    while sair:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN: #TODO - Criar função para todos os botões
                xm = pygame.mouse.get_pos()[0]
                ym = pygame.mouse.get_pos()[1]
                print(pygame.mouse.get_pos())

                if xm > 600 and ym > 500 and xm < 655 and ym < 555 and botao == btnOk:
                    if moneycarteira >= 5:
                        sommoeda.play()
                        moneyaposta += 5
                        moneycarteira -= 5
                        tela.blit(saldoCarteira, (707, 39))
                        tela.blit(aposta, (657, 340))
                        dinheiro()
                        apostar(moneyaposta)
                    else:
                        showmensage('Saldo insuficiente!')
                elif xm > 660 and ym > 500 and xm < 715 and ym < 555 and botao == btnOk:
                    if moneycarteira >= 10:
                        sommoeda.play()
                        moneyaposta += 10
                        moneycarteira -= 10
                        tela.blit(saldoCarteira, (707, 39))
                        tela.blit(aposta, (657, 340))
                        dinheiro()
                        apostar(moneyaposta)
                    else:
                        showmensage('Saldo insuficiente!')
                elif xm > 720 and ym > 500 and xm < 775 and ym < 555 and botao == btnOk:
                    if moneycarteira >= 25:
                        sommoeda.play()
                        moneyaposta += 25
                        moneycarteira -= 25
                        tela.blit(saldoCarteira, (707, 39))
                        tela.blit(aposta, (657, 340))
                        dinheiro()
                        apostar(moneyaposta)
                    else:
                        showmensage('Saldo insuficiente!')
                elif xm > 780 and ym > 500 and xm < 835 and ym < 555 and botao == btnOk:
                    if moneycarteira >= 50:
                        sommoeda.play()
                        moneyaposta += 50
                        moneycarteira -= 50
                        tela.blit(saldoCarteira, (707, 39))
                        tela.blit(aposta, (657, 340))
                        dinheiro()
                        apostar(moneyaposta)
                    else:
                        showmensage('Saldo insuficiente!')
                elif xm > 840 and ym > 500 and xm < 895 and ym < 555 and botao == btnOk:
                    if moneycarteira >= 100:
                        sommoeda.play()
                        moneyaposta += 100
                        moneycarteira -= 100
                        tela.blit(saldoCarteira, (707, 39))
                        tela.blit(aposta, (657, 340))
                        dinheiro()
                        apostar(moneyaposta)
                    else:
                        showmensage('Saldo insuficiente!')
                elif xm > 575 and ym > 375 and xm < 635 and ym < 435:
                    if moneyaposta > 0 and teste != 1:
                        play(True)
                    else:
                        if botao == btnOk: #TODO Bug dedo nervoso
                            showmensage('Efetue uma aposta!')

                        play(False)
                    if teste > 0:
                        teste = 0
                        variaveis()
                        reiniciar()
                        inicio(btnOk)

def play(bool):
    global subir, subir2, subir3, subir4, subir5, subir6, subir7, subir8,moneyaposta
    global linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, juiz, sair

    while bool:
        musicafundo.play()
        if sair:
            linha1, subir = linha(2, x, y)
            juiz[0] = len(linha1)
        if subir:
            if len(linha1) == 0:
                loser = [1, 2]
                perdeu(loser)
            else:
                subirLinha.play()
                linha2, subir2 = linha(4, x, 396)
                juiz.append(len(linha2))
            perdeu(juiz)
        if subir2 and len(linha1) == len(linha2):
            linha3, subir3 = linha(6, x, 347)
            juiz.append(len(linha3))
            perdeu(juiz)
        if subir3 and len(linha2) == len(linha3):
            linha4, subir4 = linha(8, x, 298)
            juiz.append(len(linha4))
            perdeu(juiz)
        if subir4 and len(linha3) == len(linha4):
            linha5, subir5 = linha(10, x, 249)
            juiz.append(len(linha5))
            perdeu(juiz)
        if subir5 and len(linha4) == len(linha5):
            linha6, subir6 = linha(12, x, 200)
            juiz.append(len(linha6))
            perdeu(juiz)
        if subir6 and len(linha5) == len(linha6):
            linha7, subir7 = linha(14, x, 151)
            juiz.append(len(linha7))
            perdeu(juiz)
        if subir7 and len(linha6) == len(linha7):
            linha8, subir8 = linha(10, x, 102)
            juiz.append(len(linha8))
            perdeu(juiz)

        if subir8 and len(linha7) == len(linha8):
            juiz.append(len(linha8))
            ganhou()
    moneyaposta = 0

def apostar(valor):
    texto(str(valor), preto, 14, 700, 415)

def perdeu(lista):
    global teste, moneyaposta
    print(lista)
    vago = lista[0]
    if any(Elemento != vago for Elemento in lista):
        tela.blit(perdeuimagem,(300,100))
        musicafundo.stop()
        somperdeu.play()
        moneyaposta = 0
        teste = 1
        print(teste)
        play(False)
        inicio(btnReinicia)
    else:
        subirLinha.play()

def ganhou():
    global moneyaposta, moneycarteira,teste
    tela.blit(imgWin, (300, 100))
    pygame.display.update()
    musicafundo.stop()
    somwin.play()
    moneycarteira+=moneyaposta*10
    moneyaposta = 0
    teste = 1
    play(False)
    inicio(btnReinicia)

def quadrado(lista):
    for xy in lista:
        pygame.draw.rect(tela, vermelho, [xy[0], xy[1], 46, 47])

def quadrado2(x,y):
    global stop
    if stop:
        pygame.draw.rect(tela, vermelho, [x, y, 46, 47])
        pygame.display.update()

def linha(velocidade,x,y):
    global stop,juiz,moneyaposta,moneycarteira
    frames = pygame.time.Clock()
    vet = []
    stop = True
    xx = x
    v = False
    while stop and moneyaposta > 0:
        frames.tick(velocidade)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    v = True
                    stop = False
                    return vet, True
            if evento.type == pygame.MOUSEBUTTONDOWN: #TODO - Criar função para todos os botões
                xm = pygame.mouse.get_pos()[0]
                ym = pygame.mouse.get_pos()[1]
                print(pygame.mouse.get_pos())
                if xm > 373 and ym > 530 and xm < 428 and ym < 590:
                    v = True
                    stop = False
                    return vet, True

        if v:
            break
        else:

            if stop and len(vet) < 5:
                atual = [xx, y]
                vet.append(atual)
                quadrado2(atual[0], atual[1])
                xx += 49
            else:
                amarelo(vet)
                vet.clear()
                xx = x

inicio(btnOk)


