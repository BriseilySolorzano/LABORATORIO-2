"""
BRISEILY YAMILETH SOLORZANO HERNANDEZ ---- SMSS030723.
EJERCICIO 2.
PAPELERIA.
"""

class Articulo:
    def __init__(self, tipo, precio_compra, cantidad):
        self.tipo = tipo  # Tipo de artículo (cuaderno o lápiz).
        self.precio_compra = precio_compra  # Precio de compra.
        self.cantidad = cantidad  # Cantidad de artículos.
        self.precio_venta = self.calcular_precio_venta()  # Precio de venta calculado.
        
    def calcular_precio_venta(self):
        return self.precio_compra * 1.30  # Margen de ganancia del 30%.
    
    def mostrar_datos(self):  # Función para mostrar los datos.
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {'HOJITA' if self.tipo == 'Cuaderno' else 'RAYA'}")
        print(f"Precio de Compra: {self.precio_compra} $")
        print(f"Precio de Venta: {self.precio_venta:.2f} $")
        print(f"Cantidad: {self.cantidad}")
        print("-----------------------")

class Papeleria:  # Clase que nos permitirá realizar todas las opciones.
    def __init__(self):
        self.articulos = []  # Lista para almacenar artículos.
    
    def registrar_articulo(self, tipo, precio_compra, cantidad):  # Función que registra artículos en la lista.
        self.articulos.append(Articulo(tipo, precio_compra, cantidad))
        
    def mostrar(self):  # Función que muestra los datos.
        for articulo in self.articulos:  # Recorre la lista con un for.
            print("-----------------------")
            articulo.mostrar_datos()  # Llama a la función de la clase Articulo.
    
    def menu(self):  # Función que cumple el papel de menú.
        while True:
            print("-----------------------")
            print("1. Registrar un artículo")
            print("2. Mostrar artículos")
            print("3. Salir")
            print("-----------------------")
            print("Bienvenidos a nuestro sistema\n") 
            opcion = input("Por favor ingrese una opción (colocar el numero): ")  # Opciones para el usuario.
            match opcion:  # El resultado y ejecuta una sentencia distinta según el caso.
                case "1":
                    print("-----------------------")
                    tipo = input("Ingrese el tipo de artículo (Cuaderno - Lápiz): ").capitalize()
                    if tipo == "Cuaderno":
                        hojas = int(input("Ingrese la cantidad de hojas (50 - 100): "))
                        if hojas < 50 or hojas > 100:
                            print("Cantidad de hojas inválida")
                            continue
                    elif tipo == "Lapiz":
                        tipo_lapiz = input("Ingrese el tipo de lápiz (Colores - Grafito): ").capitalize()
                        if tipo_lapiz not in ["Colores", "Grafito"]:
                            print("Tipo de lápiz inválido")
                            continue
                    else:
                        print("Tipo de artículo inválido")
                        continue
                    precio_compra = float(input("Ingrese el precio de compra: "))
                    cantidad = int(input("Ingrese la cantidad: "))
                    self.registrar_articulo(tipo, precio_compra, cantidad)  # Le mandamos los parámetros necesarios.
                case "2":
                    print("-----------------------")
                    self.mostrar()  # Aquí mostramos los datos ya ordenados.
                case "3":
                    print("-----------------------")
                    print("Gracias por utilizar nuestro sistema")
                    print("Feliz dia!")
                    break  # Termina el programa.
                case _:
                    print("-----------------------")
                    print("Opción inválida")
                    continue  # Esto permite que aunque falle el programa se enviará un mensaje.

papeleria = Papeleria()  # Almacenamos en una variable a la clase.
papeleria.menu()  # Llamamos al menú que es nuestra interfaz para comunicarnos con el usuario.
