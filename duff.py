#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import traceback
import time
from random import choice


class tcolors:
    N = '\033[0m'  # Default
    R = '\033[31;1m'  # rojo
    G = '\033[32m'  # verde
    O = '\033[33m'  # naranja
    B = '\033[34m'  # azul
    M = '\033[35m'  # magenta
    C = '\033[36;1m'  # cian
    BK = '\033[37;1m'  # blanco


def main():
    plataforma = sys.platform
    if plataforma == "darwin" or plataforma.startswith("linux"):
        print tcolors.BK + '''

                         88                  ad88     ad88
                         88                 d8"      d8"
                         88                 88       88
                 ,adPPYb,88  88       88  MM88MMM  MM88MMM
                a8"    `Y88  88       88    88       88
                8b       88  88       88    88       88
                "8a,   ,d88  "8a,   ,a88    88       88
                 `"8bbdP"Y8   `"YbbdP'Y8    88       88

                ''' + tcolors.C + '''[!] Autor: backd0r  |  https://underc0de.org/foro/profile/backd0r/
                [!] Email: backd0r@bk.ru
                [!] Version: 1.0
                ''' + tcolors.R + '''+++ Duff es una herramienta para generar
                archivos con contraseñas aleatorias en su totalidad +++''' + tcolors.N
        try:
            def inicio():
                while True:
                    print '''
1) Crear contraseñas complejas utilizando el archivo de caracteres.
2) Crear solo contraseñas de números.
3) Configurar archivo de caracteres.
4) Salir!
                            '''
                    option1 = raw_input(tcolors.C + "duff > " + tcolors.N)
                    while option1 == "3":  # Muestra menú 2
                        print '''
1) Crear archivo charset.
2) Cargar nueva sección de caracteres.
3) Ver el contenido del archivo de caracteres.
4) Regresar al menú anterior.
                            '''
                        option2 = raw_input(tcolors.C + "duff > " + tcolors.N)
                        if option2 == "1":  # Crear el charset.lst por defecto.
                            outfile = "charset.lst"

                            fileout = open(outfile, "w+")
                            lib = '''hexlower = 0123456789abcdef
hexupper = 0123456789ABCDEF

numeric = 0123456789
numericspace = 0 123456789

symbols = !@#$%^&*()-_+=
symbolsspace = !@#$%^&*( )=-_+

symbolsall = !@#$%^&*()-_+=~`[]{}|\:;"'<>,.?/
symbolsallspace = !@#$%^&*()-_+=~`[]{}|\:;"'< >,.?/

ualpha = ABCDEFGHIJKLMNOPQRSTUVWXYZ
ualphaspace = ABCDEFGHIJKLMNOPQRSTUVWXY Z
ualphanumeric = ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
ualphanumericspace = ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789
ualphanumericsymbol = ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=
ualphanumericsymbolspace = ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789!@#$%^&*()=-_+
ualphanumericall = ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=~`[]{}|\:;"'<>,.?/
ualphanumericallspace = ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789!@#$%^&*()-_+=~`[]{}|\:;"'<>,.?/

lalpha = abcdefghijklmnopqrstuvwxyz
lalphaspace = abcdefghijklmnopqrstuvwxy z
lalphanumeric = abcdefghijklmnopqrstuvwxyz0123456789
lalphanumericspace = abcdefghijklmnopqrstuvwxyz 0123456789
lalphanumericsymbol = abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_+=
lalphanumericsymbolspace = abcdefghijklmnopqrstuvwxyz 0123456789!@#$%^&*()=-_+
lalphanumericall = abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_+=~`[]{}|\:;"'<>,.?/
lalphanumericallspace = abcdefghijklmnopqrstuvwxyz 0123456789!@#$%^&*()-_+=~`[]{}|\:;"'<>,.?/

mixalpha = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
mixalphaspace = abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
mixalphanumeric = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
mixalphanumericspace = abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
mixalphanumericsymbol = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=
mixalphanumericsymbolspace = abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+
mixalphanumericall = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=~`[]{}|\:;"'<>,.?/
mixalphanumericallspace = abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=~`[]{}|\:;"'<>,.?/

#############################
#  U S E R   O P T I O N S  #
#############################
'''
                            fileout.write(lib)
                            fileout.close()
                            print tcolors.R + "Espere por favor." + tcolors.N
                            print tcolors.R + "Listo, he creado charset.lst." + tcolors.N
                            time.sleep(2)
                            os.system("clear")
                        elif option2 == "2":  # Añadir contenido al charset.lst
                            print tcolors.R + '''
Para usar esta opción tienes que darme los valores de la siguiente forma:
    ''' + tcolors.C + '''       ej. duff > ''' + tcolors.N + '''minuevaseccion = AQUI LOS CARACTERES A USAR'''
                            print ""
                            line = raw_input(tcolors.C + "duff > " + tcolors.N) + "\n"
                            infile = "charset.lst"
                            if line != "\n":
                                filein = open(infile, "a")
                                filein.write(line)
                                filein.close()
                            else:
                                print ""
                                print tcolors.R + "Creo que no me has dado ningún valor." + tcolors.N
                                print tcolors.R + ":(" + tcolors.N
                                print ""
                                time.sleep(3)

                        elif option2 == "3":  # cat al archivo charset.lst
                            os.system("cat charset.lst")
                        elif option2 == "4":
                            os.system("clear")
                            main()
                            inicio()



                        else:
                            print ""
                            print tcolors.R + "Lo siento comando inválido." + tcolors.N
                            print tcolors.R + "Intentemos de nuevo." + tcolors.N
                            time.sleep(2)
                            os.system("clear")
                    if option1 == "1":
                        print ""
                        print tcolors.R + "[!] Cuántos caracteres quieres que tenga la contraseña?" + tcolors.N
                        print ""
                        digitos = int(raw_input(tcolors.C + "duff > " + tcolors.N))
                        print ""
                        print tcolors.R + "[!] Cuántas contraseñas quieres generar?" + tcolors.N
                        print ""
                        numpass = int(raw_input(tcolors.C + "duff > " + tcolors.N))
                        print ""
                        print tcolors.R + '''[!] Con que caracteres debo trabajar. (usa el charset.lst)''' + tcolors.G + '''
Ejemplo:
Si debo trabajar solo con letras mayusculas me das el siguiente valor.
    ''' + tcolors.C + '''       ej. duff > ''' + tcolors.N + ''' ualpha
    ''' + tcolors.N
                        print ""
                        charsec = raw_input(tcolors.C + "duff > " + tcolors.N)
                        print ""
                        print tcolors.R + "[!] Dame el nombre de tu archivo de salida? (*.txt)" + tcolors.N
                        print ""
                        passtxt = raw_input(tcolors.C + "duff > " + tcolors.N)
                        infile = "charset.lst"
                        with open(infile) as fileopen:
                            for line in fileopen:
                                if charsec in line:
                                    listas = line.split(" = ")
                                    charoptions = listas[0]
                                    if charoptions == charsec:
                                        chars = listas[1].rstrip("\n")
                                        file_ex = open(passtxt, "w")
                                        for i in range(numpass):
                                            creapass = ''.join([choice(chars) for i in range(digitos)]) + "\n"
                                            file_ex.write(creapass)
                                        file_ex.close()

                        print ""
                        print tcolors.R + "[!] Listo he generado tu archivo se llama: " + passtxt + tcolors.N
                        time.sleep(2)
                        os.system("clear")




                    elif option1 == "2":  # Crear solo contraseñas de numeros.
                        infile = "charset.lst"
                        charsec = "numeric"
                        print ""
                        print tcolors.R + "[!] Cuántos caracteres quieres que tenga la contraseña?" + tcolors.N
                        print ""
                        digitos = int(raw_input(tcolors.C + "duff > " + tcolors.N))
                        print ""
                        print tcolors.R + "[!] Cuántas contraseñas quieres generar?" + tcolors.N
                        print ""
                        numpass = int(raw_input(tcolors.C + "duff > " + tcolors.N))
                        print ""
                        print tcolors.R + "[!] Dame el nombre de tu archivo de salida? (*.txt)" + tcolors.N
                        print ""
                        passtxt = raw_input(tcolors.C + "duff > " + tcolors.N)
                        print ""
                        with open(infile) as fileopen:
                            for line in fileopen:
                                if charsec in line:
                                    listas = line.split(" = ")
                                    charoptions = listas[0]
                                    if charoptions == charsec:
                                        chars = listas[1].rstrip("\n")
                                        file_ex = open(passtxt, "w")
                                        for i in range(numpass):
                                            creapass = ''.join([choice(chars) for i in range(digitos)]) + "\n"
                                            file_ex.write(creapass)
                                        file_ex.close()
                                        print ""
                                        print tcolors.R + "[!] Listo he generado tu archivo se llama: " + passtxt + tcolors.N
                                        time.sleep(2)
                                        os.system("clear")



                    elif option1 == "4":
                        print ""
                        print "Gracias por usar Duff, hasta la proxima."
                        print ""
                        sys.exit(0)
                    else:
                        print ""
                        print tcolors.R + "Lo siento comando inválido." + tcolors.N
                        print tcolors.R + "Intentemos de nuevo." + tcolors.N
                        time.sleep(2)
                        os.system("clear")
                        main()
                        inicio()

            inicio()
        except KeyboardInterrupt:
            print ""
            print "Gracias por usar Duff, hasta la proxima."
            print ""
        except Exception:
            traceback.print_exc(file=sys.stdout)
        sys.exit(0)
    elif plataforma.startswith("win"):
                #Comieza script para windows
                os.system("color 7")
                print '''

             88                  ad88     ad88
             88                 d8"      d8"
             88                 88       88
     ,adPPYb,88  88       88  MM88MMM  MM88MMM
    a8"    `Y88  88       88    88       88
    8b       88  88       88    88       88
    "8a,   ,d88  "8a,   ,a88    88       88
     `"8bbdP"Y8   `"YbbdP'Y8    88       88

    [!] Autor: backd0r  |  https://underc0de.org/foro/profile/backd0r/
    [!] Email: backd0r@bk.ru
    [!] Version: 1.0
    ++ Duff es una herramienta para generar
    archivos con passwords aleatorias en su totalidad +++'''
                try:
                    def inicio():
                        while True:

                            print '''
1) Crear passwords complejas utilizando el archivo de caracteres.
2) Crear solo passwords de numeros.
3) Configurar archivo de caracteres.
4) Salir!
                                    '''
                            option1 = raw_input("duff > ")
                            while option1 == "3":  # Muestra menú 2
                                print '''
1) Crear archivo charset.
2) Cargar nueva seccion de caracteres.
3) Ver el contenido del archivo de caracteres.
4) Regresar al menu anterior.
                                    '''
                                option2 = raw_input("duff > ")
                                if option2 == "1":  # Crear el charset.lst por defecto.
                                    outfile = "charset.lst"

                                    fileout = open(outfile, "w+")
                                    lib = '''hexlower = 0123456789abcdef
hexupper = 0123456789ABCDEF

numeric = 0123456789
numericspace = 0 123456789

symbols = !@#$%^&*()-_+=
symbolsspace = !@#$%^&*( )=-_+

symbolsall = !@#$%^&*()-_+=~`[]{}|\:;"'<>,.?/
symbolsallspace = !@#$%^&*()-_+=~`[]{}|\:;"'< >,.?/

ualpha = ABCDEFGHIJKLMNOPQRSTUVWXYZ
ualphaspace = ABCDEFGHIJKLMNOPQRSTUVWXY Z
ualphanumeric = ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
ualphanumericspace = ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789
ualphanumericsymbol = ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=
ualphanumericsymbolspace = ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789!@#$%^&*()=-_+
ualphanumericall = ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=~`[]{}|\:;"'<>,.?/
ualphanumericallspace = ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789!@#$%^&*()-_+=~`[]{}|\:;"'<>,.?/

lalpha = abcdefghijklmnopqrstuvwxyz
lalphaspace = abcdefghijklmnopqrstuvwxy z
lalphanumeric = abcdefghijklmnopqrstuvwxyz0123456789
lalphanumericspace = abcdefghijklmnopqrstuvwxyz 0123456789
lalphanumericsymbol = abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_+=
lalphanumericsymbolspace = abcdefghijklmnopqrstuvwxyz 0123456789!@#$%^&*()=-_+
lalphanumericall = abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_+=~`[]{}|\:;"'<>,.?/
lalphanumericallspace = abcdefghijklmnopqrstuvwxyz 0123456789!@#$%^&*()-_+=~`[]{}|\:;"'<>,.?/

mixalpha = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
mixalphaspace = abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
mixalphanumeric = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
mixalphanumericspace = abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
mixalphanumericsymbol = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=
mixalphanumericsymbolspace = abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+
mixalphanumericall = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=~`[]{}|\:;"'<>,.?/
mixalphanumericallspace = abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=~`[]{}|\:;"'<>,.?/

#############################
#  U S E R   O P T I O N S  #
#############################
'''
                                    fileout.write(lib)
                                    fileout.close()
                                    print "Espere por favor."
                                    time.sleep(1)
                                    print "Listo, he creado charset.lst."
                                    time.sleep(2)
                                    os.system("cls")
                                elif option2 == "2":  # Añadir contenido al charset.lst
                                    print '''
    Para usar esta opcion tienes que darme los valores de la siguiente forma:
          ej. duff > minuevaseccion = AQUI LOS CARACTERES A USAR'''
                                    print ""
                                    line = raw_input("duff > ") + "\n"
                                    infile = "charset.lst"
                                    if line != "\n":
                                        filein = open(infile, "a")
                                        filein.write(line)
                                        filein.close()
                                    else:
                                        print ""
                                        print "Creo que no me has dado ningun valor."
                                        print ":("
                                        print ""
                                        time.sleep(3)

                                elif option2 == "3":  # cat al archivo charset.lst
                                    os.system("type charset.lst")
                                elif option2 == "4":
                                    os.system("cls")
                                    main()
                                    inicio()



                                else:
                                    print ""
                                    print "Lo siento comando invalido."
                                    print "Intentemos de nuevo."
                                    time.sleep(2)
                                    os.system("cls")
                            if option1 == "1":
                                print ""
                                print "[!] Cuantos caracteres quieres que tenga la contrasena?"
                                print ""
                                digitos = int(raw_input("duff > "))
                                print ""
                                print "[!] Cuantas passwords quieres generar?"
                                print ""
                                numpass = int(raw_input("duff > "))
                                print ""
                                print '''[!] Con que caracteres debo trabajar. (usa el charset.lst)
    Ejemplo:
    Si debo trabajar solo con letras mayusculas me das el siguiente valor.
          ej. duff > ualpha
            '''
                                print ""
                                charsec = raw_input("duff > ")
                                print ""
                                print "[!] Dame el nombre de tu archivo de salida? (*.txt)"
                                print ""
                                passtxt = raw_input("duff > ")
                                infile = "charset.lst"
                                with open(infile) as fileopen:
                                    for line in fileopen:
                                        if charsec in line:
                                            listas = line.split(" = ")
                                            charoptions = listas[0]
                                            if charoptions == charsec:
                                                chars = listas[1].rstrip("\n")
                                                file_ex = open(passtxt, "w")
                                                for i in range(numpass):
                                                    creapass = ''.join([choice(chars) for i in range(digitos)]) + "\n"
                                                    file_ex.write(creapass)
                                                file_ex.close()

                                print ""
                                print "[!] Listo he generado tu archivo se llama: " + passtxt
                                time.sleep(2)
                                os.system("cls")




                            elif option1 == "2":  # Crear solo contraseñas de numeros.
                                infile = "charset.lst"
                                charsec = "numeric"
                                print ""
                                print "[!] Cuantos caracteres quieres que tenga la password?"
                                print ""
                                digitos = int(raw_input( "duff > " ))
                                print ""
                                print "[!] Cuantas passwords quieres generar?"
                                print ""
                                numpass = int(raw_input( "duff > " ))
                                print ""
                                print "[!] Dame el nombre de tu archivo de salida? (*.txt)"
                                print ""
                                passtxt = raw_input( "duff > " )
                                print ""
                                with open(infile) as fileopen:
                                    for line in fileopen:
                                        if charsec in line:
                                            listas = line.split(" = ")
                                            charoptions = listas[0]
                                            if charoptions == charsec:
                                                chars = listas[1].rstrip("\n")
                                                file_ex = open(passtxt, "w")
                                                for i in range(numpass):
                                                    creapass = ''.join([choice(chars) for i in range(digitos)]) + "\n"
                                                    file_ex.write(creapass)
                                                file_ex.close()
                                                print ""
                                                print  "[!] Listo he generado tu archivo se llama: " + passtxt
                                                time.sleep(2)
                                                os.system("cls")



                            elif option1 == "4":
                                print ""
                                print "Gracias por usar Duff, hasta la proxima."
                                print ""
                                sys.exit(0)
                            else:
                                print ""
                                print  "Lo siento comando invalido."
                                print  "Intentemos de nuevo."
                                time.sleep(2)
                                os.system("cls")
                                main()
                                inicio()

                    inicio()
                except KeyboardInterrupt:
                    print ""
                    print "Gracias por usar Duff, hasta la proxima."
                    print ""
                except Exception:
                    traceback.print_exc(file=sys.stdout)
                sys.exit(0)

    else:
        print tcolors.R + "me perdí :(" + tcolors.N
        sys.exit(0)

if __name__ == "__main__":
    main()
