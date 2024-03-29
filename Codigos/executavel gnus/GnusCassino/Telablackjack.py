from baralho import Baralho
from Howtoplay import Howtoplay
from pygame import mixer
from tkinter import *
from Ranking import Ranking
from functools import partial
from tkinter import messagebox
import time
import threading
import pygame


class Telablackjack:
    """Esta é a classe TelablackJack que serve que é usada para criar a tela do jogo blackjack e todas as funcionalidades da mesma."""
    def __init__(self, user,janela):
        self.__user = user
        pygame.init()
        #criando frame desta janela e posicionando.
        self.janela = Frame(janela)
        self.janela['width'] = 910
        self.janela['height'] = 600
        self.janela['bg'] = "#006400"
        self.janela.place(x=0, y=0)
        #fim do frame tela principal do jogo.
        mixer.init()
        self.bara = Baralho()
        self.r = Ranking("blackjack")
        self.cartasMaquina = []
        self.cartasJogador = []
        self.valorJogador = 0
        self.valorMaquina = 0
        self.qtdCartasJogador = 2
        self.qtdCartasMaquina = 2
        self.urlDesvira = ''
        self.saldo_carteira = 250
        self.valor_aposta = 00

        # inicio botao reinicio
        self.reinicio = Button(self.janela)
        self.reinicioimg =PhotoImage(file="imagem/restart2.png")
        self.reinicio['image'] = self.reinicioimg
        self.reinicio['relief'] = FLAT
        self.reinicio['command'] = self.novaPartida
        self.reinicio['bg'] = '#006400'
        # fim reinicio

        # LOGOgnus
        self.logo = Label(self.janela)
        self.imglogo = PhotoImage(file="imagem/meio2.png")
        self.logo['image'] = self.imglogo
        self.logo['bg'] = '#006400'
        self.logo.place(x=340, y=240)

        # botao comecar partida!
        self.inicio = Button(self.janela)
        self.imgInicio = PhotoImage(file=r"imagem/play2.png")
        self.inicio['image'] = self.imgInicio
        self.inicio['relief'] = FLAT
        self.inicio['command'] = self.novaPartida
        self.inicio['bg'] = '#006400'
        self.inicio.place(x=400, y=165)

        # MAQUINA SLOT CARTAS
        # perfil label img MAQUINA gnu
        self.mperfil = Label(self.janela)
        self.imgperfil = PhotoImage(file=r"imagem/mrgnu2.png")
        self.mperfil['image'] = self.imgperfil
        self.mperfil['bg'] = '#006400'
        self.mperfil.place(x=160, y=10)

        # soma, placar da maquina gnu
        self.msomam = Label(self.janela)
        self.imgsomam = PhotoImage(file=r"imagem/SOMA.png")
        self.msomam['image'] = self.imgsomam
        self.msomam['bg'] = '#006400'
        self.msomam.place(x=160, y=130)

        # slot 1 para cartas
        self.m = Label(self.janela)
        self.img1 = PhotoImage(file="imagem/cartasSlot.png")
        self.m['image'] = self.img1
        self.m['bg'] = '#006400'
        self.m.place(x=350, y=30)

        # slot 2 para cartas
        self.m2 = Label(self.janela)
        self.img2 = PhotoImage(file=r"imagem/cartasSlot.png")
        self.m2['image'] = self.img2
        self.m2['bg'] = '#006400'
        self.m2.place(x=443, y=30)

        # JOGADOR SLOT CARTAS
        # img personagem jogador perfil
        self.mPer = Label(self.janela)
        self.imgPer = PhotoImage(file=r"imagem/user2.png")
        self.mPer['image'] = self.imgPer
        self.mPer['bg'] = '#006400'
        self.mPer.place(x=160, y=430)

        # m_principal de olho virado para mover olho do personagem.
        self.img_olho_virado = PhotoImage(file=r"imagem/user2vira.png")
        self.img_olho_cima_ganhou = PhotoImage(file=r"imagem/user2cimaganhou.png")
        self.img_olho_cima_perdeu = PhotoImage(file=r"imagem/user2cimaperdeu.png")
        self.img_olho_cima_empatou = PhotoImage(file=r"imagem/user2cimaempatou.png")
        #img da maquina
        self.img_olho_ganhou=PhotoImage(file=r"imagem/mrgnu2ganhou.png")
        self.img_olho_perdeu = PhotoImage(file=r"imagem/mrgnu2perdeu.png")

        # soma label img placar jogador
        self.msoma = Label(self.janela)
        self.imgsoma = PhotoImage(file=r"imagem/SOMA.png")
        self.msoma['image'] = self.imgsoma
        self.msoma['bg'] = '#006400'
        self.msoma.place(x=160, y=550)

        # slot3, jogador
        self.m3 = Label(self.janela)
        self.img3 = PhotoImage(file=r"imagem/cartasSlot.png")
        self.m3['image'] = self.img3
        self.m3['bg'] = '#006400'
        self.m3.place(x=350, y=460)

        # slot4 jogador
        self.m4 = Label(self.janela)
        self.img4 = PhotoImage(file=r"imagem/cartasSlot.png")
        self.m4['image'] = self.img4
        self.m4['bg'] = '#006400'
        self.m4.place(x=443, y=460)

        # inicio quadro ranking
        self.rank = Label(self.janela)
        self.imgrank = PhotoImage(file=r"imagem/quadroRanking.png")
        self.rank['bg'] = "#006400"
        self.rank.place(x=9, y=10)

        # label ranking
        self.ranking = Label(self.janela)
        self.ranking['bg'] = '#C8AB37'
        self.ranking['font'] = 'Arial', 12, "bold"
        self.ranking.place(x=1000, y=38)
        self.ranking['text'] = " "

        #algumas ns_slotmachine reservas em slots invisiveis que ficarão do lado direito do user..

        self.imag1 = Label(self.janela)
        self.imag1Carta = PhotoImage(file=r"imagem/Baralho\Ao.png")
        self.imag1['image'] = self.imag1Carta
        self.imag1['bg'] = '#006400'

        self.imag2 = Label(self.janela)
        self.imag2Carta = PhotoImage(file=r"imagem/Baralho\Ao.png")
        self.imag2['image'] = self.imag2Carta
        self.imag2['bg'] = '#006400'

        self.imag3 = Label(self.janela)
        self.imag3Carta = PhotoImage(file=r"imagem/Baralho\Ao.png")
        self.imag3['image'] = self.imag3Carta
        self.imag3['bg'] = '#006400'

        self.imag4 = Label(self.janela)
        self.imag4Carta = PhotoImage(file=r"imagem/Baralho\Ao.png")
        self.imag4['image'] = self.imag4Carta
        self.imag4['bg'] = '#006400'

        self.imag5 = Label(self.janela)
        self.imag5Carta = PhotoImage(file=r"imagem/Baralho\Ao.png")
        self.imag5['image'] = self.imag5Carta
        self.imag5['bg'] = '#006400'

        # daqui pra baixo fica slots para mais cartas da maquina!!@

        self.imag6 = Label(self.janela)
        self.imag6Carta = PhotoImage(file=r"imagem/Baralho\Ap.png")
        self.imag6['image'] = self.imag6Carta
        self.imag6['bg'] = '#006400'

        self.imag7 = Label(self.janela)
        self.imag7Carta = PhotoImage(file=r"imagem/Baralho\Ap.png")
        self.imag7['image'] = self.imag7Carta
        self.imag7['bg'] = '#006400'

        self.imag8 = Label(self.janela)
        self.imag8Carta = PhotoImage(file=r"imagem/Baralho\Ap.png")
        self.imag8['image'] = self.imag8Carta
        self.imag8['bg'] = '#006400'

        self.imag9 = Label(self.janela)
        self.imag9Carta = PhotoImage(file=r"imagem/Baralho\Ap.png")
        self.imag9['image'] = self.imag9Carta
        self.imag9['bg'] = '#006400'

        self.imag10 = Label(self.janela)
        self.imag10Carta = PhotoImage(file=r"imagem/Baralho\Ap.png")
        self.imag10['image'] = self.imag10Carta
        self.imag10['bg'] = '#006400'

        # botao de parar
        self.btnParar = Button(self.janela)
        self.btnParar['bg'] = '#006400'
        self.btnParar['relief'] = FLAT
        self.btnParar['command'] = self.pararcarta
        self.imgbtnP = PhotoImage(file=r"imagem/btnP2.png")
        self.btnParar['image'] = self.imgbtnP

        # botao descer mais carta
        self.btnDescer = Button(self.janela)
        self.btnDescer['bg'] = '#006400'
        self.btnDescer['command'] = self.puxarcarta
        self.btnDescer['relief'] = FLAT
        self.imgbtnD = PhotoImage(file=r"imagem/btnD2.png")
        self.btnDescer['image'] = self.imgbtnD

        # inicio  botao voltar para tela principal
        self.btnVoltar = Button(self.janela)
        self.btnVoltar['bg'] = '#006400'
        self.btnVoltar['command'] = self.voltar
        self.btnVoltar['relief'] = FLAT
        self.imgbtnVoltar = PhotoImage(file=r"imagem/voltar2.png")
        self.btnVoltar['image'] = self.imgbtnVoltar
        self.btnVoltar.place(x=2, y=530)

        # monte label img, m_principal do monte de cartas no lado direito>>>
        self.m5 = Label(self.janela)
        self.img5 = PhotoImage(file=r"imagem/monteC3.png")
        self.m5['image'] = self.img5
        self.m5['bg'] = '#006400'
        self.m5['height'] = 300
        self.m5['width'] = 300
        self.m5.place(x=670, y=60)

        # carteira
        self.carteira = Label(self.janela)
        self.cimg = PhotoImage(file=r"imagem/carteira2.png")
        self.carteira['image'] = self.cimg
        self.carteira['bg'] = "#006400"
        self.carteira.place(x=790, y=20)

        self.qtdcarteira = Label(self.janela)
        self.qtdcartimg = PhotoImage(file=r"imagem/qtdcarteira.png")
        self.qtdcarteira['image'] = self.qtdcartimg
        self.qtdcarteira['bg'] = "#006400"
        self.qtdcarteira.place(x=702, y=47)

        self.saldo_carteira_lb = Label(self.janela)
        self.saldo_carteira_lb['text'] =   self.saldo_carteira
        self.saldo_carteira_lb['bg'] = "#C8AB37"
        self.saldo_carteira_lb['font'] = "Arial", 12, "bold"
        self.saldo_carteira_lb.place(x=710, y=54)
        # fim carteira

        # label mostrador da maquina
        self.lbMaquina = Label(self.janela, text='00')
        self.lbMaquina['font'] = 'Arial', 12, "bold"
        self.lbMaquina['bg'] = "#C8AB37"
        self.lbMaquina.place(x=254, y=138)

        # label mostrador jogador
        self.lbJogador = Label(self.janela, text='00')
        self.lbJogador['font'] = 'Arial', 12, "bold"
        self.lbJogador['bg'] = "#C8AB37"
        self.lbJogador.place(x=254, y=557)


        # medalha ganhou partida
        self.medalha = Label(self.janela)
        self.imgMedalha = PhotoImage(file=r"imagem/ganhou2.png")
        self.medalha['image'] = self.imgMedalha
        self.medalha['bg'] = '#006400'

        # perdeu  partida
        self.perdeuimg = Label(self.janela)
        self.imgPerdeu = PhotoImage(file=r"imagem/perdeu1.png")
        self.perdeuimg['image'] = self.imgPerdeu
        self.perdeuimg['bg'] = '#006400'

        # EMPATOU partida
        self.empateimg = Label(self.janela)
        self.imgEmpate = PhotoImage(file=r"imagem/empate.png")
        self.empateimg['image'] = self.imgEmpate
        self.empateimg['bg'] = '#006400'

        # lbResultadoMaquina
        self.lbResultadoMaquina = Label(self.janela)
        self.lbResultadoMaquina['font'] = 'Arial', 12, "bold"
        self.pontoMaquina = PhotoImage(file=r"imagem/pontoM.png")
        self.lbResultadoMaquina['bg'] = '#006400'
        self.lbResultadoMaquina['image'] = self.pontoMaquina

        # lbResultadoJogador
        self.lbResultadoJogador = Label(self.janela)
        self.lbResultadoJogador['font'] = 'Arial', 12, "bold"
        self.pontoJogador = PhotoImage(file=r"imagem/pontoM.png")
        self.lbResultadoJogador['bg'] = '#006400'
        self.lbResultadoJogador['image'] = self.pontoJogador

        # lbPontuacao maquina inicio
        self.lbPontuacaoMaquina = Label(self.janela)
        self.lbPontuacaoMaquina['font'] = 'Arial', 12, "bold"
        self.lbPontuacaoMaquina['bg'] = '#C8AB37'
        self.lbPontuacaoMaquina.place(x=1000, y=165)

        # lbPontuacao Jogador inicio
        self.lbPontuacaoJogador = Label(self.janela)
        self.lbPontuacaoJogador['font'] = 'Arial', 12, "bold"
        self.lbPontuacaoJogador['bg'] = "#C8AB37"
        self.lbPontuacaoJogador.place(x=1000, y=415)

        # btnapagarvaloraposta - este botão cancela o que foi apostado.
        self.btn_apagar_aposta = Button(self.janela)
        self.imgbtn_apagar_aposta = PhotoImage(file="imagem/btnApagar.png")
        self.btn_apagar_aposta['image'] = self.imgbtn_apagar_aposta
        self.btn_apagar_aposta['relief'] = FLAT
        self.btn_apagar_aposta['command'] = self.cancelar_aposta
        self.btn_apagar_aposta['bg'] = "#006400"
        self.btn_apagar_aposta.place(x=1000, y=450)

        # fichas na tela 5,10,25,50,100
        self.ficha5 = Button(self.janela)
        self.fimg5 = PhotoImage(file=r"imagem/ficha/cinco.png")
        self.ficha5['bg'] = "#006400"
        self.ficha5['image'] = self.fimg5
        self.ficha5['command'] = partial(self.aposta_ficha, 5)
        self.ficha5['relief'] = FLAT

        self.ficha10 = Button(self.janela)
        self.fimg10 = PhotoImage(file=r"imagem/ficha/dez.png")
        self.ficha10['bg'] = "#006400"
        self.ficha10['image'] = self.fimg10
        self.ficha10['relief'] = FLAT
        self.ficha10['command'] = partial(self.aposta_ficha, 10)

        self.ficha25 = Button(self.janela)
        self.fimg25 = PhotoImage(file=r"imagem/ficha/vintecinco.png")
        self.ficha25['bg'] = "#006400"
        self.ficha25['image'] = self.fimg25
        self.ficha25['relief'] = FLAT
        self.ficha25['command'] = partial(self.aposta_ficha, 25)

        self.ficha50 = Button(self.janela)
        self.fimg50 = PhotoImage(file=r"imagem/ficha/cinquenta.png")
        self.ficha50['bg'] = "#006400"
        self.ficha50['image'] = self.fimg50
        self.ficha50['relief'] = FLAT
        self.ficha50['command'] = partial(self.aposta_ficha, 50)

        self.ficha100 = Button(self.janela)
        self.fimg100 = PhotoImage(file=r"imagem/ficha/cem.png")
        self.ficha100['bg'] = "#006400"
        self.ficha100['relief'] = FLAT
        self.ficha100['image'] = self.fimg100
        self.ficha100['command'] = partial(self.aposta_ficha, 100)
        # fim de fichas

        # quadro de apostas
        self.aposta = Label(self.janela)
        self.imgAposta = PhotoImage(file=r"imagem/aposta3.png")
        self.aposta['image'] = self.imgAposta
        self.aposta['bg'] = "#006400"

        self.valor_aposta_lb = Label(self.janela)
        self.valor_aposta_lb['text'] =   self.valor_aposta
        self.valor_aposta_lb['bg'] = "#C8AB37"
        self.valor_aposta_lb['font'] = "Arial", 12, "bold"

        # btn Ok
        self.btnOk = Button(self.janela)
        self.btnOk['bg'] = '#006400'
        self.btnOk['command'] = self.Ok
        self.btnOk['relief'] = FLAT
        self.imgbtnOk = PhotoImage(file=r"imagem/btnOk.png")
        self.btnOk['image'] = self.imgbtnOk
        self.btnOk.place(x=1000, y=350)


        self.aposta_status("fechado")  # esta linha é super importante para fazer com que as fichas não entrem ao iniciar o sistema.
        self.texto_ranking = self.imprimir_ranking()

        self.ranking['text'] = self.texto_ranking
        self.rank['image'] = self.imgrank
        self.ranking.place(x=25, y=43)

        # lbAlerta(movimento invalido) inicio
        self.lbAlerta_aposta = Label(self.janela,text="Efetue uma aposta!")
        self.lbAlerta_aposta['font'] = 'Arial', 12, "bold"
        self.lbAlerta_aposta['bg'] = "#ff0000"
        self.lbAlerta_aposta['fg']="#fff"
        self.lbAlerta_aposta.place(x=1000, y=450)

        #lbAlerta Quantia aposta invalida
        self.lbAlerta_quantia = Label(self.janela,text="Saldo insuficiente!")
        self.lbAlerta_quantia['font'] = 'Arial', 12, "bold"
        self.lbAlerta_quantia['bg'] = "#ff0000"#COR Do BG da mensagem ANTIGA:C8AB37
        self.lbAlerta_quantia['fg']="#fff"
        self.lbAlerta_quantia.place(x=1000, y=450)

        self.btn_how_to_play = Button(self.janela)
        self.imgbtn_how_to_play = PhotoImage(file="imagem/howtoplaybutton.png")
        self.btn_how_to_play['image'] = self.imgbtn_how_to_play
        self.btn_how_to_play['relief'] = FLAT
        self.btn_how_to_play['command'] = self.abre_how_to_play
        self.btn_how_to_play['bg'] = "#006400"
        self.btn_how_to_play.place(x=2, y=465)


    def trhead_temporizador(self,tempo,texto,xA,yA,xNovo,yNovo):
        """mostra por um breve tempo na tela"""
        texto.place(x=xNovo, y=yNovo)
        time.sleep(tempo)
        texto.place(x=xA, y=yA)

    def mostra_temporizado(self,tempo,texto,xA,yA,xNovo,yNovo):
        """Este método serve para colocar um componente na tela por um tempo pré-determinado"""
        threading.Timer(0.1, partial(self.trhead_temporizador,tempo,texto,xA,yA,xNovo,yNovo)).start()

    #get e set do user
    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, valor):
        self.__user = valor

    def abre_how_to_play(self):
        """este metodo serve para abrir o how to play da tela blackjack"""
        Howtoplay(self.janela, "blackjack")

    def aposta_status(self,stat):
        """Este método serve para esconder as fichas(botões), do jogador no momento em que esses botões não são necessários"""
        if stat == "aberto":
            self.btn_apagar_aposta.place(x=859, y=377)
            self.ficha5.place(x=597, y=520)
            self.ficha10.place(x=657, y=520)
            self.ficha25.place(x=717, y=520)
            self.ficha50.place(x=777, y=520)
            self.ficha100.place(x=837, y=520)
            self.aposta.place(x=657, y=345)
            self.btnOk.place(x=575, y=375)
            self.valor_aposta_lb.place(x=740, y=415)
        else:
            self.btn_apagar_aposta.place(x=1000, y=377)
            self.ficha5.place(x=1000, y=500)
            self.ficha10.place(x=1070, y=500)
            self.ficha25.place(x=1140, y=500)
            self.ficha50.place(x=1130, y=500)
            self.ficha100.place(x=1100, y=500)
            self.btnOk.place(x=1000, y=240)

    def aposta_ficha(self,ficha):
        """Este método serve para configurar apostas feitas pelo jogador, e também mudar o valor da carteira do jogador"""
        if self.saldo_carteira - ficha >= 0:
            self.cliqueMoeda()# som de clique na ficha.
            if ficha == 5:
                self.valor_aposta = self.valor_aposta + 5
                self.saldo_carteira = self.saldo_carteira - 5
                self.saldo_carteira_lb['text'] =   self.saldo_carteira
                self.valor_aposta_lb['text'] =   self.valor_aposta
            if ficha == 10:
                self.valor_aposta = self.valor_aposta + 10
                self.saldo_carteira = self.saldo_carteira - 10
                self.saldo_carteira_lb['text'] =   self.saldo_carteira
                self.valor_aposta_lb['text'] =   self.valor_aposta
            if ficha == 25:
                self.valor_aposta = self.valor_aposta + 25
                self.saldo_carteira = self.saldo_carteira - 25
                self.saldo_carteira_lb['text'] =   self.saldo_carteira
                self.valor_aposta_lb['text'] =   self.valor_aposta
            if ficha == 50:
                self.valor_aposta = self.valor_aposta + 50
                self.saldo_carteira = self.saldo_carteira - 50
                self.saldo_carteira_lb['text'] =   self.saldo_carteira
                self.valor_aposta_lb['text'] =   self.valor_aposta
            if ficha == 100:
                self.valor_aposta = self.valor_aposta + 100
                self.saldo_carteira = self.saldo_carteira - 100
                self.saldo_carteira_lb['text'] =   self.saldo_carteira
                self.valor_aposta_lb['text'] =   self.valor_aposta
        else:
            self.mostra_temporizado(0.5,self.lbAlerta_quantia,1000,400,690,450)# alerta não deixa apostar essa quantia

    def reiniciarCarteira(self):
        """Este método serve para resetar o valor da carteira para o valor inicial"""
        self.saldo_carteira = 250
        self.valor_aposta_lb.place(x=1000, y=230)

    def Ok(self):
        """Este metodo serve para chamar esconder as fichas de aposta e iniciar uma partida do game"""
        if self.valor_aposta>0:
            self.aposta_status("fechado")
            self.play()
        else:
            self.mostra_temporizado(0.5,self.lbAlerta_aposta,1000,400,680,450)# alerta valor aposta invalido

    def novaPartida(self):
        """Este metodo serve para Configurar uma nova partida limpando a tela sem alterar o valor da carteira."""
        self.zeraLimpa()
        self.valor_aposta = 00
        self.valor_aposta_lb['text'] =   self.valor_aposta
        self.aposta_status("aberto")
        self.reinicio['image'] = ""
        self.inicio['image'] = ""
        self.reinicio.place(x=1000, y=200)
        self.inicio.place(x=1000, y=200)

    def estadoBtn(self,est):
        """Este metodo serve para esconder/mostrar os botoes D(descer carta) e P(parar de comprar) """
        if est == "ativa":
            self.btnDescer['image'] = self.imgbtnD
            self.btnParar['image'] = self.imgbtnP
            self.btnParar.place(x=550, y=510)
            self.btnDescer.place(x=655, y=510)
        else:
            self.btnDescer['image'] = ''
            self.btnParar['image'] = ''
            self.btnParar.place(x=1000, y=200)
            self.btnDescer.place(x=1000, y=200)

    def cancelar_aposta(self):
        """Este método serve para cancelar uma aposta que foi efetuada.Este método devolve o valor da aposta para a carteira."""
        self.saldo_carteira = self.saldo_carteira + self.valor_aposta
        self.saldo_carteira_lb['text'] = self.saldo_carteira
        self.valor_aposta = 00
        self.valor_aposta_lb['text'] = self.valor_aposta

    def tiralogo(self):
        """este metodo retira a logo do centro da tela"""
        self.logo['image'] = ''
        self.logo.place(x=1000, y=200)

    def zeraLimpa(self):
        """Este metodo serve para ser chamado por outros metodos quando precisar zerar uma partida e limpar o centro da tela"""
        self.zerarPartida()
        self.limpaMeio()

    def desvira(self):
        """este metodo serve para desvirar a carta da máquina que inicialmente está virada para baixo"""
        self.img2['file'] = self.urlDesvira
        self.m2.place(x=443, y=30)

    def limpaMeio(self):
        """este metodo reconfigura o centro do jogo limpando tudo que é resultado de uma partida."""
        self.mPer['image'] = self.imgPer
        self.mperfil['image'] = self.imgperfil
        self.medalha['image'] = ''
        self.perdeuimg['image'] = ''
        self.empateimg['image'] = ''
        self.lbMaquina['text'] = ''
        self.lbJogador['text'] = ''
        self.logo['image'] = self.imglogo
        self.logo.place(x=340, y=240)
        self.medalha.place(x=1000, y=200)
        self.perdeuimg.place(x=1000, y=200)
        self.empateimg.place(x=1000, y=200)
        self.m.place(x=350, y=30)
        self.m2.place(x=443, y=30)
        self.m3.place(x=350, y=460)
        self.m4.place(x=443, y=460)
        self.img1['file'] = r"imagem/cartasSlot.png"
        self.img2['file'] = r"imagem/cartasSlot.png"
        self.img3['file'] = r"imagem/cartasSlot.png"
        self.img4['file'] = r"imagem/cartasSlot.png"
        self.imag1.place(x=1000, y=400)
        self.imag2.place(x=1000, y=400)
        self.imag3.place(x=1000, y=400)
        self.imag4.place(x=1000, y=400)
        self.imag5.place(x=1000, y=400)
        self.imag6.place(x=1000, y=450)
        self.imag7.place(x=1000, y=450)
        self.imag8.place(x=1000, y=450)
        self.imag9.place(x=1000, y=450)
        self.imag10.place(x=1000, y=450)
        self.resultadoTela("não")

    def zerarPartida(self):
        """este metodo zera uma partida e serve para ser chamado junto com outros metodos de configuração de tela"""
        self.valorMaquina = 0
        self.valorJogador = 0
        self.bara.baralho = []
        self.bara.pilha.topo = None
        self.cartasJogador = []
        self.cartasMaquina = []
        self.qtdCartasJogador = 2
        self.qtdCartasMaquina = 2

    def resultadoTela(self,s):
        """este metodo serve para mostrar o resultado do maquina/jogador no centro da tela"""
        if s == 'sim':
            self.lbResultadoMaquina.place(x=360, y=160)
            self.lbPontuacaoMaquina.place(x=472, y=168)
            self.lbResultadoJogador.place(x=360, y=410)
            self.lbPontuacaoJogador.place(x=472, y=418)
            self.lbResultadoMaquina['image'] = self.pontoMaquina
            self.lbResultadoJogador['image'] = self.pontoJogador
            self.lbPontuacaoMaquina['text'] = self.valorMaquina
            self.lbPontuacaoJogador['text'] = self.valorJogador
        else:
            self.lbPontuacaoMaquina['text'] = ""
            self.lbPontuacaoJogador['text'] = ""
            self.lbPontuacaoMaquina.place(x=1000, y=650)
            self.lbPontuacaoJogador.place(x=1000, y=650)
            self.lbResultadoJogador['image'] = ''
            self.lbResultadoMaquina['image'] = ''

    def imprimir_ranking(self):
        """este metodo serve para retornar uma string com os nomes e pontuação que aparecerão no ranking"""
        return self.r.retorna_ranking()

    def inserir_no_ranking(self,score):
        """este metodo adiciona o usuario do game ao ranking"""
        self.r.add_record(self.user, int(score))

    def empatou(self):
        """Este metodo serve para mostrar a mensagem de - empate."""
        self.saldo_carteira = self.saldo_carteira + self.valor_aposta
        self.saldo_carteira_lb['text'] =   self.saldo_carteira
        self.reinicio['image'] = self.reinicioimg
        self.reinicio.place(x=748, y=500)
        self.mPer['image']=self.img_olho_cima_empatou
        self.estadoBtn("desativa")
        self.perdeuSom()
        self.tiralogo()
        self.resultadoTela("sim")
        self.lbJogador['text'] = ''
        self.lbMaquina['text'] = ''
        self.logo['image'] = ''
        self.empateimg['image'] = self.imgEmpate
        self.empateimg.place(x=330, y=220)
        self.logo.place(x=1000, y=200)
        self.ranking['text'] = self.imprimir_ranking()
        self.ranking.place(x=25, y=43)

    def ganhou(self):
        """Este metodo serve para mostrar a mensagem de - ganhou partida."""
        self.saldo_carteira = self.saldo_carteira + (self.valor_aposta * 3)
        self.saldo_carteira_lb['text'] =   self.saldo_carteira
        self.reinicio['image'] = self.reinicioimg
        self.reinicio.place(x=748, y=500)
        self.mPer['image'] = self.img_olho_cima_ganhou
        self.mperfil['image'] = self.img_olho_perdeu
        self.estadoBtn("desativa")
        self.ganhouSom()
        self.tiralogo()
        self.resultadoTela("sim")
        self.lbJogador['text'] = ''
        self.lbMaquina['text'] = ''
        self.logo['image'] = ''
        self.medalha['image'] = self.imgMedalha
        self.medalha.place(x=330, y=220)
        self.logo.place(x=1000, y=200)
        self.inserir_no_ranking(self.saldo_carteira)
        self.ranking['text'] = self.imprimir_ranking()
        self.ranking.place(x=25, y=43)

    def perdeu(self):
        """Este metodo serve para mostrar a mensagem de - perdeu partida."""
        self.saldo_carteira_lb['text'] =   self.saldo_carteira
        self.reinicio['image'] = self.reinicioimg
        self.reinicio.place(x=748, y=500)
        self.mPer['image'] = self.img_olho_cima_perdeu
        self.mperfil['image'] = self.img_olho_ganhou
        self.estadoBtn("desativa")
        self.perdeuSom()
        self.tiralogo()
        self.resultadoTela("sim")
        self.lbJogador['text'] = ''
        self.lbMaquina['text'] = ''
        self.logo['image'] = ''
        self.perdeuimg['image'] = self.imgPerdeu
        self.perdeuimg.place(x=330, y=220)
        self.logo.place(x=1000, y=200)
        self.ranking['text'] = self.imprimir_ranking()
        self.ranking.place(x=25, y=43)


    def play(self):
        """Este metodo serve para ser chamado quando precisar iniciar uma nova partida, e deve ser chamado por outros métodos"""
        self.ranking['text'] = self.imprimir_ranking()
        self.ranking.place(x=25, y=43)
        self.rank['image'] = self.imgrank
        self.zeraLimpa()
        self.jogar()
        self.estadoBtn("ativa")
        self.inicio['image'] = ''
        self.logo['image'] = self.imglogo
        self.medalha['image'] = ''
        self.medalha.place(x=1000, y=200)
        self.perdeuimg['image'] = ''
        self.perdeuimg.place(x=1000, y=200)
        self.inicio.place(x=1000, y=200)
        self.logo.place(x=340, y=240)
        self.reinicio.place(x=748, y=500)

    def EmbaralharSom(self):
        """Este metodo serve para tocar o som de - embaralhamento de cartas"""
        mixer.music.load('sounds/emb3.wav')  # embaralhar
        mixer.music.play()

    def perdeuSom(self):
        """Este metodo serve para tocar o som de - perdeu"""
        mixer.music.load('sounds/uhoh.mp3')  # perdeu
        mixer.music.play()

    def ganhouSom(self):
        """Este metodo serve para tocar o som de - ganhou"""
        mixer.music.load('sounds/ganhou.mp3')  # ganhou
        mixer.music.play()

    def puxacartaSom(self):
        """Este metodo serve para tocar o som de - compra de carta"""
        mixer.music.load('sounds/DEAL1.wav')  # puxando carta
        mixer.music.play()

    def cliqueMoeda(self):
        """Este método serve para tocar o som de - clique ao pressionar uma ficha de aposta"""
        mixer.music.load('sounds/moeda2.wav') # clique
        mixer.music.play()

    def adicionaCartaSlot(self,jogador, url):
        """Este metodo serve para sobrepor as cartas que o jogador/maquina compra uma do lado da outra na tela de jogo."""
        if jogador == "jogador":
            self.m3.place(x=320, y=460)
            self.m4.place(x=350, y=460)
            self.qtdCartasJogador = self.qtdCartasJogador + 1
            if self.qtdCartasJogador == 3:
                self.imag1Carta['file'] = url
                self.imag1.place(x=380, y=460)
            elif self.qtdCartasJogador == 4:
                self.imag2Carta['file'] = url
                self.imag2.place(x=410, y=460)
            elif self.qtdCartasJogador == 5:
                self.imag3Carta['file'] = url
                self.imag3.place(x=440, y=460)
            elif self.qtdCartasJogador == 6:
                self.imag4Carta['file'] = url
                self.imag4.place(x=470, y=460)
            elif self.qtdCartasJogador == 7:
                self.imag5Carta['file'] = url
                self.imag5.place(x=500, y=460)
        else:
            self.m.place(x=320, y=30)
            self.img2['file'] = self.urlDesvira
            self.m2.place(x=350, y=30)

            self.qtdCartasMaquina = self.qtdCartasMaquina + 1
            if self.qtdCartasMaquina == 3:
                self.imag6Carta['file'] = url
                self.imag6.place(x=380, y=30)

            elif self.qtdCartasMaquina == 4:
                self.imag7Carta['file'] = url
                self.imag7.place(x=410, y=30)

            elif self.qtdCartasMaquina == 5:
                self.imag8Carta['file'] = url
                self.imag8.place(x=440, y=30)

            elif self.qtdCartasMaquina == 6:
                self.imag9Carta['file'] = url
                self.imag9.place(x=470, y=30)

            elif self.qtdCartasMaquina == 7:
                self.imag10Carta['file'] = url
                self.imag10.place(x=500, y=30)

    def puxarcarta(self):
        """Este metodo serve para a compra de mais cartas- botão (comprar)."""
        self.mPer['image'] = self.img_olho_virado
        self.puxacartaSom()
        self.cartasJogador.append(self.bara.topo_da_pilha())
        url1 = self.criaString(self.descobreCarta(self.cartasJogador))
        self.adicionaCartaSlot("jogador", url1)
        jogador = self.Trata(self.cartasJogador)
        self.valorJogador = self.placarGeral(jogador)
        self.lbJogador['text'] = self.valorJogador

        if self.valorJogador > 21:
            if self.valorMaquina>21:
                self.empatou()
                self.desvira()
                self.zerarPartida()
                self.lbJogador['text'] = ''
                self.lbMaquina['text'] = ''
            else:
                self.perdeu()
                #1-perdeu@ MAQUINA VALOR MENOR QUE 21
                self.desvira()
                self.zerarPartida()
                self.lbJogador['text'] = ''
                self.lbMaquina['text'] = ''
                if self.saldo_carteira < 1:
                    messagebox.showinfo("Que pena!" ,"Perdeu tudo!")
                    self.voltar()

    def pararcarta(self):
        """Este metodo serve para a maquina decidir se compra ou não mais cartas, se ela decidir comprar então esta ação é feita."""
        if self.valorJogador == self.valorMaquina:
            self.empatou()
            self.desvira()
            #ESPECIAL#-maquina empatou pois os valores eram iguais NO INICIO
            self.zerarPartida()
        elif self.valorJogador > 21:
            self.perdeu()
            self.desvira()
            # especial2 - MAQUINA TINHA VALOR ABAIXO DE 21 E JOGADOR 22. DE CARA.azar MAIOR
            self.zerarPartida()
            if self.saldo_carteira < 1:
                messagebox.showinfo("Que pena!", "Perdeu tudo!")
                self.voltar()

        elif self.valorMaquina > 21:
            self.ganhou()
            self.desvira()
            #- especial - Maquina iniciou com 22 de cara: sorte...
            self.zerarPartida()
        elif self.valorMaquina > self.valorJogador:
            self.perdeu()
            self.desvira()
            #2-perdeu, maquina tinha valor maior!
            self.zerarPartida()
            if self.saldo_carteira < 1:
                messagebox.showinfo("Que pena!", "Perdeu tudo!")#ALERTA PERDEU TUDO.
                self.voltar()

        else:
            # maquina joga!@
            while (self.valorMaquina < self.valorJogador):
                self.cartasMaquina.append(self.bara.topo_da_pilha())
                url2 = self.criaString(self.descobreCarta(self.cartasMaquina))
                self.adicionaCartaSlot("maquina", url2)
                maquina = self.Trata(self.cartasMaquina)
                self.valorMaquina = self.placarGeral(maquina)
                self.lbMaquina['text'] = self.valorMaquina

            if self.valorMaquina == self.valorJogador:
                self.empatou()
                #empate! maquina decidiu empatar com vc!
                self.zerarPartida()
            elif self.valorMaquina > 21:
                self.ganhou()
                #ganhou! maquina estourou valor!
                self.zerarPartida()
            elif self.valorMaquina == 21:
                self.perdeu()
                #perdeu, maquina fez exatamente21!
                self.zerarPartida()
                if self.saldo_carteira < 1:
                    messagebox.showinfo("Que pena!" ,"Perdeu tudo!")#ALERTA PERDEU TUDO.
                    self.voltar()

            else:
                self.perdeu()
                #2-perdeu! maquina venceu abaixo de 21!
                self.zerarPartida()
                if self.saldo_carteira < 1:
                    messagebox.showinfo("Que pena!" ,"Perdeu tudo!")# ALERTA PERDEU TUDO.
                    self.voltar()

    def voltar(self):
        """Este metodo serve para fechar a janela do jogo blackjack E RETORNAR PARA A JANELA PRINCIPAL DO GAME."""
        pygame.quit()
        self.janela.destroy()

    def placarGeral(self,v):
        """Este metodo serve para somar o valor das cartas da maquina ou do jogador"""
        t = ''
        soma = 0
        for i in range(len(v)):
            soma = soma + v[i]
            t = t + str(v[i]) + ", "
        #("jogador ou maquina " + t + " PTs: " + str(soma)) esta string mostra o valor nos vetores. usada apenas em debugs
        return soma

    def Trata(self,cartas):
        """Este metodo serve para tratar a matriz que contém as cartas e retornar apenas um vetor com o valor das cartas do jogador/maquina"""
        vet = []
        for i in range(len(cartas)):
            carM = 0
            carM = int(cartas[i][0])
            vet.append(carM)
        return vet

    def criaString(self,entrada):
        """Este metodo serve para criar a string de URL(caminho) que será passada na hora de chamar a m_principal de alguma carta"""
        s = "imagem/Baralho\ " + str(entrada) + ".png"
        return s.replace(" ", "")

    def descobreCarta(self,mat):
        """Este metodo serve para retornar o nome da ultima carta comprada."""
        ultima = mat[-1]
        valor = ''
        valor = ultima[1] + ultima[2][0]
        return valor

    def jogar(self):
        """Este metodo serve para iniciar uma partida entre jogador/maquina."""
        self.EmbaralharSom()
        urlFechada = r"imagem/cartafechada.png"
        self.cartasMaquina = []
        self.cartasJogador = []
        self.valorJogador = 0
        self.valorMaquina = 0

        self.bara.gerar_baralho() # gerando baralho
        self.bara.pilha_embaralhar() #Embaralhando as cartas.

        self.cartasMaquina.append(self.bara.topo_da_pilha())#apendando na lista cartasMaquina o topo da Pilha
        url1 = self.criaString(self.descobreCarta(self.cartasMaquina))

        self.cartasJogador.append(self.bara.topo_da_pilha())
        url3 = self.criaString(self.descobreCarta(self.cartasJogador))

        self.cartasMaquina.append(self.bara.topo_da_pilha())
        # este não possui URL pois esta carta esta virada para baixo.
        self.urlDesvira = self.criaString(self.descobreCarta(self.cartasMaquina))
        # a url foi criada para desvirar esta carta no futuro. e fica salva numa global.

        self.cartasJogador.append(self.bara.topo_da_pilha()) # Appendando na lista cartasJogador o topo da Pilha.
        url4 = self.criaString(self.descobreCarta(self.cartasJogador))
        self.img1['file'] = url1
        self.img2['file'] = urlFechada
        self.img3['file'] = url3
        self.img4['file'] = url4

        maquina = self.Trata(self.cartasMaquina) #TRATANDO OS VALORES DA MAQUINA
        jogador = self.Trata(self.cartasJogador) #TRANADO OS VALORES DO JOGADOR

        self.valorMaquina = self.placarGeral(maquina) #DESCOBRINDO O VALOR DA PONTUAÇÃO.
        self.valorJogador = self.placarGeral(jogador)
        self.lbMaquina['text'] = maquina[0]
        self.lbJogador['text'] = self.valorJogador
