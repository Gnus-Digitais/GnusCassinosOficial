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

def muda_alavanca(status):
    if status=="cima":
        #status e cima
        imgSpin.place(x=480, y=200)
        imgSP['file'] = r"imagens/bracoCima.png"
        btnSpin.place(x=503, y=190)
        btnSpin['image']=imgbtnSpin
        b['image']=''
        b.place(x=0,y=0)
    else:
        #status e baixo
        imgSpin.place(x=480, y=291)
        imgSP['file'] = r"imagens/bracoBaixo.png"
        btnSpin.place(x=0,y=0)
        btnSpin['image']=""
        b['image']=bImg
        b.place(x=503,y=390)


def gira():
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
    muda_alavanca("cima")

def sorteia():
    #muda_alavanca("meio")
    muda_alavanca("baixo")
    threading.Timer(0.1, gira).start()


# inicia tela
tela = Tk()
c=1

#caça niquel logo !
cNiquel=Label(tela)
imgcNiquel=PhotoImage(file="imagens/cacaniquel2.png")
cNiquel['image']=imgcNiquel
cNiquel['bg']="#006400"
cNiquel.place(x=180,y=30)
#fim caça niquel logo !

# Primeiro slot
imagem = Label(tela)
img1 = PhotoImage(file="imagens/gnu.png")
imagem['image'] = img1
imagem['bg'] = '#fff'
imagem.place(x=230, y=280)

# Segundo slot
imagem2 = Label(tela)
img2 = PhotoImage(file="imagens/gnu.png")
imagem2['image'] = img2
imagem2['bg'] = '#fff'
imagem2.place(x=305, y=280)

# Terceiro slot
imagem3 = Label(tela)
img3 = PhotoImage(file="imagens/gnu.png")
imagem3['image'] = img3
imagem3['bg'] = '#fff'
imagem3.place(x=380, y=280)


#braco do spin button
imgSpin=Label(tela)
imgSpin['bg']="#006400"
imgSP=PhotoImage(file=r"imagens/bracoCima.png")
imgSpin['image']=imgSP
imgSpin.place(x=480,y=200)
#fim braco spin button

# Botão de spin
btnSpin=Button(tela)
btnSpin['bg']='#006400'
btnSpin['relief']=FLAT
btnSpin['command']= sorteia
imgbtnSpin=PhotoImage(file=r"imagens\btnSpin.png")
btnSpin['image']=imgbtnSpin
btnSpin.place(x=503, y=190)
#fim botao spin
#bolinha inicio
b=Label(tela)
b['bg']='#006400'
bImg=PhotoImage(file=r"imagens\Bolinha.png")
b['image']=bImg
#bolinha fim

# Conigurações da janela
tela.title("G'nus Slot Machine") # titulo da janela
tela.iconbitmap(r"imagens\logoSistema.ico")# icone do programa
tela['bg'] = "#006400" # Background color
tela.resizable(0,0) # seta a janela com tamanho fixo
x = (tela.winfo_screenwidth() // 2) - (700 // 2) # Pega o valor X do ponto central
y = (tela.winfo_screenheight() // 2) - (550 // 2) # Pega o valor Y do ponto central
tela.geometry("700x550+{}+{}".format(x, y))  # largura x altura + esquerda + topo
tela.mainloop() # mantem a tela aberta