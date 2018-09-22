import random

#toooop

nome=input("NickName: ")
cartas=['Aa','Ab','Ac','Ad','2a','2b','2c','2d','3a','3b','3c','3d','4a','4b','4c','4d','5a','5b','5c','5d','6a','6b','6c','6d','7a','7b','7c','7d','8a','8b','8c','8d','9a','9b','9c','9d','10a','10b','10c','10d','Ja','Jb','Jc','Jd','Qa','Qb','Qc','Qd','Ka','Kb','Kc','Kd']


def placarMaquina(v):
    #inicio do print de placar da maquina
    tex="Máquina cards:. "
    t=''
    soma=0
    for i in range(len(v)):
        soma=soma+v[i]
        t=t+str(v[i])+", "
    print(tex+t+" PTs: "+str(soma))
    return soma


def placarJogador(v):
    #inicio do print de placar da maquina
    tex="Jogador cards:. "
    t=''
    soma=0
    for i in range(len(v)):
        soma=soma+v[i]
        t=t+str(v[i])+", "
    print(tex+t+" PTs: "+str(soma))
    return soma


def Trata(cartasMaquina):
    vet=[]
    #vetP=[]
    for i in range(len(cartasMaquina)):
        carM=0
        if cartasMaquina[i][0] == 'A':
            carM = 11
        elif cartasMaquina[i][0] == 'J' or cartasMaquina[i][0] == 'Q' or cartasMaquina[i][0] == 'K':
            carM = 10
        else:
            carM = int(cartasMaquina[i][0])
        vet.append(carM)
    return vet

def maquinaPensa(): #inteligencia não artificial aleatoria kk by:igor
    vet=[13,14,15,16,17,18,19]
    pensou=random.choice(vet)
    return pensou

def embaralhar(c):
    random.shuffle(c)

def distribuiCartas():
    aleatorio1 = random.choice(cartas)
    cartas.remove(aleatorio1)
    return aleatorio1


def jogar():
    cartasMaquina=[]
    cartasJogador=[]
    valorJogador = 0
    valorMaquina = 0

    #inicio do jogo
    embaralhar(cartas)
    cartasMaquina.append(distribuiCartas())
    cartasJogador.append(distribuiCartas())
    cartasMaquina.append(distribuiCartas())
    cartasJogador.append(distribuiCartas())

    maquina=Trata(cartasMaquina)
    #print(maquina)
    #print(cartasMaquina[1])
    jogador=Trata(cartasJogador)
    #print(jogador)

    valorMaquina=placarMaquina(maquina)
    valorJogador=placarJogador(jogador)

    perguntaPlayer=int(input("PARA PARAR (1)\nPARA DESCER CARTA (2) : "))

    while(perguntaPlayer != 1):
        cartasJogador.append(distribuiCartas())
        jogador=Trata(cartasJogador)
        valorJogador=placarJogador(jogador)
        perguntaPlayer = int(input("PARA PARAR (1)\nPARA DESCER CARTA (2) : "))


    # >>> VEZ DA MAQUINA JOGAR ;) <<<
    if valorJogador>21:
        print("Você perdeu!")
    else:#código de : igor ramos de oliveira..
        #maquina joga!@@@
        Qi=False
        while(Qi==False):
            if valorMaquina<maquinaPensa():
                cartasMaquina.append(distribuiCartas())
                maquina=Trata(cartasMaquina)
                valorMaquina=placarMaquina(maquina)
            else:
                Qi=True
        if valorMaquina==valorJogador:
            print("Você empatou!")
        elif valorMaquina>21:
            print("Você ganhou!")
        elif valorJogador>valorMaquina:
            print("Você ganhou!")
        else:
            print("Você perdeu, maquina ganhou!")

jogar()
#cartas=['Aa','Ab','Ac','Ad','2a','2b','2c','2d','3a','3b','3c','3d','4a','4b','4c','4d','5a','5b','5c','5d','6a','6b','6c','6d','7a','7b','7c','7d','8a','8b','8c','8d','9a','9b','9c','9d','10a','10b','10c','10d','Ja','Jb','Jc','Jd','Qa','Qb','Qc','Qd','Ka','Kb','Kc','Kd']
#tô muito feliz
#jogar()
