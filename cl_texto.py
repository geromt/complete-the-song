#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Clase texto


class Texto(object):
    '''Clase que contiene toda la información de un texto ya editado. Permite
    reeditar el texto rapidamente y de forma más eficaz. También guardará la
    información en archivos para ser consultados despues.'''

    def __init__(self, nombre):
        '''Constructor de la clase'''

        self.nombre = nombre
        self.direccion = "datos/" + self.nombre

    def escribir_archivo(self, video, texto):
        '''Este método guardará todos los datos del objeto para poder leerlos
        despues. video(str) >> dirección URL del video para ser embebido.
        texto(list) >> texto dividido en renglones y palabras'''
        self.video = video
        self.texto = texto
        archivo = open(self.direccion, "w") # crea el archivo
        archivo.write(self.video)
        archivo.write("\n")
        #archivo.writeline()
        for renglon in self.texto:
            for palabra in renglon:
                archivo.write(palabra + "\n")
            archivo.write("\n")

    def leer_archivo(self):
        '''método para leer el archivo que contiene la dirección del video y el
        texto dividido por frases y palabras'''
        archivo = open(self.direccion, "r")
        self.video = archivo.readline()
        self.texto = []
        hecho = True
        i = 0
        while hecho:
            self.texto.append([])
            renglon = True
            palabra = 0
            while renglon:
                self.texto[i].append(archivo.readline())

                if self.texto[i][palabra] == "\n" or not self.texto[i][palabra]:
                    renglon = False

                if len(self.texto[i][palabra]) > 1:
                    self.texto[i][palabra] = self.texto[i][palabra][:-1]
                palabra += 1

            if not self.texto[i][palabra - 1]:
                hecho = False

            i += 1
