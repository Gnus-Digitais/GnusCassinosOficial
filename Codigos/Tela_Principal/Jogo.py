from tkinter import *
class Jogo:
    def __init__(self,tela):
        self.tela=tela
        '''
        self.tridir=Label(self.tela)
        self.imgdir=PhotoImage(file="trinagulodireita.png")
        self.tridir['image']=self.imgdir
        self.tridir['bg']="#000080"
        self.tridir.place(x=570,y=-8)
        '''
        self.logo=Label(self.tela)
        self.imglogo=PhotoImage(file="logomeio.png")
        self.logo['image']=self.imglogo
        self.logo['bg']="#000080"
        self.logo.place(x=300,y=10)
        '''
        self.lb_apelido=Label(self.tela)
        self.imgapelido=PhotoImage(file="lb_apelido.png")
        self.lb_apelido['image']=self.imgapelido
        self.lb_apelido['bg']="#000080"
        self.lb_apelido.place(x=375,y=225)

        self.lb_caixa=Label(self.tela)
        self.imgacx=PhotoImage(file="entr_name.png")
        self.lb_caixa['image']=self.imgacx
        self.lb_caixa['bg']="#000080"
        self.lb_caixa.place(x=300,y=265)

        self.cx_nome=Entry(self.tela)
        self.cx_nome['font'] = 'sans', 19, "bold"
        self.cx_nome['bg'] = "#C8AB37"
        self.cx_nome['relief']=FLAT
        self.cx_nome['width']=12
        self.cx_nome.place(x=366,y=270)

        self.btnM=Button(self.tela)
        self.btnM['relief']=FLAT
        self.imgM=PhotoImage(file="playMegastacker.png")
        self.btnM['image']=self.imgM
        self.btnM['bg'] = "#000080"
        self.btnM.place(x=2, y=380)

        self.btnB=Button(self.tela)
        self.btnB['relief']=FLAT
        self.imgB=PhotoImage(file="playBlackjack.png")
        self.btnB['image']=self.imgB
        self.btnB['bg'] = "#000080"
        self.btnB.place(x=302, y=380)

        self.btnS=Button(self.tela)
        self.btnS['relief']=FLAT
        self.imgS=PhotoImage(file="playSlotmachine.png")
        self.btnS['image']=self.imgS
        self.btnS['bg'] = "#000080"
        self.btnS.place(x=602,y=380)
        '''


tela = Tk()
Jogo(tela)
tela['bg']="#000080"
tela.title("G'nus Cassinos")
#telaa.iconbitmap("Jogo21\image\logoSistema.ico")
tela.resizable(0, 0)
x = (tela.winfo_screenwidth() // 2) - (910 // 2)
y = (tela.winfo_screenheight() // 2) - (600 // 2)
tela.geometry("910x600+{}+{}".format(x, y))  # largura x altura + esquerda + topo
# telaprincipal.overrideredirect(True)#retira bordas

tela.mainloop()

