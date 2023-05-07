from alumno import Alumno
from manejadorAlumnos import Alumnos
from materiasAprobadas import MateriasAprobadas
from manejadorMateriasAp import ManjeadorMateriasAp
from menu import Menu


if __name__ == '__main__':
    arregloAlumnos = Alumnos()
    arregloAlumnos.testAlumnos()
    listaMaterias = ManjeadorMateriasAp()
    listaMaterias.test()
    menu = Menu()
    menu.opciones(listaMaterias, arregloAlumnos)
    