import csv
from materiasAprobadas import MateriasAprobadas
from alumno import Alumno
from manejadorAlumnos import Alumnos

class ManjeadorMateriasAp:
    __materiasAprobadas = []
    
    def __init__(self):
        self.__materiasAprobadas = []
        
    def test(self):
        cabecera = True
        with open('materiasAprobadas.csv','r')as file:
            reader = csv.reader(file, delimiter = ';')
            for fila in reader:
                if cabecera:
                    cabecera = not cabecera
                else:
                    unaMateria = MateriasAprobadas(fila[0], fila[1], fila[2], int(fila[3]), fila[4])
                    self.__materiasAprobadas.append(unaMateria)
            print('Las materias fueron cargadas exitosamente')
            
    def promedioSinAplazo(self, dni):
        acumNotasAprobadas = 0
        contadorAp = 0
        for alumno in self.__materiasAprobadas:
            if alumno.get_dni() == dni:
                if alumno.get_nota() >= 7:
                    acumNotasAprobadas += alumno.get_nota()
                    contadorAp += 1
        if contadorAp != 0:
            promedio = acumNotasAprobadas/contadorAp
        else:
            promedio = -1
        return promedio

    def promedioConAplazo(self, dni):
        acumNotasTotales = 0
        contadorTot = 0
        for alumno in self.__materiasAprobadas:
            if alumno.get_dni() == dni:
                acumNotasTotales += alumno.get_nota()
                contadorTot += 1
        if contadorTot != 0:
            promedio = acumNotasTotales/contadorTot
        else:
            promedio = -1
        return promedio

    def comunicar_promedios(self):
        dni = input('Ingrese el DNI del alumno')
        print('Promedios del alumno con el dni {}'.format(dni))
        promedioSin = self.promedioSinAplazo(dni)
        promedioCon = self.promedioConAplazo(dni)
        if promedioSin != -1:
            print('Promedio sin aplazo: {}'.format(promedioSin))
        else: 
            print('El alumno no aprobo ninguna materia')
        if promedioCon != -1:
            print('Promedio con aplazo: {}'.format(promedioCon))
        else: 
            print('El alumno no rindió ninguna materia')
        
    def informarAprobados(self, nombreMateria, listaAlumnos: Alumnos):
        print('DNI     Apellido y nombre     Fecha     Nota     Año que cursa')
        print('---     -----------------     -----     ----     -------------')
        for materia in self.__materiasAprobadas:
            if materia.get_nombre() == nombreMateria:
                if materia.get_aprobación() == 'P':
                    if materia.get_nota() >= 7:
                        indice = listaAlumnos.buscar_alumno(materia.get_dni())
                        if indice is not None and indice < listaAlumnos.get_dimension():
                            unAlumno = listaAlumnos.getUnAlumno(indice)
                            print(f'{materia.get_dni()} {unAlumno.get_nombre_completo()} {materia.get_fecha()} {materia.get_nota()} {unAlumno.get_año()}')
                        
                        
            
            
    
    