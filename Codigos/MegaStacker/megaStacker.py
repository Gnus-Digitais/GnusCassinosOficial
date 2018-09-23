import threading
from tkinter import *
import time
from functools import partial


def linha8():
    q70['image']=aqImg
    time.sleep(0.2)
    q71['image']=aqImg
    time.sleep(0.2)
    q72['image']=aqImg
    time.sleep(0.2)
    q73['image']=aqImg
    time.sleep(0.2)
    q74['image']=aqImg
    time.sleep(0.2)
    q74['image'] = vqImg
    time.sleep(0.2)
    q73['image'] = vqImg
    time.sleep(0.2)
    q72['image'] = vqImg
    time.sleep(0.2)
    q71['image'] = vqImg
    time.sleep(0.2)
    q70['image'] = vqImg
    time.sleep(0.2)
    chama()

def chama():
    threading.Timer(0.2,linha8).start()

def clique():
    print("clicou")

# inicia tela
tela = Tk()
mat=[['q00', 'q01', 'q02', 'q03', 'q04'], ['q10', 'q11', 'q12', 'q13', 'q14'], ['q20', 'q21', 'q22', 'q23', 'q24'], ['q30', 'q31', 'q32', 'q33', 'q34'], ['q40', 'q41', 'q42', 'q43', 'q44'], ['q50', 'q51', 'q52', 'q53', 'q54'], ['q60', 'q61', 'q62', 'q63', 'q64'], ['q70', 'q71', 'q72', 'q73', 'q74']]


maquina=Label(tela)
maqImg=PhotoImage(file=r"imagens/megaStacker.png")
maquina['image']=maqImg
maquina.place(x=260,y=40)
maquina['bg']="#006400"

#quadradinho vermelho
vqImg=PhotoImage(file=r"imagens/vq.png")
#fim quadradinho vermelho

#criando 40 quadradinhos vermelhos labels@@

q00=Label(tela)
q00['image']=vqImg
q00.place(x=282,y=102)
q00['bg']='#000'
q01=Label(tela)
q01['image']=vqImg
q01.place(x=331,y=102)
q01['bg']='#000'
q02=Label(tela)
q02['image']=vqImg
q02.place(x=380,y=102)
q02['bg']='#000'
q03=Label(tela)
q03['image']=vqImg
q03.place(x=429,y=102)
q03['bg']='#000'
q04=Label(tela)
q04['image']=vqImg
q04.place(x=478,y=102)
q04['bg']='#000'
q10=Label(tela)
q10['image']=vqImg
q10.place(x=282,y=151)
q10['bg']='#000'
q11=Label(tela)
q11['image']=vqImg
q11.place(x=331,y=151)
q11['bg']='#000'
q12=Label(tela)
q12['image']=vqImg
q12.place(x=380,y=151)
q12['bg']='#000'
q13=Label(tela)
q13['image']=vqImg
q13.place(x=429,y=151)
q13['bg']='#000'
q14=Label(tela)
q14['image']=vqImg
q14.place(x=478,y=151)
q14['bg']='#000'
q20=Label(tela)
q20['image']=vqImg
q20.place(x=282,y=200)
q20['bg']='#000'
q21=Label(tela)
q21['image']=vqImg
q21.place(x=331,y=200)
q21['bg']='#000'
q22=Label(tela)
q22['image']=vqImg
q22.place(x=380,y=200)
q22['bg']='#000'
q23=Label(tela)
q23['image']=vqImg
q23.place(x=429,y=200)
q23['bg']='#000'
q24=Label(tela)
q24['image']=vqImg
q24.place(x=478,y=200)
q24['bg']='#000'
q30=Label(tela)
q30['image']=vqImg
q30.place(x=282,y=249)
q30['bg']='#000'
q31=Label(tela)
q31['image']=vqImg
q31.place(x=331,y=249)
q31['bg']='#000'
q32=Label(tela)
q32['image']=vqImg
q32.place(x=380,y=249)
q32['bg']='#000'
q33=Label(tela)
q33['image']=vqImg
q33.place(x=429,y=249)
q33['bg']='#000'
q34=Label(tela)
q34['image']=vqImg
q34.place(x=478,y=249)
q34['bg']='#000'
q40=Label(tela)
q40['image']=vqImg
q40.place(x=282,y=298)
q40['bg']='#000'
q41=Label(tela)
q41['image']=vqImg
q41.place(x=331,y=298)
q41['bg']='#000'
q42=Label(tela)
q42['image']=vqImg
q42.place(x=380,y=298)
q42['bg']='#000'
q43=Label(tela)
q43['image']=vqImg
q43.place(x=429,y=298)
q43['bg']='#000'
q44=Label(tela)
q44['image']=vqImg
q44.place(x=478,y=298)
q44['bg']='#000'
q50=Label(tela)
q50['image']=vqImg
q50.place(x=282,y=347)
q50['bg']='#000'
q51=Label(tela)
q51['image']=vqImg
q51.place(x=331,y=347)
q51['bg']='#000'
q52=Label(tela)
q52['image']=vqImg
q52.place(x=380,y=347)
q52['bg']='#000'
q53=Label(tela)
q53['image']=vqImg
q53.place(x=429,y=347)
q53['bg']='#000'
q54=Label(tela)
q54['image']=vqImg
q54.place(x=478,y=347)
q54['bg']='#000'
q60=Label(tela)
q60['image']=vqImg
q60.place(x=282,y=396)
q60['bg']='#000'
q61=Label(tela)
q61['image']=vqImg
q61.place(x=331,y=396)
q61['bg']='#000'
q62=Label(tela)
q62['image']=vqImg
q62.place(x=380,y=396)
q62['bg']='#000'
q63=Label(tela)
q63['image']=vqImg
q63.place(x=429,y=396)
q63['bg']='#000'
q64=Label(tela)
q64['image']=vqImg
q64.place(x=478,y=396)
q64['bg']='#000'
q70=Label(tela)
q70['image']=vqImg
q70.place(x=282,y=445)
q70['bg']='#000'
q71=Label(tela)
q71['image']=vqImg
q71.place(x=331,y=445)
q71['bg']='#000'
q72=Label(tela)
q72['image']=vqImg
q72.place(x=380,y=445)
q72['bg']='#000'
q73=Label(tela)
q73['image']=vqImg
q73.place(x=429,y=445)
q73['bg']='#000'
q74=Label(tela)
q74['image']=vqImg
q74.place(x=478,y=445)
q74['bg']='#000'


btP=Button(tela)
btpImg=PhotoImage(file=r"imagens/btnP.png")
btP['image']=btpImg
btP['relief']=FLAT
btP['bg']="#006400"
btP['command']=clique
btP.place(x=380,y=515)

#fim criando 40 quadradinhos vermelhos labels##@
#criando quadrado amarelo
aqImg=PhotoImage(file=r'imagens/aq.png')
#fim quadradinho amarelo

chama()


# Conigurações da janela
tela.title("G'nus Mega Stacker") # titulo da janela
tela.iconbitmap(r"imagens\logoSistema.ico")# icone do programa
tela['bg'] = "#006400" # Background color
tela.resizable(0,0) # seta a janela com tamanho fixo
x = (tela.winfo_screenwidth() // 2) - (800 // 2) # Pega o valor X do ponto central
y = (tela.winfo_screenheight() // 2) - (600 // 2) # Pega o valor Y do ponto central
tela.geometry("800x600+{}+{}".format(x, y))  # largura x altura + esquerda + topo
tela.mainloop()


#criando matriz para classe futura>>
'''
mat=[]
for i in range(8):
    linha=[]
    for j in range(5):
        linha.append("q"+str(i)+str(j))
    mat.append(linha)
print(mat)
'''

'''
s=''
x=282
y=102
for i in range(8):
    for j in range(5):
        s=s+str(mat[i][j])+"=Label(tela)\n"+str(mat[i][j])+"['image']=vqImg\n"+str(mat[i][j])+".place(x="+str(x)+",y="+str(y)+")\n"+str(mat[i][j])+"['bg']='#000'"+"\n"
        x=x+49
    y=y+49
    x=282
print(s)
'''