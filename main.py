#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Archivo principal del programa

import os

import cl_texto
import trabajar_texto as tt
import crear_html


def main():
    #<--BUCLE PRINCIPAL-->
    b_principal = True  # Bucle principal del menú
    while b_principal:
        #<--MENU DE INICIO-->
        print("")
        print("***Bienvenido a Textos Incompletos***")
        print("")
        print("¿Qué acción desea realizar?")
        print("\t(n)Agregar un archivo nuevo")
        print("\t(v)Ver los textos editados hasta ahora")
        print("\t(r)Reeditar un texto")
        print("\t(s)Salir")
        eleccion = str(input("¿? "))

        #<--PROCESADOR DE EVENTOS-->
        if eleccion.strip().upper().startswith("N"):
            '''Opción para agregar un nuevo archivo'''
            #<--INTRODUCCIÓN DE DATOS-->
            nombre_archivo = str(input('''Nombre del archivo de texto nuevo >> '''))
            direc_video = str(input('''Dirección URL del video >> '''))
            try:
                tipo_edicion = int(input('''Tipo de edición a realizar: 1 (una
                palabra por línea), 2(dos palabras por línea), etc >> '''))
            except:
                print("")
                print("El dato que has introducido no es valido")

                continue

            #<--REVISAMOS SI EL ARCHIVO YA HA SIDO CREADO-->
            nombre = os.path.splitext(nombre_archivo)[0]
            nombre_html = "Canciones/" + nombre + "(incompleta).html"                                        
            if os.path.exists(nombre_html):
                print("")
                print("Ese archivo ya ha sido editado")
                print("El archivo no se ha creado")
                
                continue
                
            #<-----LECTURA Y ACOMODO DEL ARCHIVO----->
            # Ruta del archivo de texto
            ruta_archivo = "Canciones/" + nombre_archivo
            # Comprobamos si existe el archivo de texto
            try:
                archivo = open(ruta_archivo, "r")
            except:
                print("")
                print("No existe el archivo %s" % (nombre))
                
                continue

            # Separamos el texto por líneas y después por palabras en cada línea
            texto_editar = archivo.read().split("\n")
            archivo.close()
            for linea in range(len(texto_editar)):
                texto_editar[linea] = texto_editar[linea].split()

            #Escribimos el archivo como lo tenemos editado hasta el momento
            # Creación del objeto texto
            texto_objeto = cl_texto.Texto(nombre_archivo)
            texto_objeto.escribir_archivo(direc_video,texto_editar)

            #Edición del archivo a html
            #####REVISIÓN
            editar_archivo_html(nombre_archivo, texto_editar, tipo_edicion,
                                direc_video)

            #Agregamos el nuevo elemento en la base de datos
            bd_textos = open("bd_textos", "a")
            bd_textos.write(nombre_archivo + "\n")
            bd_textos.close()

        elif eleccion.strip().upper().startswith("V"):
            #Opción para ver los archivo editados hasta ahora
            #<--Lectura del archivo-->
            bd_lista = tt.leer_archivo("bd_textos")
            for i in bd_lista:
                print(i)

        elif eleccion.strip().upper().startswith("R"):
            #Opción para reeditar un archivo ya creado
            nombre_archivo = str(input("¿Cuál archivo deseas reeditar?"))
            tipo_edicion = int(input("¿Qué tipo de edición deseas realizar?"))
            texto = cl_texto.Texto(nombre_archivo)
            texto.leer_archivo()

            editar_archivo_html(nombre_archivo, texto.texto, tipo_edicion,
                texto.video)

        elif eleccion.strip().upper().startswith("S"):
            #Opción para salir del programa
            b_principal = False


def editar_archivo_html(nombre_archivo, lista, edicion, video):
    '''función para ahorrar espacio'''
    #<-----EDICIÓN DEL ARCHIVO----->
    #Se sustituye (tipo_edicion) número de palabras al azar por una indicación
    #####REVISIÓN
    texto_editado = tt.quitar_palabras_azar(lista, edicion)

    #<-----CREACIÓN DE LA PLANTILLA----->
    #Hacemos la edición HTML
    archivo_html = crear_html.crear_html(nombre_archivo, texto_editado, video)
    #Añadimos un salto de linea al final de cada renglon

    html_editado = tt.colocar_salto_linea(archivo_html)

    #Creamos el archivo
    indice_sup = len(nombre_archivo) - 4
    nombre = nombre_archivo[:indice_sup]
    direccion_nueva = "Canciones/" + nombre + "(incompleta).html"

    nuevo_archivo = open(direccion_nueva, "w")
    nuevo_archivo.writelines(html_editado)
    nuevo_archivo.close()


if __name__ == "__main__":
    main()
