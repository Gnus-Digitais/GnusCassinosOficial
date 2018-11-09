from tkinter import *
from Codigos.tela_principal.Jogo import Jogo


tela = Tk()
tela['bg']="#000080"
tela.title("G'nus Cassinos")
tela.resizable(0, 0)
tela.iconbitmap("imagem\logoicone3.ico")
x = (tela.winfo_screenwidth() // 2) - (910 // 2)
y = (tela.winfo_screenheight() // 2) - (600 // 2)
tela.geometry("910x600+{}+{}".format(x, y))  # largura x altura + esquerda + topo
# telaprincipal.overrideredirect(True)#retira bordas
Jogo(tela)
tela.mainloop()
