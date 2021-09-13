#Genero una lista para meterlo en la tupla que se nos pide en el ejecicio y me servira para crear la clave del punto 3
lista=[1,2,3,4,5]
#1.Genero la tupla con los 5 tipos de datos diferentes
tupla = ("Jorge", True, 12.56, 5, lista)
#2.Cambiamos de tupla a lista
list(tupla)
#3.Genero un diccionario
Diccionario = dict(zip(lista, tupla))