class MateriasAprobadas:
    __dni: str
    __nombre: str
    __fecha: str
    __nota: int
    __aprobación: str
    
    def __init__(self, dni = '', nombre = '', fecha = '', nota = 0, aprobación = ''):
        self.__dni = dni
        self.__nombre = nombre
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobación = aprobación
        
    def get_dni(self)->str:
        return self.__dni
    
    def get_nombre(self)->str:
        return self.__nombre
    
    def get_fecha(self)->str:
        return self.__fecha
    
    def get_aprobación(self)->str:
        return self.__aprobación
    
    def get_nota(self)->int:
        return self.__nota