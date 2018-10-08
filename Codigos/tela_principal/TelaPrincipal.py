from tkinter import *


def abre_blackjack():
    pass
def abre_megastacker():
    pass
def abre_slotmachine():
    pass

telaprincipal = Tk()

tridir=Label(telaprincipal)
imgdir=PhotoImage(file="image/trinagulodireita.png")
tridir['image']=imgdir
tridir['bg']="#000080"
tridir.place(x=570,y=-8)

logo=Label(telaprincipal)
imglogo=PhotoImage(file="image/logomeio.png")
logo['image']=imglogo
logo['bg']="#000080"
logo.place(x=300,y=10)

lb_apelido=Label(telaprincipal)
imgapelido=PhotoImage(file="image/lb_apelido.png")
lb_apelido['image']=imgapelido
lb_apelido['bg']="#000080"
lb_apelido.place(x=375,y=225)

lb_caixa=Label(telaprincipal)
imgacx=PhotoImage(file="image/entr_name.png")
lb_caixa['image']=imgacx
lb_caixa['bg']="#000080"
lb_caixa.place(x=300,y=265)

cx_nome=Entry(telaprincipal)
cx_nome['font'] = 'sans', 19, "bold"
cx_nome['bg'] = "#C8AB37"
cx_nome['relief']=FLAT
cx_nome['width']=12
cx_nome.place(x=366,y=270)

btnM=Button(telaprincipal)
btnM['bg']="#000080"
btnM['relief']=FLAT
imgM=PhotoImage(file="image/playMegastacker.png")
btnM['image']=imgM

btnB=Button(telaprincipal)
btnB['bg']="#000080"
btnB['relief']=FLAT
imgB=PhotoImage(file="image/playBlackjack.png")
btnB['image']=imgB

btnS=Button(telaprincipal)
btnS['bg']="#000080"
btnS['relief']=FLAT
imgS=PhotoImage(file="image/playSlotmachine.png")
btnS['image']=imgS

btnM.place(x=2,y=380)
btnB.place(x=302,y=380)
btnS.place(x=602,y=380)

telaprincipal['bg'] = "#000080"
telaprincipal.title("G'nus Cassinos")
#telaprincipal.iconbitmap("image/logoSistema.ico")
telaprincipal.resizable(0, 0)
x = (telaprincipal.winfo_screenwidth() // 2) - (910 // 2)
y = (telaprincipal.winfo_screenheight() // 2) - (600 // 2)
telaprincipal.geometry("910x600+{}+{}".format(x, y))  # largura x altura + esquerda + topo
# telaprincipal.overrideredirect(True)#retira bordas
telaprincipal.mainloop()
