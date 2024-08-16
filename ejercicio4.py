"""
BRISEILY YAMILETH SOLORZANO HERNANDEZ ---- SMSS030723.
EJERCICIO 4.
ALMACEN DE VENTA DE DISPOSITIVOS ELECTRONICOS
"""

class DispositivoElectronico:
    def __init__(self, tipo, precio_compra, caracteristicas):
        self.tipo = tipo  # Tipo de dispositivo: Celular, Tablet o Portátil.
        self.marca = "PHR"  # Todos los dispositivos son de la marca PHR.
        self.precio_compra = precio_compra  # Precio de compra.
        self.caracteristicas = caracteristicas  # Lista de 6 características del dispositivo.
        self.precio_venta = self.calcular_precio_venta()  # Precio de venta calculado.
        self.origen = "Importado"  # Todos los dispositivos son importados.
        
        self.registrar_dispositivo()  # Método para registrar el dispositivo.
        
    def calcular_precio_venta(self):
        return round(self.precio_compra * 1.7, 2)  # Precio con margen de ganancia del 70%.
    
    def registrar_dispositivo(self):
        print(f"Registrando dispositivo {self.tipo} de la marca {self.marca}...")

    def mostrar_detalles(self):
        print(f"Dispositivo: {self.tipo} ({self.marca})")
        print(f" - Precio de Compra: ${self.precio_compra:.2f}")
        print(f" - Precio de Venta: ${self.precio_venta:.2f}")
        print(f" - Origen: {self.origen}")
        print(" - Principales Características:")
        for i, caracteristica in enumerate(self.caracteristicas, 1):
            print(f"   {i}. {caracteristica}")
        print("-----------------------")

class Almacen:
    def __init__(self):
        self.dispositivos = []  # Lista para almacenar dispositivos.
    
    def agregar_dispositivo(self, tipo, precio_compra, caracteristicas):
        nuevo_dispositivo = DispositivoElectronico(tipo, precio_compra, caracteristicas)
        self.dispositivos.append(nuevo_dispositivo)
        print(f"Dispositivo {tipo} registrado exitosamente.\n")
    
    def mostrar_inventario(self):
        if not self.dispositivos:
            print("No hay dispositivos registrados en el inventario.")
        else:
            for dispositivo in self.dispositivos:
                dispositivo.mostrar_detalles()
    
    def menu(self):
        print("¡Bienvenido al sistema de gestión del almacén de dispositivos electrónicos!\n")
        while True:
            print("1. Registrar un nuevo dispositivo")
            print("2. Mostrar inventario de dispositivos")
            print("3. Salir del sistema")
            opcion = input("Seleccione una opción(colocar el numero): ")
            
            if opcion == "1":
                tipo = input("Ingrese el tipo de dispositivo (Celular, Tablet, Portátil): ").capitalize()
                precio_compra = float(input("Ingrese el precio de compra del dispositivo: $"))
                
                print("A continuación, ingrese las 6 principales características del dispositivo:")
                caracteristicas = [input(f" - Característica {i + 1}: ") for i in range(6)]
                
                self.agregar_dispositivo(tipo, precio_compra, caracteristicas)
            
            elif opcion == "2":
                print("\nInventario de dispositivos registrados:")
                self.mostrar_inventario()
                print("-----------------------")
            
            elif opcion == "3":
                print("Gracias por utilizar el sistema. ¡Hasta pronto!")
                break
            
            else:
                print("Opción inválida. Por favor, intente de nuevo.")
                print("-----------------------")

# Ejecución directa del menú
almacen = Almacen()
almacen.menu()
