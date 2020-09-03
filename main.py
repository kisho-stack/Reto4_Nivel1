class Persona():
    def __init__(self):
        self.nombre = input("Nombre :")
        self.dni = input("DNI :")
        self.edad = input("Edad :")
            
class Docente(Persona):
    def __init__ (self):
        print("Ingresar los datos del profesor")
        super().__init__()
        
class Alumno(Persona):
    def __init__ (self):
        print("Ingresar los datos del Alumno")
        super().__init__()
      
    def ingresar_notas(self):
        self.notas_lista = []
        contador = 1
        while contador <=4:
            notas = int(input("Ingresar notas del alumno :" ))
            contador = contador + 1
            self.notas_lista.append(notas)
            self.promedio = sum(self.notas_lista)//len(self.notas_lista)
            self.nota_min = min(self.notas_lista)
            self.nota_max = max(self.notas_lista)
        
              
class Archivo():
    def __init__(self, archivo_profesor,archivo_alumno):
        self.archivo_profesor = archivo_profesor
        self.archivo_alumno = archivo_alumno

    def agregar_profesor(self, profe):
        try:
            file = open(self.archivo_profesor, mode='a') 
            profe = f"""Datos del Profesor :
                          Nombre: {profe.nombre} 
                          DNI:    {profe.dni}
                          Edad:   {profe.edad}\n"""
            file.write(profe)
        except Exception as e: 
            print(f'{str(e)}')
        finally:
            if(file):
                file.close()
                print("Se guardaron los datos profesor")

    def agregar_alumno(self, alu):
        try:
            file = open(self.archivo_alumno, mode='a')
            alu = f"""Datos del Alumno :
                        Nombre:        {alu.nombre} 
                        DNI:           {alu.dni}
                        Edad:          {alu.edad}
                        Notas:         {alu.notas_lista}
                        Promedio:      {alu.promedio}
                        Nota Maxima:   {alu.nota_max}
                        Nota Minima:   {alu.nota_min}\n"""
            file.write(alu)
        except Exception as e:  
            print(f'{str(e)}')
        finally:
            if(file):
                file.close()
                print("Se guardaron los datos del alumno")            


profesor = Docente()
estudiante = Alumno()
estudiante.ingresar_notas()
archivo = Archivo("profesor.txt","alumno.txt")
archivo.agregar_profesor(profesor)
archivo.agregar_alumno(estudiante)