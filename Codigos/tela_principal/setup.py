import sys
from cx_Freeze import setup, Executable
import os

buildOptions = dict(
        packages = ["tkinter","sys","pygame"],
        includes = ["sys","pygame","tkinter"],
        include_files = ["imagem/logoicone3.ico",
                         os.path.join('C:\\Users\\Igor\\AppData\\Local\\Programs\\Python\\Python36-32', 'DLLs',
                                      'tk86t.dll'),
                         os.path.join('C:\\Users\\Igor\\AppData\\Local\\Programs\\Python\\Python36-32', 'DLLs',
                                      'tcl86t.dll'),
                         ],
        include_msvcr = True,
        excludes = []
)


os.environ['TCL_LIBRARY'] = "C:\\Users\\Igor\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Igor\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "G'nus Cassino",
        version = "1.0",
        description = "Hub de Cassino!",
        options = {"build_exe": buildOptions},
        executables = [Executable("Iniciar.py", base=base,icon="imagem/logoicone3.ico")])
