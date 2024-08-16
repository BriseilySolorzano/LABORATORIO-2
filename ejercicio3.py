"""
BRISEILY YAMILETH SOLORZANO HERNANDEZ ---- SMSS030723.
EJERCICIO 3.
CARROS.
"""

class Carro:
    def __init__(self, tipo, precio_compra, cualidades):
        self.tipo = tipo  # Tipo de vehículo (Nacional o Importado).
        self.precio_compra = precio_compra  # Precio de compra.
        self.cualidades = cualidades  # Lista de cualidades del vehículo.
        self.precio_venta = self.calcular_precio_venta()  # Precio de venta calculado.
        self.ruedas = 4  # Todos los vehículos tienen 4 ruedas.
        self.capacidad = 5  # Todos los vehículos tienen capacidad para 5 pasajeros.
        
    def calcular_precio_venta(self):
        return self.precio_compra * 1.40  # Margen de ganancia del 40%.
    
    def mostrar_datos(self):  # Función para mostrar los datos.
        print(f"Tipo: {self.tipo}")
        print(f"Precio de Compra: {self.precio_compra} $")
        print(f"Precio de Venta: {self.precio_venta:.2f} $")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad: {self.capacidad} pasajeros")
        print("Cualidades:")
        for cualidad in self.cualidades:
            print(f"- {cualidad}")
        print("-----------------------")

class Concesionario:  # Clase que nos permitirá realizar todas las opciones.
    def __init__(self):
        self.carros = []  # Lista para almacenar vehículos.
    
    def registrar_carro(self, tipo, precio_compra, cualidades):  # Función que registra vehículos en la lista.
        self.carros.append(Carro(tipo, precio_compra, cualidades))
        
    def mostrar(self):  # Función que muestra los datos.
        for carro in self.carros:  # Recorre la lista con un for.
            print("-----------------------")
            carro.mostrar_datos()  # Llama a la función de la clase Carro.
    
    def menu(self):  # Función que cumple el papel de menú.
        while True:
            print("1. Registrar un vehículo")
            print("2. Mostrar vehículos")
            print("3. Salir")
            print("-----------------------\n")
            print("Bienvenidos a nuestro sistema")
            opcion = input("Favor ingrese el numero de su opcion: ")  # Opciones para el usuario.
            match opcion:  # El resultado y ejecuta una sentencia distinta según el caso.
                case "1":
                    print("-----------------------")
                    tipo = input("Ingrese el tipo de vehículo (Nacional o Importado): ").capitalize()
                    precio_compra = float(input("Ingrese el precio de compra: "))
                    cualidades = []
                    print("Ingrese las primeras 10 cualidades del vehículo:")
                    for i in range(10):
                        cualidad = input(f"Cualidad {i + 1}: ")
                        cualidades.append(cualidad)
                    self.registrar_carro(tipo, precio_compra, cualidades)  # Le mandamos los parámetros necesarios.
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
                    continue  # Esto permite que aunque falle el programa se enviará un mensaje.

concesionario = Concesionario()  # Almacenamos en una variable a la clase.
concesionario.menu()  # Llamamos al menú que es nuestra interfaz para comunicarnos con el usuario.

