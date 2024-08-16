"""
BRISEILY YAMILETH SOLORZANO HERNANDEZ ---- SMSS030723.
EJERCICIO 5.
PROGRAMACION ORIENTADA A OBJETOS (POO)

Un programa para una escuela que es practicamente un sistema para almacenar los datos de los 
estudiantes, nombre, edad y si asistio a clases.
"""

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre  # Nombre del estudiante.
        self.edad = edad  # Edad del estudiante.
        self.grado = grado  # Grado escolar del estudiante.
        self.asistencia = False  # Estado de asistencia (por defecto no han asistido).

    def marcar_asistencia(self):# Cambia el estado de asistencia a True (presente).
        self.asistencia = True
        print(f"Asistencia marcada para {self.nombre}.\n")

    def mostrar_info(self):# Muestra la información del estudiante.
        estado_asistencia = "Presente" if self.asistencia else "Ausente"
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}") 
        print(f"Grado: {self.grado}")
        print(f"Asistencia: {estado_asistencia}")

class Escuela:
    def __init__(self):
        self.estudiantes = []  # Lista para almacenar estudiantes.

    def agregar_estudiante(self, nombre, edad, grado): # Crea un nuevo estudiante y lo agrega a la lista.
        nuevo_estudiante = Estudiante(nombre, edad, grado)
        self.estudiantes.append(nuevo_estudiante)
        print(f"Estudiante '{nombre}' ha sido registrado.\n")

    def mostrar_lista_estudiantes(self): # Muestra la lista de estudiantes registrados.
        if not self.estudiantes:
            print("No hay estudiantes registrados.")
        else:
            print("Lista de estudiantes:\n")
            for estudiante in self.estudiantes:
                estudiante.mostrar_info()  # Muestra la información de cada estudiante.
            print("-----------------------")

    def marcar_asistencia_estudiante(self, nombre): # Busca al estudiante por nombre y marca su asistencia.
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre:
                estudiante.marcar_asistencia()
                break
        else:
            print(f"Estudiante '{nombre}' no encontrado.\n")

# Ejecución directa del menú
escuela = Escuela()

while True:
    print("1. Registrar un nuevo estudiante")
    print("2. Mostrar lista de estudiantes")
    print("3. Marcar asistencia de un estudiante")
    print("4. Salir")
    opcion = input("Seleccione una opción(colocar numero):  ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        grado = input("Ingrese el grado del estudiante: ")
        escuela.agregar_estudiante(nombre, edad, grado)

    elif opcion == "2":
        escuela.mostrar_lista_estudiantes()

    elif opcion == "3":
        nombre = input("Ingrese el nombre del estudiante para marcar asistencia: ")
        escuela.marcar_asistencia_estudiante(nombre)

    elif opcion == "4":
        print("Gracias por utilizar el sistema de la escuela. ¡Hasta pronto!")
        break

    else:
        print("Opción inválida. Por favor, intente de nuevo.\n")
