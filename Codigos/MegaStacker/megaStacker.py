import threading
from tkinter import *
import time
from functools import partial

#GNUS DIGITAIS> BRUNO, RODRIGO, MATHEUS E IGOR
def linha1():
    u=0
    global cliq
    while True:
        if cliq !=1:
            q00['image'] = aqImg
            time.sleep(0.1)
        else:
            #q00['image'] = aqImg
            u=1
            break
        if cliq != 1:
            q01['image'] = aqImg
            time.sleep(0.1)
        else:
            #q01['image'] = aqImg
            u=2
            break
        if cliq != 1:
            q02['image'] = aqImg
            time.sleep(0.1)
        else:
            #q02['image'] = aqImg
            u=3
            break
        if cliq != 1:
            q03['image'] = aqImg
            time.sleep(0.1)
        else:
            #q03['image'] = aqImg
            u=4
            break
        if cliq != 1:
            q04['image'] = aqImg
            time.sleep(0.1)
        else:
            q04['image'] = aqImg
            u=5
            break

        q04['image'] = vqImg
        q03['image'] = vqImg
        q02['image'] = vqImg
        q01['image'] = vqImg
        q00['image'] = vqImg
        time.sleep(0.0)
        q00['image'] = aqImg
    cliq = 0
    analisa_resultado(u)


def linha2():
    u=0
    global cliq
    while True:
        if cliq !=1:
            q10['image'] = aqImg
            time.sleep(0.1)
        else:
            #q10['image'] = aqImg
            u=1
            break
        if cliq != 1:
            q11['image'] = aqImg
            time.sleep(0.1)
        else:
            #q11['image'] = aqImg
            u=2
            break
        if cliq != 1:
            q12['image'] = aqImg
            time.sleep(0.1)
        else:
            #q12['image'] = aqImg
            u=3
            break
        if cliq != 1:
            q13['image'] = aqImg
            time.sleep(0.1)
        else:
            #q13['image'] = aqImg
            u=4
            break
        if cliq != 1:
            q14['image'] = aqImg
            time.sleep(0.1)
        else:
            q14['image'] = aqImg
            u=5
            break

        q14['image'] = vqImg
        q13['image'] = vqImg
        q12['image'] = vqImg
        q11['image'] = vqImg
        q10['image'] = vqImg
        time.sleep(0.0)
        q10['image'] = aqImg
    cliq = 0
    analisa_resultado(u)


def linha3():
    u=0
    global cliq
    while True:
        if cliq !=1:
            q20['image'] = aqImg
            time.sleep(0.1)
        else:
            #q20['image'] = aqImg
            u=1
            break
        if cliq != 1:
            q21['image'] = aqImg
            time.sleep(0.2)
        else:
            #q21['image'] = aqImg
            u=2
            break
        if cliq != 1:
            q22['image'] = aqImg
            time.sleep(0.2)
        else:
            #q22['image'] = aqImg
            u=3
            break
        if cliq != 1:
            q23['image'] = aqImg
            time.sleep(0.2)
        else:
            #q23['image'] = aqImg
            u=4
            break
        if cliq != 1:
            q24['image'] = aqImg
            time.sleep(0.2)
        else:
            q24['image'] = aqImg
            u=5
            break

        q24['image'] = vqImg
        q23['image'] = vqImg
        q22['image'] = vqImg
        q21['image'] = vqImg
        q20['image'] = vqImg
        time.sleep(0.0)
        q20['image'] = aqImg
    cliq = 0
    analisa_resultado(u)



def linha4():
    u=0
    global cliq
    while True:
        if cliq !=1:
            q30['image'] = aqImg
            time.sleep(0.1)
        else:
            #q30['image'] = aqImg
            u=1
            break
        if cliq != 1:
            q31['image'] = aqImg
            time.sleep(0.2)
        else:
            #q31['image'] = aqImg
            u=2
            break
        if cliq != 1:
            q32['image'] = aqImg
            time.sleep(0.2)
        else:
            #q32['image'] = aqImg
            u=3
            break
        if cliq != 1:
            q33['image'] = aqImg
            time.sleep(0.2)
        else:
            #q33['image'] = aqImg
            u=4
            break
        if cliq != 1:
            q34['image'] = aqImg
            time.sleep(0.2)
        else:
            q34['image'] = aqImg
            u=5
            break

        q34['image'] = vqImg
        q33['image'] = vqImg
        q32['image'] = vqImg
        q31['image'] = vqImg
        q30['image'] = vqImg
        time.sleep(0.0)
        q30['image'] = aqImg
    cliq = 0
    analisa_resultado(u)


def linha5():
    u=0
    global cliq
    while True:
        if cliq !=1:
            q40['image'] = aqImg
            time.sleep(0.1)
        else:
            #q40['image'] = aqImg
            u=1
            break
        if cliq != 1:
            q41['image'] = aqImg
            time.sleep(0.3)
        else:
            #q41['image'] = aqImg
            u=2
            break
        if cliq != 1:
            q42['image'] = aqImg
            time.sleep(0.3)
        else:
            #q42['image'] = aqImg
            u=3
            break
        if cliq != 1:
            q43['image'] = aqImg
            time.sleep(0.3)
        else:
            #q43['image'] = aqImg
            u=4
            break
        if cliq != 1:
            q44['image'] = aqImg
            time.sleep(0.3)
        else:
            q44['image'] = aqImg
            u=5
            break

        q44['image'] = vqImg
        q43['image'] = vqImg
        q42['image'] = vqImg
        q41['image'] = vqImg
        q40['image'] = vqImg
        time.sleep(0.0)
        q40['image'] = aqImg
    cliq = 0
    analisa_resultado(u)


def linha6():
    u=0
    global cliq
    while True:
        if cliq !=1:
            q50['image'] = aqImg
            time.sleep(0.1)
        else:
            #q50['image'] = aqImg
            u=1
            break
        if cliq != 1:
            q51['image'] = aqImg
            time.sleep(0.4)
        else:
            #q51['image'] = aqImg
            u=2
            break
        if cliq != 1:
            q52['image'] = aqImg
            time.sleep(0.4)
        else:
            #q52['image'] = aqImg
            u=3
            break
        if cliq != 1:
            q53['image'] = aqImg
            time.sleep(0.4)
        else:
            #q53['image'] = aqImg
            u=4
            break
        if cliq != 1:
            q54['image'] = aqImg
            time.sleep(0.4)
        else:
            q54['image'] = aqImg
            u=5
            break

        q54['image'] = vqImg
        q53['image'] = vqImg
        q52['image'] = vqImg
        q51['image'] = vqImg
        q50['image'] = vqImg
        time.sleep(0.0)
        q50['image'] = aqImg
    cliq = 0
    analisa_resultado(u)


def linha7():
    u=0
    global cliq
    while True:
        if cliq !=1:
            q60['image'] = aqImg
            time.sleep(0.1)
        else:
            #q60['image'] = aqImg
            u=1
            break
        if cliq != 1:
            q61['image'] = aqImg
            time.sleep(0.5)
        else:
            #q61['image'] = aqImg
            u=2
            break
        if cliq != 1:
            q62['image'] = aqImg
            time.sleep(0.5)
        else:
            #q62['image'] = aqImg
            u=3
            break
        if cliq != 1:
            q63['image'] = aqImg
            time.sleep(0.5)
        else:
            #q63['image'] = aqImg
            u=4
            break
        if cliq != 1:
            q64['image'] = aqImg
            time.sleep(0.5)
        else:
            q64['image'] = aqImg
            u=5
            break

        q64['image'] = vqImg
        q63['image'] = vqImg
        q62['image'] = vqImg
        q61['image'] = vqImg
        q60['image'] = vqImg
        time.sleep(0.0)
        q60['image'] = aqImg
    cliq = 0
    analisa_resultado(u)


def linha8():
    global ultima
    global cliq
    while True:
        if cliq!=1:
            q70['image']=aqImg
            time.sleep(0.1)#por enquanto menor time 2!!
            #fazer com u?
        else:
           #q70['image'] = aqImg
            ultima=1
            break
        if cliq != 1:
            q71['image']=aqImg
            time.sleep(0.5)
        else:
            #q71['image'] = aqImg
            ultima=2
            break
        if cliq != 1:
            q72['image']=aqImg
            time.sleep(0.5)
        else:
            #q72['image'] = aqImg
            ultima=3
            break
        if cliq != 1:
            q73['image']=aqImg
            time.sleep(0.5)
        else:
            #q73['image'] = aqImg
            ultima=4
            break
        if cliq != 1:
            q74['image']=aqImg
            time.sleep(0.5)
        else:
            q74['image'] = aqImg
            ultima=5
            break


        q74['image'] = vqImg
        q73['image'] = vqImg
        q72['image'] = vqImg
        q71['image'] = vqImg
        q70['image'] = vqImg
        time.sleep(0.0)
        q70['image'] = aqImg

    cliq = 0
    linha7()


def analisa_resultado(u):
    global ultima
    global linha
    linha=linha-1
    if linha==6:
        if ultima==u:
            print("aqui analisa o resultado do player\npassou para proxima linha")
            linha6()
    elif linha==5:
        if ultima==u:
            print("aqui analisa o resultado do player\npassou para proxima linha")
            linha5()
        else:
            print("você perdeu - linha 5.")
    elif linha==4:
        if ultima==u:
            print("aqui analisa o resultado do player\npassou para proxima linha")
            linha4()
        else:
            print("você perdeu - linha 4.")
    elif linha==3:
        if ultima==u:
            print("aqui analisa o resultado do player\npassou para proxima linha")
            linha3()
        else:
            print("você perdeu - linha 3.")
    elif linha==2:
        if ultima==u:
            linha2()
            print("aqui analisa o resultado do player\npassou para proxima linha")
        else:
            print("você perdeu - linha 2.")
    elif linha==1:
        if ultima==u:
            print("aqui analisa o resultado do player\npassou para proxima linha")
            linha1()
        else:
            print("você perdeu - linha 1.")
    else:
        print("@@@chegou ao topo ! presumo! @@@")

def reniciar():
    global cliq, ultima, linha,vqImg
    analisa_resultado(-1)
    linha = 7
    ultima = 0
    clic = 0
    q00['image']=vqImg
    q01['image']=vqImg
    q02['image']=vqImg
    q03['image']=vqImg
    q04['image']=vqImg
    q10['image']=vqImg
    q11['image']=vqImg
    q12['image']=vqImg
    q13['image']=vqImg
    q14['image']=vqImg
    q20['image']=vqImg
    q21['image']=vqImg
    q22['image']=vqImg
    q23['image']=vqImg
    q24['image']=vqImg
    q30['image']=vqImg
    q31['image']=vqImg
    q32['image']=vqImg
    q33['image']=vqImg
    q34['image']=vqImg
    q40['image']=vqImg
    q41['image']=vqImg
    q42['image']=vqImg
    q43['image']=vqImg
    q44['image']=vqImg
    q50['image']=vqImg
    q51['image']=vqImg
    q52['image']=vqImg
    q53['image']=vqImg
    q54['image']=vqImg
    q60['image']=vqImg
    q61['image']=vqImg
    q62['image']=vqImg
    q63['image']=vqImg
    q64['image']=vqImg
    q70['image']=vqImg
    q71['image']=vqImg
    q72['image']=vqImg
    q73['image']=vqImg
    q74['image']=vqImg
    chama()

def chama():
    threading.Timer(0.2,linha8).start()

def clique():
    print("clicou")
    global cliq
    cliq=1

# inicia tela
tela = Tk()
cliq=0
ultima=0
linha=7
#mat=[['q00', 'q01', 'q02', 'q03', 'q04'], ['q10', 'q11', 'q12', 'q13', 'q14'], ['q20', 'q21', 'q22', 'q23', 'q24'], ['q30', 'q31', 'q32', 'q33', 'q34'], ['q40', 'q41', 'q42', 'q43', 'q44'], ['q50', 'q51', 'q52', 'q53', 'q54'], ['q60', 'q61', 'q62', 'q63', 'q64'], ['q70', 'q71', 'q72', 'q73', 'q74']]


maquina=Label(tela)
maqImg=PhotoImage(file=r"imagens/megaStacker.png")
maquina['image']=maqImg
maquina.place(x=260,y=40)
maquina['bg']="#006400"

#quadradinho vermelho
vqImg=PhotoImage(file=r"imagens/vq.png")
#fim quadradinho vermelho

#criando 40 quadradinhos vermelhos labels@@



#btn parar!
btP=Button(tela)
btpImg=PhotoImage(file=r"imagens/pare.png")
btP['image']=btpImg
btP['relief']=FLAT
btP['bg']="#006400"
btP['command']=clique
btP.place(x=410,y=515)

#brn Reiniciar!
btR=Button(tela)
btrImg=PhotoImage(file=r"imagens/reinicio.png")
btR['image']=btrImg
btR['relief']=FLAT
btR['bg']="#006400"
btR['command']= reniciar
btR.place(x=290,y=515)


#fim criando 40 quadradinhos vermelhos labels##@
q00 = Label(tela)
q00['image'] = vqImg
q00.place(x=282, y=102)
q00['bg'] = '#000'
q01 = Label(tela)
q01['image'] = vqImg
q01.place(x=331, y=102)
q01['bg'] = '#000'
q02 = Label(tela)
q02['image'] = vqImg
q02.place(x=380, y=102)
q02['bg'] = '#000'
q03 = Label(tela)
q03['image'] = vqImg
q03.place(x=429, y=102)
q03['bg'] = '#000'
q04 = Label(tela)
q04['image'] = vqImg
q04.place(x=478, y=102)
q04['bg'] = '#000'
q10 = Label(tela)
q10['image'] = vqImg
q10.place(x=282, y=151)
q10['bg'] = '#000'
q11 = Label(tela)
q11['image'] = vqImg
q11.place(x=331, y=151)
q11['bg'] = '#000'
q12 = Label(tela)
q12['image'] = vqImg
q12.place(x=380, y=151)
q12['bg'] = '#000'
q13 = Label(tela)
q13['image'] = vqImg
q13.place(x=429, y=151)
q13['bg'] = '#000'
q14 = Label(tela)
q14['image'] = vqImg
q14.place(x=478, y=151)
q14['bg'] = '#000'
q20 = Label(tela)
q20['image'] = vqImg
q20.place(x=282, y=200)
q20['bg'] = '#000'
q21 = Label(tela)
q21['image'] = vqImg
q21.place(x=331, y=200)
q21['bg'] = '#000'
q22 = Label(tela)
q22['image'] = vqImg
q22.place(x=380, y=200)
q22['bg'] = '#000'
q23 = Label(tela)
q23['image'] = vqImg
q23.place(x=429, y=200)
q23['bg'] = '#000'
q24 = Label(tela)
q24['image'] = vqImg
q24.place(x=478, y=200)
q24['bg'] = '#000'
q30 = Label(tela)
q30['image'] = vqImg
q30.place(x=282, y=249)
q30['bg'] = '#000'
q31 = Label(tela)
q31['image'] = vqImg
q31.place(x=331, y=249)
q31['bg'] = '#000'
q32 = Label(tela)
q32['image'] = vqImg
q32.place(x=380, y=249)
q32['bg'] = '#000'
q33 = Label(tela)
q33['image'] = vqImg
q33.place(x=429, y=249)
q33['bg'] = '#000'
q34 = Label(tela)
q34['image'] = vqImg
q34.place(x=478, y=249)
q34['bg'] = '#000'
q40 = Label(tela)
q40['image'] = vqImg
q40.place(x=282, y=298)
q40['bg'] = '#000'
q41 = Label(tela)
q41['image'] = vqImg
q41.place(x=331, y=298)
q41['bg'] = '#000'
q42 = Label(tela)
q42['image'] = vqImg
q42.place(x=380, y=298)
q42['bg'] = '#000'
q43 = Label(tela)
q43['image'] = vqImg
q43.place(x=429, y=298)
q43['bg'] = '#000'
q44 = Label(tela)
q44['image'] = vqImg
q44.place(x=478, y=298)
q44['bg'] = '#000'
q50 = Label(tela)
q50['image'] = vqImg
q50.place(x=282, y=347)
q50['bg'] = '#000'
q51 = Label(tela)
q51['image'] = vqImg
q51.place(x=331, y=347)
q51['bg'] = '#000'
q52 = Label(tela)
q52['image'] = vqImg
q52.place(x=380, y=347)
q52['bg'] = '#000'
q53 = Label(tela)
q53['image'] = vqImg
q53.place(x=429, y=347)
q53['bg'] = '#000'
q54 = Label(tela)
q54['image'] = vqImg
q54.place(x=478, y=347)
q54['bg'] = '#000'
q60 = Label(tela)
q60['image'] = vqImg
q60.place(x=282, y=396)
q60['bg'] = '#000'
q61 = Label(tela)
q61['image'] = vqImg
q61.place(x=331, y=396)
q61['bg'] = '#000'
q62 = Label(tela)
q62['image'] = vqImg
q62.place(x=380, y=396)
q62['bg'] = '#000'
q63 = Label(tela)
q63['image'] = vqImg
q63.place(x=429, y=396)
q63['bg'] = '#000'
q64 = Label(tela)
q64['image'] = vqImg
q64.place(x=478, y=396)
q64['bg'] = '#000'
q70 = Label(tela)
q70['image'] = vqImg
q70.place(x=282, y=445)
q70['bg'] = '#000'
q71 = Label(tela)
q71['image'] = vqImg
q71.place(x=331, y=445)
q71['bg'] = '#000'
q72 = Label(tela)
q72['image'] = vqImg
q72.place(x=380, y=445)
q72['bg'] = '#000'
q73 = Label(tela)
q73['image'] = vqImg
q73.place(x=429, y=445)
q73['bg'] = '#000'
q74 = Label(tela)
q74['image'] = vqImg
q74.place(x=478, y=445)
q74['bg'] = '#000'

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