'''
import cx_Freeze, sys, matplotlib, os

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables =[cx_Freeze.Executable("iniciar.py",base=base,icon='imagem/icone2.png')]

cx_Freeze.setup(
    name = "GNUCasinos",
    options = {"build_exe": {"packages":["tkinter","pygame","matplotlib","time","threading","partial","os","random","sys"],"include_files":["imagem/icone2.png"]}},
    version = "1.0",
    executables = executables
    )
'''
import sys
from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] ="C:\\Users\\Igor\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Igor\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executable = [
        Executable(script="Iniciar.py", base=base, icon="imagem/logoicone3.ico")
]

buildOptions = dict(
        packages = ["tkinter","pygame"],
        includes = ["tkinter","pygame","matplotlib","time","threading","os","random","sys","functools"],
        include_files = ["imagem/logoicone3.ico","Jogo.py","Howtoplay.py","imagem/aposta3.png","imagem/carteira2.png","imagem/entr_name.png","imagem/exit.png","imagem/howtoplayblackjack.png","imagem/howtoplaybutton.png","imagem/howtoplaymegastacker.png","imagem/howtoplayslotmachine.png","imagem/lb_apelido.png","imagem/logomeio.png","imagem/playBlackjack.png","imagem/playMegastacker.png","imagem/playSlotmachine.png","imagem/qtdcarteira.png","imagem/triangulodireita2.png","imagem/trinagulodireita.png","imagem/voltar2.png","imagem/icone2.png"],
        include_msvcr = True,
        excludes = []
)




setup(
    name = "GNUScasinos",
    version = "1.0",
    description = "Simulador de casinos",
    options = dict(build_exe = buildOptions),
    executables = executable
 )
