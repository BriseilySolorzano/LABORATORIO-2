"""
BRISEILY YAMILETH SOLORZANO HERNANDEZ ---- SMSS030723.
EJERCICIO 1.
VETERINARIA.
"""

class gato():
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre  # nombre del animal.
        self.raza = raza  # raza.
        self.edad = edad  # edad.
        self.peso = peso  # peso.
        self.tipo = self.det_tipo()  # llamamos a nuestra funcion.
        self.estado = self.estado()  # llamamos a nuestra funcion.
        
    def det_tipo(self):  # Función para el pes ( - de 10 kg o + de 10 kg) los guardara como "Gato Grande" o "Gato Pequeño".
        if self.peso < 10:
            return "Gato Pequeño"
        else:
            return "Gato Grande"
            
    def estado(self):  # Devuelve el estado.
        self.estado = "ATENDIDO"
        return self.estado
    
    def mostrar_datos(self):  # Función para mostrar los datos.
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")
        print(f"Peso: {self.peso} kg")
        print(f"Tipo: {self.tipo}")
        print(f"Estado: {self.estado}")
        print("-----------------------")
        
class veterinaria():  # Clase que nos permitirá realizar todas las opciones.
    def __init__(self):
        self.gatos = []  #  lista para almacenar.
    
    def registrar_gatos(self, nombre, raza, edad, peso):  # Función que registra los gatos en la lista.
        self.gatos.append(gato(nombre, raza, edad, peso))
        
    def mostrar(self):  # Función que muestra los datos.
        for i in self.gatos:  # Recorre la lista con un for.
            print("-----------------------")
            i.mostrar_datos()  # Llama a la función de la clase gato.
    
    def menu(self):  # Función que cumple el papel de menú.
        while True:
            print("1. Por favor registrar a su gato")
            print("2. Mostrar gatos")
            print("3. Salir")
            print("-----------------------")
            opcion = input("Ingrese una opción: ")  # Opciones para el usuario.
            match opcion:  # El resultado y ejecuta una sentencia distinta según el caso.
                case "1":
                    print("-----------------------")
                    nombre = input("Ingrese el nombre del gato: ")
                    raza = input("Ingrese la raza del gato: ")
                    edad = int(input("Ingrese la edad del gato: "))
                    peso = int(input("Ingrese el peso del gato: "))  # Obtenemos los datos.
                    self.registrar_gatos(nombre, raza, edad, peso)  # Le mandamos los parámetros necesarios.
                case "2":
                    print("-----------------------")
                    self.mostrar()  # Aquí mostramos los datos ya ordenados.
                case "3":
                    print("-----------------------")
                    print("Gracias por utilizar el sistema")
                    break  # Termina el programa.
                case _:
                    print("-----------------------")
                    print("Opción inválida")
                    continue  # Esto permite que aunque falle el programa se enviara un mensaje.
                    
veterinaria = veterinaria()  # Almacenamos en una variable a la clase.
veterinaria.menu()  # Llamamos al menú que es nuestra interfaz para comunicarnos con el usuario.
