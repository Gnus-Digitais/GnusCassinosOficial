from baralho import Baralho
from pygame  import mixer
from tkinter import *
from Codigos.classes_auxiliares.Ranking import Raking
from functools import partial

#TODO 1 - LEMBRAR DE ADICIONAR FUNÇÃO PARA APLICAÇÃO REINICIAR APÓS CARTEIRA IGUAL A 0.0()
#TODO 2 - LEMBRAR DE ADICIONAR FUNÇÕES PARA ATUALIZAR VALOR DO ARQUIVO DA CLASSE RANKING, CASO A PARTIDA TERMINE.
#TODO 3 - REVISAR O CÓDIGO TODO, E MUDAR AS FUNÇÕES PARA MÉTODOS DE UMA CLASSE JOGO21.
#TODO 4 - VERIFICAR QUANDO MAQUINA VENCE ANTES DO USUARIO FINALIZAR A JOGADA.

#fodasticamente by:grupomaisfodadoBrasil <"G'NUS DIGITAIS"> não ouse tocar nesta linha!>>risco de morte
#melhor team: "G'NUS DIGITAIS"> Matheus Dias, Bruno Felipe, Rodrigo Rocca e Igor Ramos(6998121-0671)..
def aposta_status(stat):
    if stat=="aberto":
        ficha5.place(x=597, y=520)
        ficha10.place(x=657, y=520)
        ficha25.place(x=717, y=520)
        ficha50.place(x=777, y=520)
        ficha100.place(x=837, y=520)
        aposta.place(x=657,y=345)
        btnOk.place(x=575, y=375)
        valor_aposta_lb.place(x=740, y=415)

    else:
        ficha5.place(x=1000, y=500)
        ficha10.place(x=1070, y=500)
        ficha25.place(x=1140, y=500)
        ficha50.place(x=1130, y=500)
        ficha100.place(x=1100, y=500)
        btnOk.place(x=1000,y=240)

def aposta_ficha(ficha):
    global saldo_carteira
    global valor_aposta
    if saldo_carteira-ficha>=0:
        if ficha==5:
            valor_aposta=valor_aposta+5
            saldo_carteira=saldo_carteira-5
            saldo_carteira_lb['text'] = "%.2f" % saldo_carteira
            valor_aposta_lb['text'] = "%.2f" % valor_aposta
        if ficha==10:
            valor_aposta = valor_aposta + 10
            saldo_carteira = saldo_carteira - 10
            saldo_carteira_lb['text'] = "%.2f" % saldo_carteira
            valor_aposta_lb['text'] = "%.2f" % valor_aposta
        if ficha==25:
            valor_aposta = valor_aposta + 25
            saldo_carteira = saldo_carteira - 25
            saldo_carteira_lb['text'] = "%.2f" % saldo_carteira
            valor_aposta_lb['text'] = "%.2f" % valor_aposta
        if ficha==50:
            valor_aposta = valor_aposta + 50
            saldo_carteira = saldo_carteira - 50
            saldo_carteira_lb['text'] = "%.2f" % saldo_carteira
            valor_aposta_lb['text'] = "%.2f" % valor_aposta
        if ficha==100:
            valor_aposta = valor_aposta + 100
            saldo_carteira = saldo_carteira - 100
            saldo_carteira_lb['text'] = "%.2f" % saldo_carteira
            valor_aposta_lb['text'] = "%.2f" % valor_aposta
    else:
        #não pode apostar !
        print("não deixa apostar essa quantia ! :( ")

def reiniciarCarteira():
    global saldo_carteira
    saldo_carteira=250.0
    valor_aposta_lb.place(x=1000, y=230)


def Ok():
    aposta_status("fechado")
    play()

def novaPartida():
    zeraLimpa()
    global valor_aposta
    valor_aposta = 00
    valor_aposta_lb['text'] = "%.2f" % valor_aposta
    aposta_status("aberto")
    reinicio['image']=""
    inicio['image']=""
    reinicio.place(x=0, y=0)
    inicio.place(x=0,y=0)

def estadoBtn(est):
    if est=="ativa":
        #print("ativou")
        btnDescer['image'] = imgbtnD
        btnParar['image'] = imgbtnP
        btnParar.place(x=550, y=500)
        btnDescer.place(x=615, y=500)
    else:
        #print("desativou")
        btnDescer['image']=''
        btnParar['image'] =''
        btnParar.place(x=0, y=0)
        btnDescer.place(x=0,y=0)

def tiralogo():
    logo['image'] = ''
    logo.place(x=0, y=0)

def zeraLimpa():
    zerarPartida()
    limpaMeio()
def desvira():
    global urlDesvira
    img2['file'] = urlDesvira
    imagem2.place(x=443, y=30)

def limpaMeio():
    imagemPer['image'] = imgPer
    medalha['image']=''
    perdeuimg['image']=''
    empateimg['image']=''
    lbMaquina['text'] = ''
    lbJogador['text'] = ''
    logo['image'] = imglogo
    logo.place(x=340, y=240)
    medalha.place(x=0, y=0)
    perdeuimg.place(x=0, y=0)
    empateimg.place(x=0,y=0)
    imagem.place(x=350, y=30)
    imagem2.place(x=443, y=30)
    imagem3.place(x=350, y=460)
    imagem4.place(x=443, y=460)
    img1['file']=r"image\cartasSlot.png"
    img2['file']=r"image\cartasSlot.png"
    img3['file']=r"image\cartasSlot.png"
    img4['file']=r"image\cartasSlot.png"
    imag1.place(x=1000, y=400)
    imag2.place(x=1000, y=400)
    imag3.place(x=1000, y=400)
    imag4.place(x=1000, y=400)
    imag5.place(x=1000, y=400)
    imag6.place(x=1000, y=450)
    imag7.place(x=1000, y=450)
    imag8.place(x=1000, y=450)
    imag9.place(x=1000, y=450)
    imag10.place(x=1000, y=450)
    resultadoTela("não")

def zerarPartida():
    global qtdCartasMaquina
    global qtdCartasJogador
    global valorJogador
    global valorMaquina
    global cartasMaquina
    global cartasJogador
    valorMaquina = 0
    valorJogador = 0
    bara.baralho=[]  #TODO olhar esta linha..(ps. ESTOU MODIFICANDO DIRETO NUM ATRIBUTO(get) DA CLASSE BARALHO)
    cartasJogador = []
    cartasMaquina = []
    print("Máquina cards:. " + str(cartasMaquina) + " Pts: " + str(valorMaquina))
    print("Jogador cards:. " + str(cartasJogador) + " Pts: " + str(valorJogador))
    qtdCartasJogador = 2
    qtdCartasMaquina = 2


def resultadoTela(s):
    if s == 'sim':
        lbResultadoMaquina.place(x=360, y=160)
        lbPontuacaoMaquina.place(x=472, y=168)
        lbResultadoJogador.place(x=360, y=410)
        lbPontuacaoJogador.place(x=472, y=418)
        lbResultadoMaquina['image']=pontoMaquina
        lbResultadoJogador['image']=pontoJogador
        lbPontuacaoMaquina['text'] = valorMaquina
        lbPontuacaoJogador['text'] = valorJogador

    else:
        lbPontuacaoMaquina['text'] = ""
        lbPontuacaoJogador['text'] = ""
        lbPontuacaoMaquina.place(x=1000,y=650)
        lbPontuacaoJogador.place(x=1000,y=650)
        lbResultadoJogador['image']=''
        lbResultadoMaquina['image']=''


def imprimir_ranking():
    global r
    return r.retorna_ranking()

def inserir_no_ranking(score):
    global r, carteira
    r.addRecord("testador", int(score))


def empatou():
    global saldo_carteira
    global valor_aposta
    saldo_carteira=saldo_carteira+valor_aposta
    saldo_carteira_lb['text'] = "%.2f" % saldo_carteira
    reinicio['image'] = reinicioimg
    reinicio.place(x=748, y=500)
    estadoBtn("desativa")
    mixer.init()
    mixer.music.load(r'sounds/uhoh.mp3')
    mixer.music.play()
    tiralogo()
    resultadoTela("sim")
    lbJogador['text']=''
    lbMaquina['text']=''
    logo['image'] = ''
    empateimg['image']=imgEmpate
    empateimg.place(x=330,y=220)
    logo.place(x=0, y=0)
    ranking['text'] = imprimir_ranking()
    ranking.place(x=25, y=43)

def ganhou():
    global saldo_carteira
    global valor_aposta
    saldo_carteira = saldo_carteira + (valor_aposta*3)
    saldo_carteira_lb['text'] = "%.2f" % saldo_carteira
    reinicio['image'] = reinicioimg
    reinicio.place(x=748, y=500)
    estadoBtn("desativa")
    #musica ganhou
    mixer.init()
    mixer.music.load(r'sounds/ganhou.mp3')
    mixer.music.play()
    tiralogo()
    resultadoTela("sim")
    lbJogador['text'] = ''
    lbMaquina['text'] = ''
    logo['image'] = ''
    medalha['image']=imgMedalha
    medalha.place(x=330, y=220)
    logo.place(x=0,y=0)
    inserir_no_ranking(saldo_carteira)
    ranking['text'] = imprimir_ranking()
    ranking.place(x=25, y=43)


def perdeu():
    global saldo_carteira
    saldo_carteira_lb['text'] = "%.2f" % saldo_carteira
    reinicio['image'] = reinicioimg
    reinicio.place(x=748, y=500)
    #musica perdeu
    estadoBtn("desativa")
    mixer.init()
    mixer.music.load(r'sounds/uhoh.mp3')
    mixer.music.play()
    tiralogo()
    resultadoTela("sim")
    lbJogador['text'] = ''
    lbMaquina['text'] = ''
    logo['image'] = ''
    perdeuimg['image'] = imgPerdeu
    perdeuimg.place(x=330, y=220)
    logo.place(x=0, y=0)
    ranking['text'] = imprimir_ranking()
    ranking.place(x=25, y=43)

def play():
    ranking['text']=imprimir_ranking()
    ranking.place(x=25, y=43)
    rank['image'] = imgrank
    zeraLimpa()
    jogar()
    estadoBtn("ativa")
    inicio['image']=''
    logo['image']=imglogo
    medalha['image']=''
    medalha.place(x=0,y=0)
    perdeuimg['image']=''
    perdeuimg.place(x=0,y=0)
    inicio.place(x=0,y=0)
    logo.place(x=340, y=240)
    #AtualizaPlay()
    reinicio.place(x=748, y=500)

def EmbaralharSom():
    mixer.init()
    mixer.music.load(r'sounds/emb3.wav')
    mixer.music.play()
def adicionaCartaSlot(jogador,url):
    global qtdCartasJogador
    global qtdCartasMaquina
    global urlDesvira

    if jogador=="jogador":
        #1- passo, mover carta slot 2 para a esquerda em (x).
        imagem3.place(x=320,y=460)
        imagem4.place(x=350, y=460)
        qtdCartasJogador=qtdCartasJogador+1
        if qtdCartasJogador==3:
            imag1Carta['file']=url
            imag1.place(x=380,y=460)
        elif qtdCartasJogador==4:
            imag2Carta['file'] = url
            imag2.place(x=410, y=460)
        elif qtdCartasJogador==5:
            imag3Carta['file'] = url
            imag3.place(x=440, y=460)
        elif qtdCartasJogador==6:
            imag4Carta['file'] = url
            imag4.place(x=470, y=460)
        elif qtdCartasJogador==7:
            imag5Carta['file']=url
            imag5.place(x=500,y=460)
    else:
        #é igual a maquina:
        #1- passo desvirar carta slot 2 maquina e mover pra esquerda (x)
        imagem.place(x=320, y=30)
        img2['file'] = urlDesvira
        imagem2.place(x=350, y=30)

        qtdCartasMaquina = qtdCartasMaquina + 1
        if qtdCartasMaquina == 3:
            imag6Carta['file'] = url
            imag6.place(x=380, y=30)

        elif qtdCartasMaquina == 4:
            imag7Carta['file'] = url
            imag7.place(x=410, y=30)

        elif qtdCartasMaquina == 5:
            imag8Carta['file'] = url
            imag8.place(x=440, y=30)

        elif qtdCartasMaquina == 6:
            imag9Carta['file'] = url
            imag9.place(x=470, y=30)

        elif qtdCartasMaquina == 7:
            imag10Carta['file'] = url
            imag10.place(x=500, y=30)



def puxarcarta():
    imagemPer['image']=img_olho_virado
    mixer.init()
    mixer.music.load(r'sounds/DEAL1.wav')
    mixer.music.play()
    global cartasJogador
    global valorJogador
    global valorMaquina

    cartasJogador.append(bara.topo_da_pilha())
    url1 = criaString(descobreCarta(cartasJogador))
    adicionaCartaSlot("jogador",url1)
    jogador = Trata(cartasJogador)
    valorJogador = placarJogador(jogador)
    lbJogador['text']=valorJogador
    print(len(bara.embalharada))#todo - retirar isso daqui -> print testeeeeeeeeeeeeeeeeeeeeeeeeeee
    if valorJogador>21:
        perdeu()
        print("1-perdeu")
        desvira()
        zerarPartida()
        lbJogador['text']=''
        lbMaquina['text']=''

    elif valorJogador==21 and valorMaquina==21:
        empatou()
        desvira()
        print("1-Empate com a maquina!")
        zerarPartida()
    elif valorJogador==21:
        ganhou()
        desvira()
        print("1-ganhou de cara21!")
        zerarPartida()
    elif(valorMaquina==21):
        perdeu()
        desvira()
        print("1-perdeu, maquina ganhou de cara21!")
        zerarPartida()

    elif valorMaquina>21:
        ganhou()
        desvira()
        print("1-ganhou! maquina estourou21")
        zerarPartida()

def pararcarta():
    imagemPer['image'] = img_olho_cima
    global cartasJogador
    global cartasMaquina
    global valorJogador
    global valorMaquina
    if valorJogador==valorMaquina:
        empatou()
        desvira()
        print("c-3 #ESPECIAL#-maquina empatou pois os valores eram iguais NO INICIO")
        zerarPartida()
    elif valorMaquina>valorJogador:
        perdeu()
        desvira()
        print("2-perdeu, maquina tinha valor maior!")
        zerarPartida()
    else:
        # maquina joga!@@@
        while (valorMaquina<valorJogador):
            cartasMaquina.append(bara.topo_da_pilha())
            url2 = criaString(descobreCarta(cartasMaquina))
            adicionaCartaSlot("maquina", url2)
            maquina = Trata(cartasMaquina)
            valorMaquina = placarMaquina(maquina)
            lbMaquina['text']=valorMaquina
            print(len(bara.embalharada))  #todo - retirar isso daqui-> print testeeeeeeeeeeeeeeeeeeeeeeeeeee

        if valorMaquina==valorJogador:
            empatou()
            print("2-empate! maquina decidiu empatar com vc!")
            zerarPartida()
        elif valorMaquina>21:
            ganhou()
            print("2-ganhou! maquina estourou valor!")
            zerarPartida()
        elif valorMaquina==21:
            perdeu()
            print("2-perdeu, maquina fez exatamente21!")
            zerarPartida()
        else:
            perdeu()
            print("2-perdeu! maquina venceu abaixo de 21!")
            zerarPartida()

def sair():
    janela.destroy()

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

def Trata(cartas):
    vet=[]
    for i in range(len(cartas)):
        carM=0
        carM = int(cartas[i][0])
        vet.append(carM)
    return vet

def criaString(entrada):
    s=r"image\Baralho\ "+str(entrada)+".png"
    return s.replace(" ","")

def descobreCarta(mat):
    ultima=mat[-1]
    valor=''
    valor=ultima[1]+ultima[2][0]
    return valor


def jogar():
    EmbaralharSom()
    urlFechada=r"image\cartafechada.png"
    global cartasMaquina
    cartasMaquina= []
    global cartasJogador
    cartasJogador= []
    global valorJogador
    valorJogador= 0
    global valorMaquina
    valorMaquina= 0
    global urlDesvira

    bara.gerar_baralho()
    bara.pilha_embaralhar()

    cartasMaquina.append(bara.topo_da_pilha())
    url1 = criaString(descobreCarta(cartasMaquina))

    cartasJogador.append(bara.topo_da_pilha())
    url3 = criaString(descobreCarta(cartasJogador))

    cartasMaquina.append(bara.topo_da_pilha())
    #este não possui URL pois esta carta esta virada para baixo.
    urlDesvira=criaString(descobreCarta(cartasMaquina))
    # a url foi criada para desvirar esta carta no futuro. e fica salva numa global.

    cartasJogador.append(bara.topo_da_pilha())
    url4 = criaString(descobreCarta(cartasJogador))
    img1['file'] = url1
    img2['file'] = urlFechada
    img3['file'] = url3
    img4['file'] = url4

    print(cartasMaquina)
    print(cartasJogador)

    maquina = Trata(cartasMaquina)
    jogador = Trata(cartasJogador)

    valorMaquina = placarMaquina(maquina)
    valorJogador = placarJogador(jogador)
    lbMaquina['text']=maquina[0]
    lbJogador['text']=valorJogador


'''codigo principal'''

janela = Tk()
janela.title("G'nus Cassinos")
bara = Baralho()
cartasMaquina=[]
cartasJogador=[]
valorJogador=0
valorMaquina=0
qtdCartasJogador=2
qtdCartasMaquina=2
urlDesvira=''
saldo_carteira=250.00
valor_aposta=00.00
r = Raking("blackjack", "f")

'''fim DO codigo principal DA aplicacao'''

#inicio botao reinicio
reinicio=Button(janela)
reinicioimg=PhotoImage(file=r"image\restart2.png")
reinicio['image']=reinicioimg
reinicio['relief']=FLAT
reinicio['command']=novaPartida
reinicio['bg']='#006400'
#fim reincio

#LOGOgnus
logo=Label(janela)
imglogo=PhotoImage(file=r"image\meio2.png")
logo['image']=imglogo
logo['bg']='#006400'
logo.place(x=340,y=240)

#botao comecar partida!
inicio=Button(janela)
imgInicio=PhotoImage(file=r"image\play2.png")
inicio['image']=imgInicio
inicio['relief']=FLAT
inicio['command']=novaPartida
inicio['bg']='#006400'
inicio.place(x=400,y=165)
#fim botao comecar partida!

#MAQUINA SLOT CARTAS
#perfil label img MAQUINA gnu
imagemperfil=Label(janela)
imgperfil=PhotoImage(file=r"image\mrgnu2.png")
imagemperfil['image']=imgperfil
imagemperfil['bg']='#006400'
imagemperfil.place(x=160,y=10)
#fim perfil gnu
#soma, placar da maquina gnu
imagemsomam=Label(janela)
imgsomam=PhotoImage(file=r"image\SOMA.png")
imagemsomam['image']=imgsomam
imagemsomam['bg']='#006400'
imagemsomam.place(x=160,y=130)
#fim placar maquina soma, GNU

#slot 1 para cartas
imagem=Label(janela)
img1=PhotoImage(file="image/cartasSlot.png")
imagem['image']=img1
imagem['bg']='#006400'
imagem.place(x=350,y=30)
#fim slot 1 para cartas
#slot 2 para cartas
imagem2=Label(janela)
img2=PhotoImage(file=r"image\cartasSlot.png")
imagem2['image']=img2
imagem2['bg']='#006400'
imagem2.place(x=443,y=30)
#fim do slot 2 para cartas maquina
#fim maquina !

#JOGADOR SLOT CARTAS
#img personagem jogador perfil
imagemPer=Label(janela)
imgPer=PhotoImage(file=r"image\user2.png")
imagemPer['image']=imgPer
imagemPer['bg']='#006400'
imagemPer.place(x=160,y=430)
#fim perfil jogador img

#imagem de olho virado para mover olho do personagem.
img_olho_virado=PhotoImage(file=r"image\user2vira.png")
img_olho_cima=PhotoImage(file=r"image\user2cima.png")
#fim img de olho virado

#soma label img placar jogador
imagemsoma=Label(janela)
imgsoma=PhotoImage(file=r"image\SOMA.png")
imagemsoma['image']=imgsoma
imagemsoma['bg']='#006400'
imagemsoma.place(x=160,y=550)
#fim label soma, placar do jogador
#slot3, jogador
imagem3=Label(janela)
img3=PhotoImage(file=r"image\cartasSlot.png")
imagem3['image']=img3
imagem3['bg']='#006400'
imagem3.place(x=350,y=460)
#fim slot3 jogador
#slot4 jogador
imagem4=Label(janela)
img4=PhotoImage(file=r"image\cartasSlot.png")
imagem4['image']=img4
imagem4['bg']='#006400'
imagem4.place(x=443,y=460)
#fim slot4 jogador

#inicio quadro ranking
rank=Label(janela)
imgrank=PhotoImage(file=r"image\quadroRanking.png")
rank['bg']="#006400"
rank.place(x=5,y=10)

#label ranking
ranking=Label(janela)
ranking['bg']='#C8AB37'
ranking['font']='Arial',12,"bold"
ranking.place(x=1000,y=38)
ranking['text']=" "
#fim quadro ranking

"""algumas imagens reservas em slots invisiveis que ficarão do lado direito do user: """

imag1 = Label(janela)
imag1Carta = PhotoImage(file=r"image\Baralho\Ao.png")
imag1['image'] = imag1Carta
imag1['bg'] = '#006400'


imag2 = Label(janela)
imag2Carta = PhotoImage(file=r"image\Baralho\Ao.png")
imag2['image'] = imag2Carta
imag2['bg'] = '#006400'


imag3 = Label(janela)
imag3Carta = PhotoImage(file=r"image\Baralho\Ao.png")
imag3['image'] = imag3Carta
imag3['bg'] = '#006400'

imag4 = Label(janela)
imag4Carta = PhotoImage(file=r"image\Baralho\Ao.png")
imag4['image'] = imag4Carta
imag4['bg'] = '#006400'


imag5 = Label(janela)
imag5Carta = PhotoImage(file=r"image\Baralho\Ao.png")
imag5['image'] = imag5Carta
imag5['bg'] = '#006400'

#daqui pra baixo fica slots para mais cartas da maquina!!@

imag6 = Label(janela)
imag6Carta = PhotoImage(file=r"image\Baralho\Ap.png")
imag6['image'] = imag6Carta
imag6['bg'] = '#006400'

imag7 = Label(janela)
imag7Carta = PhotoImage(file=r"image\Baralho\Ap.png")
imag7['image'] = imag7Carta
imag7['bg'] = '#006400'

imag8 = Label(janela)
imag8Carta = PhotoImage(file=r"image\Baralho\Ap.png")
imag8['image'] = imag8Carta
imag8['bg'] = '#006400'

imag9 = Label(janela)
imag9Carta = PhotoImage(file=r"image\Baralho\Ap.png")
imag9['image'] = imag9Carta
imag9['bg'] = '#006400'

imag10 = Label(janela)
imag10Carta = PhotoImage(file=r"image\Baralho\Ap.png")
imag10['image'] = imag10Carta
imag10['bg'] = '#006400'

#botao de parar
btnParar=Button(janela)
btnParar['bg']='#006400'
btnParar['relief']=FLAT
btnParar['command']=pararcarta
imgbtnP=PhotoImage(file=r"image\btnP.png")
btnParar['image']=imgbtnP
#fim botao parar

#botao descer mais carta
btnDescer=Button(janela)
btnDescer['bg']='#006400'
btnDescer['command']=puxarcarta
btnDescer['relief']=FLAT
imgbtnD=PhotoImage(file=r"image\btnD.png")
btnDescer['image']=imgbtnD
#fim botao descer mais carta

#inicio  botao sair sistema
sa=Label(janela,text="Sair")
sa['bg']='#006400'
sa['font']='Arial',12,"bold"
sa['bg']="#C8AB37"
sa.place(x=15,y=570)
btnExit=Button(janela)
btnExit['bg']='#006400'
btnExit['command']=sair
btnExit['relief']=FLAT
imgbtnExit=PhotoImage(file=r"image\exit.png")
btnExit['image']=imgbtnExit
btnExit.place(x=0,y=505)
#FIM BTN SAIR SISTEMA
#monte label img, imagem do monte de cartas no lado direito>>>
imagem5=Label(janela)
img5=PhotoImage(file=r"image\monteC3.png")
imagem5['image']=img5
imagem5['bg']='#006400'
imagem5['height']=300
imagem5['width']=300
imagem5.place(x=670,y=60)
#fim imagem label, monte do lado direito>>>>>>>>>>>>>>>>>>>>>>>

#carteira
carteira=Label(janela)
cimg=PhotoImage(file=r"image\carteira2.png")
carteira['image']=cimg
carteira['bg']="#006400"
carteira.place(x=790,y=20)

qtdcarteira=Label(janela)
qtdcartimg=PhotoImage(file=r"image\qtdcarteira.png")
qtdcarteira['image']=qtdcartimg
qtdcarteira['bg']="#006400"
qtdcarteira.place(x=702,y=47)

saldo_carteira_lb=Label(janela)
saldo_carteira_lb['text']="%.2f"%saldo_carteira
saldo_carteira_lb['bg']="#C8AB37"
saldo_carteira_lb['font']="Arial",12,"bold"
saldo_carteira_lb.place(x=710,y=54)
#fim carteira

#label mostrador da maquina
lbMaquina=Label(janela,text='00')
lbMaquina['font']='Arial',12,"bold"
lbMaquina['bg']="#C8AB37"
lbMaquina.place(x=254,y=138)
#fim label mostrador da maquina
#label mostrador jogador
lbJogador=Label(janela,text='00')
lbJogador['font']='Arial',12,"bold"
lbJogador['bg']="#C8AB37"
lbJogador.place(x=254,y=557)
#fim label mostrador jogador

#medalha ganhou partida
medalha=Label(janela)
imgMedalha=PhotoImage(file=r"image\ganhou2.png")
medalha['image']=imgMedalha
medalha['bg']='#006400'
#fim medalha ganhou partida

#perdeu  partida
perdeuimg=Label(janela)
imgPerdeu=PhotoImage(file=r"image\perdeu1.png")
perdeuimg['image']=imgPerdeu
perdeuimg['bg']='#006400'
#fim perdeu partida

#EMPATOU partida
empateimg=Label(janela)
imgEmpate=PhotoImage(file=r"image\empate.png")
empateimg['image']=imgEmpate
empateimg['bg']='#006400'
#fim EMPATOU partida

#lbResultadoMaquina
lbResultadoMaquina=Label(janela)
lbResultadoMaquina['font']='Arial',12,"bold"
pontoMaquina=PhotoImage(file=r"image\pontoM.png")
lbResultadoMaquina['bg']='#006400'
lbResultadoMaquina['image']=pontoMaquina
#fim lbResultadoMaquina

#lbResultadoJogador
lbResultadoJogador=Label(janela)
lbResultadoJogador['font']='Arial',12,"bold"
pontoJogador=PhotoImage(file=r"image\pontoM.png")
lbResultadoJogador['bg']='#006400'
lbResultadoJogador['image']=pontoJogador
#fim lbResultadoJogador

#lbPontuacao maquina inicio
lbPontuacaoMaquina=Label(janela)
lbPontuacaoMaquina['font']='Arial',12,"bold"
lbPontuacaoMaquina['bg']='#C8AB37'
lbPontuacaoMaquina.place(x=1000, y=165)
#lbPontuacao maquina fim

#lbPontuacao Jogador inicio
lbPontuacaoJogador=Label(janela)
lbPontuacaoJogador['font']='Arial',12,"bold"
lbPontuacaoJogador['bg']="#C8AB37"
lbPontuacaoJogador.place(x=1000, y=415)
#lbPontuacao Jogador fim

#fichas na tela 5,10,25,50,100
ficha5=Button(janela)
fimg5=PhotoImage(file=r"image/ficha/cinco.png")
ficha5['bg']="#006400"
ficha5['image']=fimg5
ficha5['command']=partial(aposta_ficha,5)
ficha5['relief']=FLAT

ficha10=Button(janela)
fimg10=PhotoImage(file=r"image/ficha/dez.png")
ficha10['bg']="#006400"
ficha10['image']=fimg10
ficha10['relief']=FLAT
ficha10['command']=partial(aposta_ficha,10)

ficha25=Button(janela)
fimg25=PhotoImage(file=r"image/ficha/vintecinco.png")
ficha25['bg']="#006400"
ficha25['image']=fimg25
ficha25['relief']=FLAT
ficha25['command']=partial(aposta_ficha,25)

ficha50=Button(janela)
fimg50=PhotoImage(file=r"image/ficha/cinquenta.png")
ficha50['bg']="#006400"
ficha50['image']=fimg50
ficha50['relief']=FLAT
ficha50['command']=partial(aposta_ficha,50)

ficha100=Button(janela)
fimg100=PhotoImage(file=r"image/ficha/cem.png")
ficha100['bg']="#006400"
ficha100['relief']=FLAT
ficha100['image']=fimg100
ficha100['command']=partial(aposta_ficha,100)
#fim de fichas
#quadro de apostas
aposta=Label(janela)
imgAposta=PhotoImage(file=r"image/aposta3.png")
aposta['image']=imgAposta
aposta['bg']="#006400"
#fim quadro de apostas

valor_aposta_lb=Label(janela)
valor_aposta_lb['text']="%.2f"%valor_aposta
valor_aposta_lb['bg']="#C8AB37"
valor_aposta_lb['font']="Arial",12,"bold"

#btn Ok
btnOk=Button(janela)
btnOk['bg']='#006400'
btnOk['command']=Ok
btnOk['relief']=FLAT
imgbtnOk=PhotoImage(file=r"image\btnOk.png")
btnOk['image']=imgbtnOk
btnOk.place(x=1000,y=350)
#fim btn Ok

aposta_status("fechado")# esta linha é super importante para fazer com que as fichas não entrem ao iniciar o sistema.
texto_ranking=imprimir_ranking()

ranking['text']=texto_ranking
rank['image'] = imgrank
ranking.place(x=25, y=43)

#outras configurações da janela..

janela.iconbitmap(r"image\logoSistema.ico")
janela.resizable(0,0)
x = (janela.winfo_screenwidth() // 2) - (900// 2)
y = (janela.winfo_screenheight() // 2) - (600// 2)
janela.geometry("900x600+{}+{}".format(x, y))  # largura x altura + esquerda + topo
janela['bg'] = "#006400"
#janela.overrideredirect(True)#retira bordas
janela.mainloop()
#fim configs da janela e chamada do MAINLOOP()..

#TODO -REVISAR CÓDIGO TODO..!!!!!!