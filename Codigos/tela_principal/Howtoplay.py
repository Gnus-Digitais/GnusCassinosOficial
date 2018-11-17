from tkinter import *

class Howtoplay:
    """Classe how-to-play, onde todos os how-to-plays estão."""
    def __init__(self,tela,jogo):
        self.tela=tela
        self.jogo=jogo

        self.principal = Frame(self.tela)
        self.principal['width'] = 910
        self.principal['height'] = 600
        self.principal['bg'] = "#000080"
        self.principal.place(x=0, y=0)

        self.tela_principal=PhotoImage(file="imagem/howtoplayprincipal.png")
        self.megastacker=PhotoImage(file="imagem/howtoplaymegastacker.png")
        self.blackjack=PhotoImage(file="imagem/howtoplayblackjack.png")
        self.slotmachine=PhotoImage(file="imagem/howtoplayslotmachine.png")


        self.howtoplay = Label(self.principal)
        self.howtoplay['bg'] = "#000080"
        self.howtoplay.place(x=0,y=0)

        #esta parte do código verifica se o atributo self.jogo é o nome de uma das outras telas.
        #caso seja, ele abre o how-to-play da tela selecionada.

        if self.jogo=="tela_principal":
            self.howtoplay['image']=self.tela_principal
            self.howtoplay.place(x=90,y=20)

        elif self.jogo=="blackjack":
            self.howtoplay['image']=self.blackjack
            self.howtoplay.place(x=90, y=20)
        else:
            self.howtoplay['image']=self.slotmachine
            self.howtoplay.place(x=90, y=20)

        self.btnVoltar = Button(self.principal)
        self.imgbtnvoltar = PhotoImage(file="imagem/voltar2.png")
        self.btnVoltar['image']=self.imgbtnvoltar
        self.btnVoltar['bg']="#000080"
        self.btnVoltar['command']=self.voltar
        self.btnVoltar['relief']=FLAT
        self.btnVoltar.place(x=2,y=530)

    def voltar(self):
        """Este método retorna para tela principal, destruindo o frame que está aberto."""
        self.principal.destroy()
