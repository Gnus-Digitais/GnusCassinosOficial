import threading
from tkinter import *
from pygame import mixer
import pygame
import time
from functools import partial
from tkinter import messagebox
from Codigos.slotmachine.SlotMachine import SlotMachine
from Codigos.classes_auxiliares.Ranking import Ranking
from Codigos.tela_principal.Howtoplay import Howtoplay

class TelaSlotMachine:
    """Esta é a classe que possui as funcionalidades do jogo SlotMachine"""
    def __init__(self,user,janela):
        self.__user = user
        pygame.init()
        # criando frame desta janela e posicionando.
        self.janela = Frame(janela)
        self.janela['width'] = 910
        self.janela['height'] = 600
        self.janela['bg'] = "#006400"
        self.janela.place(x=0, y=0)
        # fim do frame tela principal do jogo.

        self.girando=False
        self.saldo_carteira = 250
        self.valor_aposta = 00
        self.status = 0
        self.sm = SlotMachine()
        self.sm.spin()
        self.r = Ranking("slotmachine", "f")
        mixer.init()

        self.imglpdLigada = PhotoImage(file="../slotmachine/imagens/cacaniquel4.png")

        # caça niquel logo !
        self.cNiquel = Label(self.janela)
        self.imgcNiquel = PhotoImage(file="../slotmachine/imagens/cacaniquel3.png")
        self.cNiquel['image'] = self.imgcNiquel
        self.cNiquel['bg'] = "#006400"
        self.cNiquel.place(x=180, y=30)
        # fim caça niquel logo !

        # Primeiro slot
        self.imagem = Label(self.janela)
        self.img1 = PhotoImage(file="../slotmachine/imagens/gnu.png")
        self.imagem['image'] = self.img1
        self.imagem['bg'] = '#fff'
        self.imagem.place(x=230, y=286)

        # Segundo slot
        self.imagem2 = Label(self.janela)
        self.img2 = PhotoImage(file="../slotmachine/imagens/gnu.png")
        self.imagem2['image'] = self.img2
        self.imagem2['bg'] = '#fff'
        self.imagem2.place(x=305, y=286)

        # Terceiro slot
        self.imagem3 = Label(self.janela)
        self.img3 = PhotoImage(file="../slotmachine/imagens/gnu.png")
        self.imagem3['image'] = self.img3
        self.imagem3['bg'] = '#fff'
        self.imagem3.place(x=380, y=286)

        # braco do spin button
        self.imgSpin = Label(self.janela)
        self.imgSpin['bg'] = "#006400"
        self.imgSP = PhotoImage(file=r"../slotmachine/imagens/bracoCima.png")
        self.imgSpin['image'] = self.imgSP
        self.imgSpin.place(x=480, y=200)
        # fim braco spin button

        # Botão de spin
        self.btnSpin = Button(self.janela)
        self.btnSpin['bg'] = '#006400'
        self.btnSpin['relief'] = FLAT
        self.btnSpin['command'] = self.sorteia
        self.imgbtnSpin = PhotoImage(file=r"../slotmachine/imagens\btnSpin.png")
        self.btnSpin['image'] = self.imgbtnSpin
        self.btnSpin.place(x=503, y=190)
        # fim botao spin
        # bolinha inicio
        self.b = Label(self.janela)
        self.b['bg'] = '#006400'
        self.bImg = PhotoImage(file=r"../slotmachine/imagens\Bolinha.png")
        self.b['image'] = self.bImg
        # bolinha fim

        #seta botao
        self.seta=Label(self.janela)
        self.seta['bg']="#006400"
        self.setaimg=PhotoImage(file="../slotmachine/imagens/seta.png")
        self.seta['image']=self.setaimg
        self.seta.place(x=543,y=195)
        #fim seta botao

        self.btnVoltar = Button(self.janela)
        self.imgVoltar = PhotoImage(file="../slotmachine/imagens/voltar2.png")
        self.btnVoltar['image'] = self.imgVoltar
        self.btnVoltar['relief'] = FLAT
        self.btnVoltar['command'] = self.voltar
        self.btnVoltar['bg'] = "#006400"
        self.btnVoltar.place(x=2, y=530)

        # carteira
        self.carteira = Label(self.janela)
        self.cimg = PhotoImage(file=r"../slotmachine/imagens/carteira2.png")
        self.carteira['image'] = self.cimg
        self.carteira['bg'] = "#006400"
        self.carteira.place(x=790, y=20)

        self.qtdcarteira = Label(self.janela)
        self.qtdcartimg = PhotoImage(file=r"../slotmachine/imagens/qtdcarteira.png")
        self.qtdcarteira['image'] = self.qtdcartimg
        self.qtdcarteira['bg'] = "#006400"
        self.qtdcarteira.place(x=702, y=47)

        self.saldo_carteira_lb = Label(self.janela)
        self.saldo_carteira_lb['text'] =  self.saldo_carteira
        self.saldo_carteira_lb['bg'] = "#C8AB37"
        self.saldo_carteira_lb['font'] = "Arial", 12, "bold"
        self.saldo_carteira_lb.place(x=710, y=54)
        # fim carteira

        # fichas na tela 5,10,25,50,100
        self.ficha5 = Button(self.janela)
        self.fimg5 = PhotoImage(file=r"../slotmachine/imagens/ficha/cinco.png")
        self.ficha5['bg'] = "#006400"
        self.ficha5['image'] = self.fimg5
        self.ficha5['command'] = partial(self.aposta_ficha, 5)
        self.ficha5['relief'] = FLAT

        self.ficha10 = Button(self.janela)
        self.fimg10 = PhotoImage(file=r"../slotmachine/imagens/ficha/dez.png")
        self.ficha10['bg'] = "#006400"
        self.ficha10['image'] = self.fimg10
        self.ficha10['relief'] = FLAT
        self.ficha10['command'] = partial(self.aposta_ficha, 10)

        self.ficha25 = Button(self.janela)
        self.fimg25 = PhotoImage(file=r"../slotmachine/imagens/ficha/vintecinco.png")
        self.ficha25['bg'] = "#006400"
        self.ficha25['image'] = self.fimg25
        self.ficha25['relief'] = FLAT
        self.ficha25['command'] = partial(self.aposta_ficha, 25)

        self.ficha50 = Button(self.janela)
        self.fimg50 = PhotoImage(file=r"../slotmachine/imagens/ficha/cinquenta.png")
        self.ficha50['bg'] = "#006400"
        self.ficha50['image'] = self.fimg50
        self.ficha50['relief'] = FLAT
        self.ficha50['command'] = partial(self.aposta_ficha, 50)

        self.ficha100 = Button(self.janela)
        self.fimg100 = PhotoImage(file=r"../slotmachine/imagens/ficha/cem.png")
        self.ficha100['bg'] = "#006400"
        self.ficha100['relief'] = FLAT
        self.ficha100['image'] = self.fimg100
        self.ficha100['command'] = partial(self.aposta_ficha, 100)
        # fim de fichas
        # quadro de apostas
        self.aposta = Label(self.janela)
        self.imgAposta = PhotoImage(file=r"../slotmachine/imagens/aposta3.png")
        self.aposta['image'] = self.imgAposta
        self.aposta['bg'] = "#006400"
        # fim quadro de apostas

        self.valor_aposta_lb = Label(self.janela)
        self.valor_aposta_lb['text'] = self.valor_aposta
        self.valor_aposta_lb['bg'] = "#C8AB37"
        self.valor_aposta_lb['font'] = "Arial", 12, "bold"

        # inicio quadro ranking
        self.rank = Label(self.janela)
        self.imgrank = PhotoImage(file=r"../Jogo21/image/quadroRanking.png")
        self.rank['bg'] = "#006400"
        self.rank.place(x=9, y=10)

        # label ranking
        self.ranking = Label(self.janela)
        self.ranking['bg'] = '#C8AB37'
        self.ranking['font'] = 'Arial', 12, "bold"
        self.ranking.place(x=1000, y=38)
        self.ranking['text'] = " "
        # fim quadro ranking

        self.aposta_status("aberto")

        self.texto_ranking = self.imprimir_ranking()
        self.ranking['text'] = self.texto_ranking
        self.rank['image'] = self.imgrank
        self.ranking.place(x=25, y=43)

        # lbAlerta(movimento invalido) inicio
        self.lbAlerta_aposta = Label(self.janela,text="Efetue uma aposta!")
        self.lbAlerta_aposta['font'] = 'Arial', 12, "bold"
        self.lbAlerta_aposta['bg'] = "#ff0000" #cor anterior: #C8AB37
        self.lbAlerta_aposta['fg']="#fff"
        self.lbAlerta_aposta.place(x=1000, y=450)
        # lbAlerta(MOVIMENTO INVALIDO) FIM

        # lbAlerta Quantia aposta invalida
        self.lbAlerta_quantia = Label(self.janela,text="Saldo insuficiente!")
        self.lbAlerta_quantia['font'] = 'Arial', 12, "bold"
        self.lbAlerta_quantia['bg'] = "#ff0000"
        self.lbAlerta_quantia['fg']='#fff'
        self.lbAlerta_quantia.place(x=1000, y=450)
        # fim lbAlerta Quantia aposta invalida

        # lbAlerta Quantia aposta invalida
        self.lbAlerta_sair = Label(self.janela,text="Espere finalizar a partida!")
        self.lbAlerta_sair['font'] = 'Arial', 12, "bold"
        self.lbAlerta_sair['fg']='#fff'
        self.lbAlerta_sair['bg'] = "#ff0000"
        self.lbAlerta_sair.place(x=1000, y=450)
        # fim lbAlerta Quantia aposta invalida

        self.btn_how_to_play = Button(self.janela)
        self.imgbtn_how_to_play = PhotoImage(file="imagem/howtoplaybutton.png")
        self.btn_how_to_play['image'] = self.imgbtn_how_to_play
        self.btn_how_to_play['relief'] = FLAT
        self.btn_how_to_play['command'] = self.abre_how_to_play
        self.btn_how_to_play['bg'] = "#006400"
        self.btn_how_to_play.place(x=2, y=465)


    #temporizador
    def trhead_temporizador(self, tempo, texto, xA, yA, xNovo, yNovo):
        """mostra por um breve tempo na tela"""
        texto.place(x=xNovo, y=yNovo)
        time.sleep(tempo)
        texto.place(x=xA, y=yA)

    def mostra_temporizado(self, tempo, texto, xA, yA, xNovo, yNovo):
        """Este metodo serve para mostrar um componente na tela por um tempo pré-determinado."""
        threading.Timer(0.1, partial(self.trhead_temporizador, tempo, texto, xA, yA, xNovo, yNovo)).start()

    # get e set do user
    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, valor):
        self.__user = valor

    def abre_how_to_play(self):
        """Este método serve para abrir o how to play da tela slotmachine."""
        Howtoplay(self.janela, "slotmachine")

    def aposta_status(self, stat):
        """Este método serve para esconder as fichas(botões), do jogador no momento em que esses botões não são necessários"""
        if stat == "aberto":
            self.ficha5.place(x=597, y=520)
            self.ficha10.place(x=657, y=520)
            self.ficha25.place(x=717, y=520)
            self.ficha50.place(x=777, y=520)
            self.ficha100.place(x=837, y=520)
            self.aposta.place(x=657, y=345)
            self.btnSpin.place(x=503, y=190)
            self.valor_aposta_lb.place(x=740, y=415)
        else:
            self.ficha5.place(x=1000, y=500)
            self.ficha10.place(x=1070, y=500)
            self.ficha25.place(x=1140, y=500)
            self.ficha50.place(x=1130, y=500)
            self.ficha100.place(x=1100, y=500)
            self.btnSpin.place(x=503, y=190)

    def aposta_ficha(self, ficha):
        """Este método serve para configurar apostas feitas pelo jogador, e também mudar o valor da carteira do jogador"""
        if self.saldo_carteira - ficha >= 0:
            self.cliqueMoeda() # esta linha adiciona o som ao clique nas fichas.
            if ficha == 5:
                self.valor_aposta = self.valor_aposta + 5
                self.saldo_carteira = self.saldo_carteira - 5
                self.saldo_carteira_lb['text'] =  self.saldo_carteira
                self.valor_aposta_lb['text'] =  self.valor_aposta
            if ficha == 10:
                self.valor_aposta = self.valor_aposta + 10
                self.saldo_carteira = self.saldo_carteira - 10
                self.saldo_carteira_lb['text'] =  self.saldo_carteira
                self.valor_aposta_lb['text'] =  self.valor_aposta
            if ficha == 25:
                self.valor_aposta = self.valor_aposta + 25
                self.saldo_carteira = self.saldo_carteira - 25
                self.saldo_carteira_lb['text'] = self.saldo_carteira
                self.valor_aposta_lb['text'] =  self.valor_aposta
            if ficha == 50:
                self.valor_aposta = self.valor_aposta + 50
                self.saldo_carteira = self.saldo_carteira - 50
                self.saldo_carteira_lb['text'] = self.saldo_carteira
                self.valor_aposta_lb['text'] = self.valor_aposta
            if ficha == 100:
                self.valor_aposta = self.valor_aposta + 100
                self.saldo_carteira = self.saldo_carteira - 100
                self.saldo_carteira_lb['text'] = self.saldo_carteira
                self.valor_aposta_lb['text'] = self.valor_aposta
        else:
            self.mostra_temporizado(0.5,self.lbAlerta_quantia,1000,400,690,450)

    def reseta(self):
        """Este metodo serve para Configurar uma nova partida limpando a tela sem alterar o valor da carteira."""
        self.valor_aposta = 00
        self.valor_aposta_lb['text'] =self.valor_aposta
        self.aposta_status("aberto")

    def voltar(self):
        """este metodo serve para retornar a tela principal do jogo"""
        if self.girando==False:
            pygame.quit()
            self.janela.destroy()
        else:
            self.mostra_temporizado(0.5,self.lbAlerta_sair,1000,400,65,550)#mensagem se alerta.

    def pin(self):
        """este metodo serve para tocar o som mp3 que inicia assim que o slot termina de girar."""
        mixer.music.load(r'../slotmachine/sounds/DEAL1.wav')
        mixer.music.play()

    def perdeuSom(self):
        """Este metodo serve para tocar o som de - perdeu"""
        mixer.music.load(r'../slotmachine/sounds/uhoh.mp3')  # perdeu
        mixer.music.play()

    def ganhouSom(self):
        """Este metodo serve para tocar o som de - ganhou"""
        mixer.music.load(r'../slotmachine/sounds/ganhou.mp3')  # ganhou
        mixer.music.play()

    def cliqueMoeda(self):
        """Este método serve para tocar o som de - clique ao pressionar uma ficha de aposta"""
        mixer.music.load(r"../slotmachine/sounds/moeda2.wav") # clique
        mixer.music.play()
    def muda_alavanca(self,status):
        """Este metodo serve para mudar a alavanca para 'cima' ou 'baixo'. """
        if status=="cima":
            #status e cima
            self.imgSpin.place(x=480, y=200)
            self.imgSP['file'] = r"../slotmachine/imagens/bracoCima.png"
            self.btnSpin.place(x=503, y=190)
            self.btnSpin['image']=self.imgbtnSpin
            self.b['image']=''
            self.b.place(x=0,y=0)
            self.seta.place(x=543, y=195)
        else:
            #status está baixo
            self.imgSpin.place(x=480, y=291)
            self.imgSP['file'] = r"../slotmachine/imagens/bracoBaixo.png"
            self.btnSpin.place(x=0,y=0)
            self.btnSpin['image']=""
            self.b['image']=self.bImg
            self.b.place(x=503,y=390)
            self.seta.place(x=1000, y=195)

    def iniciar(self):
        """Este método serve para iniciar o sorteio do SlotMachine.(inicia máquina)."""
        self.girando=True
        vet_auxiliar=[]
        resposta=False
        threading.Timer(0.1, self.muda_meio).start()
        self.status=0
        # for - 25 é uma forma de fazer tempo junto com o time.sleep()0.090 la de baixo.
        for i in range(25):
            nome = str(self.sm.spin())
            self.img1['file'] = "../slotmachine/imagens/slots/"+nome+".png"
            nome2 = str(self.sm.spin())
            self.img2['file'] = "../slotmachine/imagens/slots/" + nome2 + ".png"
            nome3 = str(self.sm.spin())
            self.img3['file'] = "../slotmachine/imagens/slots/" + nome3 + ".png"

            if i==22:
                self.pin()
            time.sleep(0.09)
        vet_auxiliar.append(nome)
        for j in range(8):
            nome2 = str(self.sm.spin())
            self.img2['file'] = "../slotmachine/imagens/slots/" + nome2 + ".png"
            nome3 = str(self.sm.spin())
            self.img3['file'] = "../slotmachine/imagens/slots/" + nome3 + ".png"

            if j==7:
                self.pin()
            time.sleep(0.09)
        vet_auxiliar.append(nome2)
        for k in range(6):
            nome3 = str(self.sm.spin())
            self.img3['file'] = "../slotmachine/imagens/slots/" + nome3 + ".png"

            if k==5:
                self.pin()
            time.sleep(0.09)
        vet_auxiliar.append(nome3)
        self.status = 1
        self.muda_alavanca("cima")
        resposta = self.igual(vet_auxiliar)#chama método que compara valores do vetor auxiliar que contém as imagens sorteadas.
        self.girando = False
        if resposta == True:
            # ganhou
            self.ganhouSom()
            # multiplica por 10 o valor da aposta
            self.saldo_carteira = self.saldo_carteira + (self.valor_aposta * 10)
            self.saldo_carteira_lb['text'] = self.saldo_carteira
            self.inserir_no_ranking(self.saldo_carteira)
            self.ranking['text'] = self.imprimir_ranking()
            self.reseta()
        else:
            self.reseta()
            self.perdeuSom()
            # perdeu
            # verifica se a carteira possui dinheiro, caso contrário sai do jogo.
            if self.saldo_carteira < 1:
                messagebox.showinfo("Que pena!", "Perdeu tudo!")
                self.voltar()

    def igual(self,vet):
        """Este é o metodo que comparar as imagens sorteadas pela maquina SLOTMACHINE. este metodo retorna true ou false."""
        anterior=vet[0]
        contador=1
        for i in range(2):
            if vet[i+1]==anterior:
                anterior=vet[i+1]
                contador=contador+1
        if contador==3:
            return True
        else:
            return False

    def imprimir_ranking(self):
        """este metodo serve para retornar uma string com os nomes e pontuação que aparecerão no ranking"""
        return self.r.retorna_ranking()

    def inserir_no_ranking(self, score):
        """este metodo adiciona o usuario do game ao ranking"""
        self.r.addRecord(self.user, int(score))

    def sorteia(self):
        """Este metodo serve para inicializar a maquina slotmachine chamando a threading responsável."""
        if self.valor_aposta > 0:
            self.aposta_status("fechado")
            # muda_alavanca("meio")
            self.muda_alavanca("baixo")
            threading.Timer(0.1, self.iniciar).start()
        else:
            self.mostra_temporizado(0.5, self.lbAlerta_aposta, 1000, 400, 680, 450)#alerta proibido iniciar antes de apostar.

    def muda_meio(self):
        """Este metodo serve para piscar lampadas da maquina slotmachine constantemente."""
        while self.status!=1:
            self.cNiquel['image']=self.imgcNiquel
            time.sleep(0.2)
            self.cNiquel['image']=self.imglpdLigada
            time.sleep(0.2)
