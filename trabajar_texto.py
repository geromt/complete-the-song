#!/usr/bin/env python
# -*- coding: utf-8 -*-

#biblioteca para trabajar con textos

import random
import sys


def leer_archivo(nombre):
    '''Función para leer un archivo y acomodar su contenido en una lista por
    lineas. La función elimina el último elemento de la lista que está vacio y
    en caso de que el archivo esté vacio deja la lista vacia igualmente'''
    try:
        archivo = open(nombre, "r")
    except:
        print("No existe el archivo %s" % (nombre))
        sys.exit()

    lista = archivo.read().split("\n")

    return lista


def comprobar_ocurrencias(lista, patron):
    '''Función que busca elementos que coincidan con el patron. Devuelve en
    número de coincidencias encontradas'''
    ocu = 0
    for ele in lista:
        indice_sup = len(ele) - 1
        if ele[:indice_sup] == patron:
            ocu += 1

    return ocu


def dividir_renglones(texto):
    '''función para dividir cada renglon del texto en una lista
        texto >> objeto que referencia el archivo de texto'''
    texto_por_renglones = []

    hecho = True
    valor = 0
    while hecho:
        '''bucle para agregar cada renglon a la lista hasta donde ya no
        encuentre más'''
        texto_por_renglones.append(texto.readline())
        if not texto_por_renglones[valor]:
            hecho = False
        valor += 1

    return texto_por_renglones


def sep_palabras(texto):
    '''funcion para separar todas las palabras de una oración y acomodarlas en
    una lista anidada por frases
        texto = lista de oraciones'''

    texto_separado = []
    for renglon in range(len(texto)):
        frase_separada = []
        indice_inferior = 0
        for letra in range(len(texto[renglon])):
            if texto[renglon][letra] == " ":
                indice_superior = letra + 1
                palabra = ""
                for caracter in range(indice_inferior, indice_superior):
                    palabra += texto[renglon][caracter]
                indice_inferior = indice_superior
                frase_separada.append(palabra)
            elif texto[renglon][letra] == "\n":
                indice_superior = letra
                palabra = ""
                for caracter in range(indice_inferior, indice_superior):
                    palabra += texto[renglon][caracter]
                indice_inferior = indice_superior
                frase_separada.append(palabra)

        texto_separado.append(frase_separada)

    return texto_separado


def quitar_palabras_azar(texto_separado, numero_palabras_quitar):
    '''función para cambiar palabras al azar de una lista de palabras por el
    simbolo "0"
        texto_separado = lista de palabras. Pueden ser listas de palabras
            anidadas
        número_palabras_quitar = el número de palabras que deseas quitar por
            oracion en la lista'''
    for frase in range(len(texto_separado)):
        numero_palabras = len(texto_separado[frase])

        #comprobar si el número de palabras a quitar no es mayor que el número
        #de palabras en la  lista
        #####REVISIÓN
        if numero_palabras < numero_palabras_quitar:
            numero_palabras_quitar_nuevo = numero_palabras
        else:
            numero_palabras_quitar_nuevo = numero_palabras_quitar

        lista_quitadas = []
        for palabras in range(numero_palabras_quitar_nuevo):

            hecho = True
            while hecho:
                #Comprobar si no hay posiciones repetidas si las hay este bucle
                #se repite generando otra posición al azar
                posicion = random.randrange(numero_palabras)
                repetido = 0

                for quitadas in lista_quitadas:
                    if posicion == quitadas:
                        repetido += 1

                if repetido == 0:
                    hecho = False

            #sustituimos la palabra por el simbolo "0 "
            texto_separado[frase][posicion] = ("0 ")
            lista_quitadas.append(posicion)

    return texto_separado


def colocar_salto_linea(texto):
    '''colocará un salto al final de cada linea'''
    nuevo_texto = []
    for frase in range(len(texto)):
        nueva_frase = texto[frase]
        nueva_frase += "\n"
        nuevo_texto.append(nueva_frase)

    return nuevo_texto
