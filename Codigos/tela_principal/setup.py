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


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("iniciar.py", base=base,icon = "imagem/icone2.png")
]

buildOptions = dict(
        packages = ["tkinter"],
        includes = ["tkinter","pygame","matplotlib","time","threading","partial","os","random","sys"],
        include_files = ["imagem/icone2.png'"],
        excludes = []
)




setup(
    name = "GNUcasino",
    version = "1.0",
    description = "Simulador de casinos",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
