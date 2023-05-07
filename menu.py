from alumno import Alumno
from manejadorAlumnos import Alumnos
from materiasAprobadas import MateriasAprobadas
from manejadorMateriasAp import ManjeadorMateriasAp
import numpy as np

class Menu:
    __cod: int
    
    def __init__(self, codigo = 0):
        self.__cod = codigo
        
    def opciones(self, materias:ManjeadorMateriasAp, alumnos:Alumnos):
        print('Opción 1: informar el promedio con aplazos y sin aplazos de un alumno')
        print('Opción 2: informar los estudiantes de una materia que la aprobaron en forma promocional, con nota mayor o igual que 7')
        print('Opción 3: Obtener listado ordenado de alumnos')
        print('Opción 0: finalizar')
        print('')
        self.__cod = int(input('Ingrese el código'))
        while self.__cod != 0:
            if self.__cod == 1:
                materias.comunicar_promedios()

            elif self.__cod == 2:
                materia = input('Ingrese el nombre de una materia')
                materias.informarAprobados(materia, alumnos)

            elif self.__cod == 3:
                lista = alumnos.ordenar()
                for alumno in lista:
                    print(alumno)

            else: 
                print('Codigo incorrecto')

            print('Opción 1: informar el promedio con aplazos y sin aplazos de un alumno')
            print('Opción 2: informar los estudiantes de una materia que la aprobaron en forma promocional, con nota mayor o igual que 7')
            print('Opción 3: Obtener listado ordenado de alumnos')
            print('Opción 0: finalizar')
            print('')
            self.__cod = int(input('Ingrese el código'))
        return
    