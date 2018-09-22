import threading
from tkinter import *

import time
from SlotMachine import SlotMachine

sm = SlotMachine()


def s1():
    threading.Timer(0.2, sorteia).start()

    nome = str(sm.spin())
    img1['file'] = "imagens/slots/"+nome+".png"
    nome2 = str(sm.spin())
    img2['file'] = "imagens/slots/" + nome2 + ".png"
    nome3 = str(sm.spin())
    img3['file'] = "imagens/slots/" + nome3 + ".png"


def sorteia():
    s1()





# inicia tela
tela = Tk()
c=1

# Primeiro slot
imagem = Label(tela)
img1 = PhotoImage(file="imagens/user.png")
imagem['image'] = img1
imagem['bg'] = '#006400'
imagem.place(x=50, y=30)

# Segundo slot
imagem2 = Label(tela)
img2 = PhotoImage(file="imagens/user.png")
imagem2['image'] = img2
imagem2['bg'] = '#006400'
imagem2.place(x=200, y=30)

# Terceiro slot
imagem3 = Label(tela)
img3 = PhotoImage(file="imagens/user.png")
imagem3['image'] = img3
imagem3['bg'] = '#006400'
imagem3.place(x=350, y=30)

# Botão de spin
btnSpin=Button(tela)
btnSpin['bg']='#006400'
btnSpin['relief']=FLAT
btnSpin['command']= sorteia
imgbtnP=PhotoImage(file=r"imagens\btnP.png")
btnSpin['image']=imgbtnP
btnSpin.place(x=240, y=200)
#fim botao parar

# Conigurações da janela
tela.title("G'nus Slot Machine") # titulo da janela
tela.iconbitmap(r"imagens\logoSistema.ico")# icone do programa
tela['bg'] = "#006400" # Background color
tela.resizable(0,0) # seta a janela com tamanho fixo
x = (tela.winfo_screenwidth() // 2) - (500 // 2) # Pega o valor X do ponto central
y = (tela.winfo_screenheight() // 2) - (300 // 2) # Pega o valor Y do ponto central
tela.geometry("500x300+{}+{}".format(x, y))  # largura x altura + esquerda + topo
tela.mainloop() # mantem a tela aberta