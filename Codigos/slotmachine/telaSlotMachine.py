import threading
from tkinter import *
from pygame import mixer
import time
from Codigos.slotmachine.SlotMachine import SlotMachine

#TODO- VERIFICAR NO RANKING SE FOI TRATADO O NOME SLOTMACHINE E SE EXISTE PASTA COM RANKING DESTE JOGO NESTE PACKAGE.

class TelaSlotMachine:
    def __init__(self,user,janela,anterior):
        anterior.focus_displayof()  # desativa tela principal
        self.__user = user
        # criando frame desta janela e posicionando.
        self.janela = Frame(janela)
        self.janela['width'] = 910
        self.janela['height'] = 600
        self.janela['bg'] = "#006400"
        self.janela.place(x=0, y=0)
        # fim do frame tela principal do jogo.

        self.status = 0
        self.sm = SlotMachine()
        self.sm.spin()
        mixer.init()
        mixer.music.load(r'../slotmachine/sounds/DEAL1.wav')

        self.imglpdLigada = PhotoImage(file="../slotmachine/imagens/cacaniquel4.png")

        # fim lampadas
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

        self.btnExit = Button(self.janela)
        self.imgExit = PhotoImage(file="../slotmachine/imagens/exit.png")
        self.btnExit['image'] = self.imgExit
        self.btnExit['relief'] = FLAT
        self.btnExit['command'] = self.sair
        self.btnExit['bg'] = "#006400"
        self.btnExit.place(x=2, y=530)


    def sair(self):
        self.janela.destroy()

    def pin(self):
        mixer.music.play()

    def muda_alavanca(self,status):
        if status=="cima":
            #status e cima
            self.imgSpin.place(x=480, y=200)
            self.imgSP['file'] = r"../slotmachine/imagens/bracoCima.png"
            self.btnSpin.place(x=503, y=190)
            self.btnSpin['image']=self.imgbtnSpin
            self.b['image']=''
            self.b.place(x=0,y=0)
        else:
            #status e baixo
            self.imgSpin.place(x=480, y=291)
            self.imgSP['file'] = r"../slotmachine/imagens/bracoBaixo.png"
            self.btnSpin.place(x=0,y=0)
            self.btnSpin['image']=""
            self.b['image']=self.bImg
            self.b.place(x=503,y=390)


    def gira(self):
        threading.Timer(0.1, self.muda_meio).start()
        self.status=0
        # for magico da porra.25 é uma forma de fazer tempo junto com o time.sleep()0.090 la de baixo.
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
        for j in range(8):
            nome2 = str(self.sm.spin())
            self.img2['file'] = "../slotmachine/imagens/slots/" + nome2 + ".png"
            nome3 = str(self.sm.spin())
            self.img3['file'] = "../slotmachine/imagens/slots/" + nome3 + ".png"
            if j==7:
                self.pin()
            time.sleep(0.09)
        for k in range(6):
            nome3 = str(self.sm.spin())
            self.img3['file'] = "../slotmachine/imagens/slots/" + nome3 + ".png"
            if k==5:
                self.pin()
            time.sleep(0.09)

        print("gotcha parou")
        self.status=1
        self.muda_alavanca("cima")

    def sorteia(self):
        #muda_alavanca("meio")
        self.muda_alavanca("baixo")
        threading.Timer(0.1, self.gira).start()


    def muda_meio(self):
        while self.status!=1:
            self.cNiquel['image']=self.imgcNiquel
            time.sleep(0.2)
            self.cNiquel['image']=self.imglpdLigada
            time.sleep(0.2)
