# Simple Transpiler Written In Python.
# Created By: Luiz Gabriel Magalhães Trindade.
# Distributed Under The GPL3 License:
# GPL3 License: https://www.gnu.org/licenses/gpl-3.0.en.html#license-text

from sys import argv
from os import system as S

c_compiler = "tcc"

program = str(argv[1])

source = []

c_source = [
    "#include <stdio.h>", 
    "#include <stdlib.h>", 
    "#include <string.h>", 
    "int main(){"
    ]
    
var = {}

# Debug Function.
def View_C_Code():
    global c_source
    print("""
    --------------
        C CODE
    --------------
    """)
    for i in c_source:
        print(i)

def Read_Source():
    global program, source
    with open(program, "r") as file:
        source = [f.strip() for f in file]

def Transpile_To_C():
    global source, c_compiler, c_source, var
    counter = 0
    while counter < len(source):
        command = source[counter].split(" ")

        #Seção para manipular dados.
        if command[0] == "print":
            content = " ".join(command[1:])
            c_source.append(f'printf("{content}");')

        elif command[0] == "number":
            name = str(command[1])
            content = float(command[2])
            var[name] = str("%f")
            c_source.append(f'float {name} = {content};')

        elif command[0] == "string":
            name = str(command[1])
            content = str("".join(command[2:]))
            length = len(content)+1
            var[name] = str("%s")
            c_source.append(f'char {name}[{length}] = "{content}";')

        elif command[0] == "view":
            name = str(command[1])
            var_type = var[name]
            c_source.append(f'printf("{var_type}", {name});')

        #Labels
        elif command[0] == "section":
            name = str(command[1])
            c_source.append(f'{name}:')

        elif command[0] == "goto":
            section_to_go = str(command[1])
            c_source.append(f"goto {section_to_go};")

        elif command[0] == "math":
            value1 = float(command[1])
            operan = float(command[2])
            value2 = float(command[3])
            result = float(command[4])
            c_source.append(f"{result} = {value1} {operan} {value2};")

        elif command[0] == "SYSTEM":
            cmd = " ".join(command[1:])
            c_source.append(f'system("{cmd}");')

        #Forçar o fim da execução do programa
        elif command[0] == "end":
            c_source.append("break;")
        
        counter += 1    
    c_source.append("return 0;")
    c_source.append("}")

def Make_Executable():
    global programa, c_source, c_compiler
    with open(f"{program}.c", "w") as c_file:
        c_file.writelines("\n".join(c_source))
    try: 
        S(f"{c_compiler} -Ofast -flto -finline-functions -funroll-loops -ftree-vectorize {program}.c -o {program}_exec")
        S(f"rm {program}.c")
    except: 
        S(f"gcc -Ofast -flto -finline-functions -funroll-loops -ftree-vectorize {program}.c -o {program}_exec")
        S(f"rm {program}.c")

def Main():
    try:
        Read_Source()
        Transpile_To_C()
        Make_Executable()
        print("Sucess!")
        View_C_Code()
    except Exception as error:
        print(error)

Main()
