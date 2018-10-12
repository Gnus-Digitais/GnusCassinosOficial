from Codigos.Jogo21.Telablackjack import Telablackjack
from Codigos.slotmachine.telaSlotMachine import TelaSlotMachine

from tkinter import *

class Jogo:
    """Classe principal JOGO, onde todos os jogos são abertos."""
    def __init__(self,tela):
        self.principal=Frame(tela)
        self.principal['width']=910
        self.principal['height']=600
        self.principal['bg']="#000080"
        self.principal.place(x=0,y=0)

        self.tridir=Label(self.principal)
        self.imgdir=PhotoImage(file="imagem/triangulodireita2.png")
        self.tridir['image']=self.imgdir
        self.tridir['bg']="#000080"
        self.tridir.place(x=570,y=-8)

        self.logo = Label(self.principal)
        self.imglogo = PhotoImage(file=r"imagem/logomeio.png")
        self.logo['image'] = self.imglogo
        self.logo['bg'] = "#000080"
        self.logo.place(x=300, y=10)

        self.lb_apelido=Label(self.principal)
        self.imgapelido=PhotoImage(file="imagem/lb_apelido.png")
        self.lb_apelido['image']=self.imgapelido
        self.lb_apelido['bg']="#000080"
        self.lb_apelido.place(x=375,y=225)

        self.lb_caixa=Label(self.principal)
        self.imgacx=PhotoImage(file="imagem/entr_name.png")
        self.lb_caixa['image']=self.imgacx
        self.lb_caixa['bg']="#000080"
        self.lb_caixa.place(x=300,y=265)

        self.cx_nome=Entry(self.principal)
        self.cx_nome['font'] = 'Courier New', 18, "bold" #sans
        self.cx_nome['fg']="#000080"
        self.cx_nome['bg'] = "#C8AB37"
        self.cx_nome['relief']=FLAT
        self.cx_nome['justify']=CENTER
        self.cx_nome['width']=12
        self.cx_nome.place(x=366,y=271)
        self.cx_nome.focus()

        self.btnM=Button(self.principal)
        self.btnM['relief']=FLAT
        self.imgM=PhotoImage(file="imagem/playMegastacker.png")
        self.btnM['image']=self.imgM
        self.btnM['bg'] = "#000080"
        self.btnM.place(x=2, y=380)

        self.btnB=Button(self.principal)
        self.btnB['relief']=FLAT
        self.imgB=PhotoImage(file="imagem/playBlackjack.png")
        self.btnB['image']=self.imgB
        self.btnB['bg'] = "#000080"
        self.btnB['command']=self.abre_blackjack
        self.btnB.place(x=302, y=380)

        self.btnS=Button(self.principal)
        self.btnS['relief']=FLAT
        self.imgS=PhotoImage(file="imagem/playSlotmachine.png")
        self.btnS['image']=self.imgS
        self.btnS['bg'] = "#000080"
        self.btnS['command'] = self.abre_slotmachine
        self.btnS.place(x=602,y=380)

        self.btnExit=Button(self.principal)
        self.imgExit=PhotoImage(file="imagem/exit.png")
        self.btnExit['image']=self.imgExit
        self.btnExit['relief']=FLAT
        self.btnExit['command']=self.sair
        self.btnExit['bg']="#000080"
        self.btnExit.place(x=2,y=2)

    def trata_texto(self,texto):
        """Metodo que trata o nick do jogador e retorna o nick já tratado."""
        textoR = texto.strip()
        if len(textoR) <=2:
            return False
        elif (len(textoR)>2 and len(textoR)<=7):
            return textoR
        else:
            return textoR[0:7]

    def sair(self):
        """metodo que fecha a tela principal do jogo."""
        tela.destroy()

    def abre_blackjack(self):
        """Metodo que abre a tela BlackJack, passando como parametro o nome do jogador, tela mãe e tela atual"""
        usuario=self.cx_nome.get()
        nome=self.trata_texto(usuario)
        if nome !=False:
            Telablackjack(nome,tela,self.principal)#todo - aparentemente ok.
        else:
            print("sem texto no campo.")#todo- bloqueio ao entrar em tela de jogo.

    def abre_slotmachine(self):
        """Metodo que abre a tela SLOTMACHINE, passando como parametro o nome do jogador, tela mãe e tela atual"""
        usuario = self.cx_nome.get()
        nome = self.trata_texto(usuario)
        if nome != False:
            TelaSlotMachine(nome, tela, self.principal)  # todo - aparentemente ok.
        else:
            print("sem texto no campo.")  # todo- bloqueio ao entrar em tela de jogo.

    def abre_megastacker(self):
        usuario = self.cx_nome.get()  # todo - não ligado ainda-BRUNO...




tela = Tk()
tela['bg']="#000080"
tela.title("G'nus Cassinos")
tela.resizable(0, 0)
tela.iconbitmap("imagem\logoSistema.ico")
x = (tela.winfo_screenwidth() // 2) - (910 // 2)
y = (tela.winfo_screenheight() // 2) - (600 // 2)
tela.geometry("910x600+{}+{}".format(x, y))  # largura x altura + esquerda + topo
# telaprincipal.overrideredirect(True)#retira bordas
Jogo(tela)
tela.mainloop()

# TODO - REVISAR CÓDIGO TODO..!!!!!! - IGOR - MATHEUS - BRUNO(se quiser).