import pygame, sys
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
largura = 900
altura = 600
tela = pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()

stop = True
def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont("Arial", tam)
    texto1 = font.render(msg, True, cor)
    tela.blit(texto1, [x, y])

def reiniciar():
    mat = [[280, 102], [329, 102], [378, 102], [427, 102], [476, 102], [280, 151], [329, 151], [378, 151], [427, 151], [476, 151], [280, 200], [329, 200], [378, 200], [427, 200], [476, 200], [280, 249], [329, 249], [378, 249], [427, 249], [476, 249], [280, 298], [329, 298], [378, 298], [427, 298], [476, 298], [280, 347], [329, 347], [378, 347], [427, 347], [476, 347], [280, 396], [329, 396], [378, 396], [427, 396], [476, 396], [280, 445], [329, 445], [378, 445], [427, 445], [476, 445]]
    amarelo(mat)

def amarelo(lista):
    global relogio
    relogio.tick(60)
    for i in range(len(lista)):
        pygame.draw.rect(tela, am, [lista[i][0], lista[i][1], 46, 47])
    pygame.display.update()


def quadrado(lista):
    print(lista)
    for xy in lista:
        pygame.draw.rect(tela, vermelho, [xy[0], xy[1], 46, 47])

def quadrado2(x,y):
    global stop
    if stop:
        pygame.draw.rect(tela, vermelho, [x, y, 46, 47])
        pygame.display.update()

def linha(velocidade,x,y):
    global stop
    frames = pygame.time.Clock()
    vet = []
    stop = True
    xx = x
    v = False
    print("Inicio")
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

        if v:
            break
        else:

            if stop and len(vet) < 5:
                #quadrado(vet)
                atual = [xx, y]
                vet.append(atual)
                quadrado2(atual[0], atual[1])
                xx += 49

                print('Entrou')

            else:
                print('Else')
                print(vet)
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
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("MegaStacker")
tela.fill(verde)
tela.blit(fundo, (260, 40))
pygame.draw.rect(tela, preto,[260, 530, 125, 40])
texto("Reiniciar(R)", branco, 22, 275, 535)
pygame.draw.rect(tela, preto,[415, 530, 125, 40])
texto("Parar(Espaço)", branco, 22, 420, 535)
reiniciar()

while True:
    if sair:
        linha1, subir = linha(2, x, y)
    if subir:
        linha2, subir2 = linha(4,x,396)
    if subir2 and len(linha1) == len(linha2):
        linha3, subir3 = linha(6,x,347)
    if subir3 and len(linha2) == len(linha3):
        linha4, subir4 = linha(8,x,298)
    if subir4 and len(linha3) == len(linha4):
        linha5, subir5 = linha(10,x,249)
    if subir5 and len(linha4) == len(linha5):
        linha6, subir6 = linha(12,x,200)
    if subir6 and len(linha5) == len(linha6):
        linha7, subir7 = linha(14,x,151)
    if subir7 and len(linha6) == len(linha7):
        linha8, subir8 = linha(16,x,102)
    sair = True
    while sair:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
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
                    sair = False
                    reiniciar()
                    linha1, subir= linha(2,x,y)
            if evento.type == pygame.MOUSEBUTTONDOWN: #TODO - Criar função para todos os botões
                pass

        print(linha1,'linha1')

        quadrado(linha1)
