import csv
import numpy as np
from alumno import Alumno
from numpy import ndarray
import os

class Alumnos:
    __cantidad = 0
    __dimension: int
    __incremento = 5
    __alumnos: ndarray
    
    def __init__(self, dimension = 8, incremento = 5):
        self.__alumnos = np.empty(dimension, dtype = Alumno)
        self.__dimension = dimension
        self.__incremento = incremento
           
    def testAlumnos(self):
        cabecera = True
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__alumnos.resize(self.__dimension)

        with open("alumnos.csv","r") as file:
            reader = csv.reader(file, delimiter=';')
            for fila in reader:
                if cabecera:
                    cabecera = not cabecera
                else:
                    
                    self.__alumnos[self.__cantidad] = Alumno(fila[0], fila[1], fila[2], fila[3], int(fila[4]))
                    self.__cantidad += 1
        print('Los alumnos fueron cargados correctamente')
        return 
    
    def getUnAlumno(self, indice)->Alumno:
        return self.__alumnos[indice]
    
    def buscar_alumno(self, dni: str)->int:
        i=0
        while i < self.get_dimension() and self.__alumnos[i].get_dni() != dni:
            i+=1
        if i < self.__dimension:
            return i
            
    def ordenar(self)->list[Alumno]:
        return sorted(self.__alumnos)
    
    def get_dimension(self)->int:
        return self.__dimension
        