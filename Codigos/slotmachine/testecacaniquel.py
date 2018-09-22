import threading
from tkinter import *
from pygame import mixer
import time
from SlotMachine import SlotMachine

sm = SlotMachine()

def pin():
    mixer.init()
    mixer.music.load(r'sounds/DEAL1.wav')
    mixer.music.play()
def s1():
    # for magico da porra.25 é uma forma de fazer tempo junto com o time.sleep()0.090 la de baixo.
    for i in range(25):
        nome = str(sm.spin())
        img1['file'] = "imagens/slots/"+nome+".png"
        nome2 = str(sm.spin())
        img2['file'] = "imagens/slots/" + nome2 + ".png"
        nome3 = str(sm.spin())
        img3['file'] = "imagens/slots/" + nome3 + ".png"
        if i==22:
            pin()
        time.sleep(0.090)
    for j in range(8):
        nome2 = str(sm.spin())
        img2['file'] = "imagens/slots/" + nome2 + ".png"
        nome3 = str(sm.spin())
        img3['file'] = "imagens/slots/" + nome3 + ".png"
        if j==7:
            pin()
        time.sleep(0.090)
    for k in range(6):
        nome3 = str(sm.spin())
        img3['file'] = "imagens/slots/" + nome3 + ".png"
        if k==5:
            pin()
        time.sleep(0.090)

    print("gotcha parou")

def sorteia():
    threading.Timer(0.1, s1).start()


# inicia tela
tela = Tk()
c=1

#caça niquel logo !
cNiquel=Label(tela)
imgcNiquel=PhotoImage(file="imagens/cacaniquel.png")
cNiquel['image']=imgcNiquel
cNiquel['bg']="#006400"
cNiquel.place(x=180,y=30)
#fim caça niquel logo !

# Primeiro slot
imagem = Label(tela)
img1 = PhotoImage(file="imagens/gnu.png")
imagem['image'] = img1
imagem['bg'] = '#fff'
imagem.place(x=240, y=255)

# Segundo slot
imagem2 = Label(tela)
img2 = PhotoImage(file="imagens/gnu.png")
imagem2['image'] = img2
imagem2['bg'] = '#fff'
imagem2.place(x=321, y=255)

# Terceiro slot
imagem3 = Label(tela)
img3 = PhotoImage(file="imagens/gnu.png")
imagem3['image'] = img3
imagem3['bg'] = '#fff'
imagem3.place(x=402, y=255)


#braco do spin button
imgSpin=Label(tela)
imgSpin['bg']="#006400"
imgSP=PhotoImage(file=r"imagens/bracoCima.png")
imgSpin['image']=imgSP
imgSpin.place(x=511,y=200)
#fim braco spin button

# Botão de spin
btnSpin=Button(tela)
btnSpin['bg']='#006400'
btnSpin['relief']=FLAT
btnSpin['command']= sorteia
imgbtnSpin=PhotoImage(file=r"imagens\btnSpin.png")
btnSpin['image']=imgbtnSpin
btnSpin.place(x=534, y=180)
#fim botao spin

# Conigurações da janela
tela.title("G'nus Slot Machine") # titulo da janela
tela.iconbitmap(r"imagens\logoSistema.ico")# icone do programa
tela['bg'] = "#006400" # Background color
tela.resizable(0,0) # seta a janela com tamanho fixo
x = (tela.winfo_screenwidth() // 2) - (700 // 2) # Pega o valor X do ponto central
y = (tela.winfo_screenheight() // 2) - (550 // 2) # Pega o valor Y do ponto central
tela.geometry("700x550+{}+{}".format(x, y))  # largura x altura + esquerda + topo
tela.mainloop() # mantem a tela aberta