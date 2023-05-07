class Alumno:
    __dni: str
    __apellido: str
    __nombre: str
    __carrera: str
    __año: int
    
    def __init__(self, dni = '', apellido = '', nombre = '', carrera = '', año = 0):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__año = año
        
    def __str__(self):
        return f'{self.__dni, self.__apellido, self.__nombre, self.__carrera, self.__año}'
    
    def get_dni(self)-> str:
        return self.__dni
    
    def get_nombre_completo(self)->str:
        return f'{self.__apellido} {self.__nombre}'
    
    def get_año(self)->int:
        return self.__año
    
    def __lt__(self, otroAlumno):
        valorRetorno = False
        if self.__año < otroAlumno.__año:
            valorRetorno = True
        elif self.__año == otroAlumno.__año:
            if self.__apellido < otroAlumno.__apellido:
                valorRetorno = True
            elif self.__apellido == otroAlumno.__apellido:
                if self.__nombre < otroAlumno.__nombre:
                    valorRetorno = True
                else:
                    valorRetorno = False
        return valorRetorno
        