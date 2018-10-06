from tkinter import *
from pygame import mixer

janela = Tk()

logo=Label(janela)
imglogo=PhotoImage(file="logomeio.png")
logo['image']=imglogo
logo['bg']="#006400"
logo.place(x=300,y=10)

lb_apelido=Label(janela)
imgapelido=PhotoImage(file="lb_apelido.png")
lb_apelido['image']=imgapelido
lb_apelido['bg']="#006400"
lb_apelido.place(x=375,y=225)

lb_caixa=Label(janela)
imgacx=PhotoImage(file="entr_name.png")
lb_caixa['image']=imgacx
lb_caixa['bg']="#006400"
lb_caixa.place(x=300,y=265)


cx_nome=Entry(janela)
cx_nome['font'] = 'sans', 19, "bold"
cx_nome['bg'] = "#C8AB37"
cx_nome['relief']=FLAT
cx_nome['width']=12
#cx_nome['heigth']=2
cx_nome.place(x=366,y=270)




btnM=Button(janela)
btnM['bg']="#006400"
btnM['relief']=FLAT
imgM=PhotoImage(file="playMegastacker.png")
btnM['image']=imgM
btnB=Button(janela)
btnB['bg']="#006400"
btnB['relief']=FLAT
imgB=PhotoImage(file="playBlackjack.png")
btnB['image']=imgB
btnS=Button(janela)
btnS['bg']="#006400"
btnS['relief']=FLAT
imgS=PhotoImage(file="playSlotmachine.png")
btnS['image']=imgS

btnM.place(x=2,y=380)
btnB.place(x=302,y=380)
btnS.place(x=602,y=380)



janela['bg'] = "#006400"
janela.title("G'nus Cassinos")
janela.iconbitmap(r"Jogo21\image\logoSistema.ico")
janela.resizable(0, 0)
x = (janela.winfo_screenwidth() // 2) - (910 // 2)
y = (janela.winfo_screenheight() // 2) - (600 // 2)
janela.geometry("910x600+{}+{}".format(x, y))  # largura x altura + esquerda + topo
# janela.overrideredirect(True)#retira bordas
janela.mainloop()