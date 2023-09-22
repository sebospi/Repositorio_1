#Programacion orientada a objetos 

#clases /  molde ( ejemplo: carro)
#objetos / representación ( ejemplo: BMW)
#instancias / invocar o creacion del objeto
#metodos / acciones que puede hacer un objeto ( ejemplo: moverse)
#atributos / caracteristicas ( ejemplo: # de puertas, color de carro, modelo, #sillas, motor,etc...)

#normas PEP 8

#Getter & setters: metodos para acceder o asignar un valor a los campos de un objeto
#metodo set= se usa para asignar valores al campo
#metodo get= se usa para obtener valores de campo 
#Ejemplos: setNombre() / getNombre()
#Ejmplo set:
#def setNombre(self,nombre:str):
    #self.__nombre= nombre
#las"__" significa campo privado, o sea que solo el programador puede acceder a la funcion 
#solo se puede modificar mediante funciones de set y get 

#Ejemplo get:
#def getNombre(self):
    #return self.nombre

class Estudiante:
    def __init__(self):
        self.nombre=None
        self.apellido=None
        self.edad=None
        self.nacionalidad='Colombia'

    def setNombre(self,nombre:str):
        self.nombre=nombre 
    
    def getNombre(self):
        return self.nombre
    
    def setApellido(self,apellido:str):
        self.apellido=apellido 
    
    def getApellido(self):
        return self.apellido
    
    def setEdad(self,edad:str):
        #self.__edad=edad
        if int(edad) > 21:
            self.__edad=edad
        else:
            self.__edad="menor de edad"
    
    def getEdad(self):
        return self.edad
    
    def setnacionalidad(self,nacionalidad:str):
        self._nacionalidad=nacionalidad 
    
    def getNacionalidad(self):
        return self.nacionalidad 
    
    def entender(self):
        return 'Si, aprendí mucho hoy :)'

    def __licor(self):
        edad=self.__edad
        if int(edad)>21:
            return "Puede beber una pola"
        elif edad=="menor de edad":
            return "Le toco un jugo"
    
    def getLicor(self):
        return self.__licor()
     

def main():
    estudiante=[]
    opc='n'
    while 1:
        est=Estudiante()
        #est.nombre=input('Nombre: ')
        #est.apellido=input('Apellido: ')
        #est.edad=input('Edad: ')
        #estudiante.append(est)
        est.setNombre=input('Nombre: ')
        est.setApellido=input('Apellido: ')
        est.setEdad=input('Edad: ')
        estudiante.append(est)
        opc=input('Desea salir? (y/n)')
        if opc=='y':
            break
        else:
            print('Invalido')
    
    print(f'-------Clase 2023-II -----\n')
    for i in estudiante:
        print(f'Nombre: {i.getNombre()} {i.getApellido()}\n\
            Edad: {i.getEdad()}\n\n')
        
        
if __name__=="__main__":
    main()


