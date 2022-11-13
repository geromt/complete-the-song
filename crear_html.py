#!/usr/bin/env python
# -*- coding: utf-8 -*-

#funciones que crearań un archivo HTML a partir de un archivo de texto

import os

def crear_html(nombre, texto, video):
    '''creará un archivo html a partir de una lista anidada de oraciones, cada
    oración dividida en lista de palabras
        nombre = nombre del archivo a ser creado
        texto = lista de oraciones'''

    #variables
    lista_archivo = []
    nombre_editado = os.path.splitext(nombre)[0].replace("_", " ").title()
    titulo = "<title>" + nombre_editado + "</title>"

    #CREACIÓN DEL ARCHIVO LÍNEA POR LÍNEA
    lista_archivo.append("<!DOCTYPE html>")
    lista_archivo.append("<html>")

    #encabezado del archivo
    lista_archivo.append("<head>")
    lista_archivo.append(titulo)
    lista_archivo.append("<meta charset=\"utf-8\">")
    lista_archivo.append('''<link rel=\"stylesheet\" hype=\"text/css\" href=\"
    estilos.css\">''')
    lista_archivo.append("</head>")

    #cuerpo del archivo
    lista_archivo.append("<body>")
    #Capa del título
    lista_archivo.append("<div class=\"titulo\">")
    lista_archivo.append("<h1>" + nombre_editado + "</h1>")
    lista_archivo.append("</div>")
    #Capa para el formulario
    lista_archivo.append("<div class=\"contenido\">")
    lista_archivo.append("<form>")
    lista_archivo.append("<p>")
    #edición y adición del texto
    for frase in range(len(texto)):
        if len(texto[frase]) > 1:
            nueva_frase = "<label>"
            for palabra in range(len(texto[frase])):
                if texto[frase][palabra] == "0 ":
                    nueva_frase += "<input type=\"text\">"
                else:
                    nueva_frase += texto[frase][palabra] + " "
            nueva_frase += "</label><br>"
        else:
            nueva_frase = "<br><br>"
        lista_archivo.append(nueva_frase)

    #cerrar capa formulario
    lista_archivo.append("</p>")
    lista_archivo.append("</form>")
    lista_archivo.append("</div>")
    #añadir capa de video
    lista_archivo.append("<div class=\"contenido\">")
    lista_archivo.append(video)
    lista_archivo.append("</div>")
    lista_archivo.append("</body>")

    lista_archivo.append("</html>")

    return lista_archivo
