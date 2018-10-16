import pygame, sys
# tentar implementar cor gradativa
from pygame.locals import *
pygame.init()
#mudança de teste bitbucket
#GNUS DIGITAIS> BRUNO, RODRIGO, MATHEUS E IGOR
verde = (0,100,0)
am = (255,255,0)
vermelho = (255,0,0)
preto = (0,0,0)
branco = (255,255,255)
tamanho = 43
fundo = pygame.image.load('imagens/megaStacker.png')
btnPare = pygame.image.load('imagens/spacebtn.png')
btnReinicia = pygame.image.load('imagens/reiniciarbtn.png')
largura = 900
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
somperdeu = pygame.mixer.Sound('sounds/perdeu.ogg')
musicafundo = pygame.mixer.Sound('sounds/musicafundo.ogg')
subirLinha = pygame.mixer.Sound('sounds/subir.wav')
sombotao = pygame.mixer.Sound('sounds/teste.wav')
sommoeda = pygame.mixer.Sound('sounds/moeda2.wav')
stop = True
moneyaposta = 0
moneycarteira = 250
def dinheiro():
    global moneycarteira, moneyaposta
    texto(str(moneycarteira), preto, 14, 715, 44)


def apostar(valor):
    texto(str(valor), preto, 14, 690, 318)

def perdeu(lista):
    print(lista)
    vago = lista[0]
    if any(Elemento != vago for Elemento in lista):
        tela.blit(perdeuimagem,(300,100))
        texto("Perdeu, aperte 'R' para reinciar!", branco, 30, 230, 5)
        musicafundo.stop()
        somperdeu.play()
    else:
        subirLinha.play()
def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont("Arial", tam,"bold")
    texto1 = font.render(msg, True, cor)
    tela.blit(texto1, [x, y])
    pygame.display.update()

def reiniciar():
    global moneyaposta
    moneyaposta = 0
    tela.fill(verde)
    tela.blit(fundo, (260, 40))
    tela.blit(btnReinicia, (320, 530))
    tela.blit(btnPare, (420, 530))
    tela.blit(carteira, (800, 15))
    tela.blit(saldoCarteira, (707, 39))
    tela.blit(aposta, (650, 250))
    tela.blit(cinco, (600, 500))
    tela.blit(dez, (660, 500))
    tela.blit(vinteCinco, (720, 500))
    tela.blit(cinquenta, (780, 500))
    tela.blit(cem, (840, 500))
    dinheiro()
    mat = [[280, 102], [329, 102], [378, 102], [427, 102], [476, 102], [280, 151], [329, 151], [378, 151], [427, 151], [476, 151], [280, 200], [329, 200], [378, 200], [427, 200], [476, 200], [280, 249], [329, 249], [378, 249], [427, 249], [476, 249], [280, 298], [329, 298], [378, 298], [427, 298], [476, 298], [280, 347], [329, 347], [378, 347], [427, 347], [476, 347], [280, 396], [329, 396], [378, 396], [427, 396], [476, 396], [280, 445], [329, 445], [378, 445], [427, 445], [476, 445]]
    amarelo(mat)
    musicafundo.play()
def amarelo(lista):
    global relogio
    relogio.tick(60)
    for i in range(len(lista)):
        pygame.draw.rect(tela, preto, [lista[i][0], lista[i][1], 46, 47])
    pygame.display.update()


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
    while stop:
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
                if xm > 420 and ym > 530 and xm < 575 and ym < 590:
                    v = True
                    stop = False
                    return vet, True
                elif xm > 600 and ym > 500 and xm < 655 and ym < 555:
                    sommoeda.play()
                    moneyaposta+=5
                    moneycarteira -= 5
                    tela.blit(saldoCarteira, (707, 39))
                    tela.blit(aposta, (650, 250))
                    dinheiro()
                    apostar(moneyaposta)
                elif xm > 660 and ym > 500 and xm < 715 and ym < 555:
                    sommoeda.play()
                    moneyaposta += 10
                    moneycarteira-= 10
                    tela.blit(saldoCarteira,(707, 39))
                    tela.blit(aposta, (650, 250))
                    dinheiro()
                    apostar(moneyaposta)
                elif xm > 720 and ym > 500 and xm < 775 and ym < 555:
                    sommoeda.play()
                    moneyaposta += 25
                    moneycarteira -= 25
                    tela.blit(saldoCarteira, (707, 39))
                    tela.blit(aposta, (650, 250))
                    dinheiro()
                    apostar(moneyaposta)
                elif xm > 780 and ym > 500 and xm < 835 and ym < 555:
                    sommoeda.play()
                    moneyaposta += 50
                    moneycarteira -= 50
                    tela.blit(saldoCarteira, (707, 39))
                    tela.blit(aposta, (650, 250))
                    dinheiro()
                    apostar(moneyaposta)
                elif xm > 840 and ym > 500 and xm < 895 and ym < 555:
                    sommoeda.play()
                    moneyaposta += 100
                    moneycarteira -= 100
                    tela.blit(saldoCarteira,(707, 39))
                    tela.blit(aposta, (650, 250))
                    dinheiro()
                    apostar(moneyaposta)


        if v:
            break
        else:

            if stop and len(vet) < 5:
                #quadrado(vet)
                atual = [xx, y]
                vet.append(atual)
                quadrado2(atual[0], atual[1])
                xx += 49
            else:
                amarelo(vet)
                vet.clear()
                xx = x


x = 280
y = 445
inicio = [280,444]
v = True
sair = True
lista = []
lista.append(inicio)
subir = False
subir2 = False
subir3 = False
subir4 = False
subir5 = False
subir6 = False
subir7 = False
subir8 = False



'''
pygame.draw.rect(tela, preto,[260, 530, 125, 40])
texto("Reiniciar(R)", branco, 22, 275, 535)
pygame.draw.rect(tela, preto,[415, 530, 125, 40])
texto("Parar(Espaço)", branco, 22, 420, 535)
'''
reiniciar()
juiz = [0]
while True:
    if sair:
        linha1, subir = linha(2, x, y)
        juiz[0] = len(linha1)
    if subir:
        subirLinha.play()
        linha2, subir2 = linha(4,x,396)
        juiz.append(len(linha2))
        perdeu(juiz)
    if subir2 and len(linha1) == len(linha2):
        linha3, subir3 = linha(6,x,347)
        juiz.append(len(linha3))
        perdeu(juiz)
    if subir3 and len(linha2) == len(linha3):
        linha4, subir4 = linha(8,x,298)
        juiz.append(len(linha4))
        perdeu(juiz)
    if subir4 and len(linha3) == len(linha4):
        linha5, subir5 = linha(10,x,249)
        juiz.append(len(linha5))
        perdeu(juiz)
    if subir5 and len(linha4) == len(linha5):
        linha6, subir6 = linha(12,x,200)
        juiz.append(len(linha6))
        perdeu(juiz)
    if subir6 and len(linha5) == len(linha6):
        linha7, subir7 = linha(14,x,151)
        juiz.append(len(linha7))
        perdeu(juiz)
    if subir7 and len(linha6) == len(linha7):
        linha8, subir8 = linha(20,x,102)
        juiz.append(len(linha8))
        perdeu(juiz)
    sair = True
    while sair:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    sombotao.play()
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
                    sair = False
                    reiniciar()
                    linha1, subir= linha(2,x,y)
                    juiz[0] = len(linha1)
            if evento.type == pygame.MOUSEBUTTONDOWN: #TODO - Criar função para todos os botões
                xm = pygame.mouse.get_pos()[0]
                ym = pygame.mouse.get_pos()[1]
                print(pygame.mouse.get_pos())
                if xm > 320 and ym > 530 and xm < 375 and ym < 590:
                    sombotao.play()
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
                    sair = False
                    reiniciar()
                    linha1, subir = linha(2, x, y)
                    juiz[0] = len(linha1)

        quadrado(linha1)


