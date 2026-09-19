productos = [
    {"nombre": "Laptop", "precio": 1200, "stock": 15},
    {"nombre": "Mouse", "precio": 25, "stock": 5},
    {"nombre": "Teclado", "precio": 75, "stock": 25},
    {"nombre": "Monitor", "precio": 300, "stock": 8}
]

# productos_bajo_stock = [] #crea una lista vacia para almacenar los productos con bajo stock 
# for producto in productos: #recorre la lista de productos, en cada iteracion, el producto actual se almacena en la variable "producto"
#     print(f"Producto: {producto['nombre']}, Precio: ${producto['precio']}") #imprime la informacion del producto
#     if producto['stock'] < 10: #verifica si el stock del producto es menor a 10
#         productos_bajo_stock.append(producto) #agrega el producto a la lista de productos con bajo stock si cumple la condicion

# print("\nProductos con bajo stock:") #imprime un mensaje indicando que se mostraran los productos con bajo stock
# print(productos_bajo_stock)#imprime la lista de productos con bajo stock

#def calcular_promedio_precio(lista): #define una funcion que recibe una lista de productos y calcula el precio promedio
    #if not lista: #verifica si la lista esta vacia, si es asi, retorna 0
       # return 0 #retorna 0 si la lista esta vacia
    #total_precio = sum(p['precio'] for p in lista) #calcula la suma de los precios de todos los productos en la lista utilizando una expresion generadora, sum es una funcion incorporada que devuelve la suma de los elementos de un iterable 
                                                #p es una variable que representa cada producto en la lista, p['precio'] accede al precio del producto actual
    #return total_precio / len(lista) #retorna el precio promedio dividiendo la suma total de los precios entre la cantidad de productos en la lista, len es una funcion incorporada que devuelve el numero de elementos en un objeto


#precio_promedio = calcular_promedio_precio(productos) #calcula el precio promedio de los productos, precio_promedio almacena el resultado de la funcion calcular_promedio_precio, que recibe la lista de productos como argumento
#print(f"\nEl precio promedio de los productos es: ${precio_promedio:.2f}") #imprime el precio promedio con dos decimales

# import csv

# productos_desde_csv = []

# with open('datos.csv', mode='r', encoding='utf-8') as archivo_csv:
#     lector_diccionario = csv.DictReader(archivo_csv)

#     for fila in lector_diccionario:
#         fila['id'] = int(fila['id'])
#         fila['precio'] = int(fila['precio'])
#         fila['stock'] = int(fila['stock'])

#         productos_desde_csv.append(fila)

# print("\nLista de productos desde el archivo CSV:")

# for producto in productos_desde_csv:#el for recorre la lista de productos obtenidos 
#                                     #desde el archivo CSV, en cada iteracion, el producto actual 
#                                     #se almacena en la variable "producto"
#     print(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Precio: ${producto['precio']} | Stock: {producto['stock']}")
#     #imprime la informacion del producto, accediendo a los valores de cada clave en el diccionario "producto"

import csv 
import json 
 
def calcular_promedio_precio(lista): 
    if not lista: 
        return 0 
    total_precio = sum(p['precio'] for p in lista) 
    return total_precio / len(lista) 
 
 
# ----- Bloque 1 y 2: Manipulación de Datos en memoria y CSV ----- 
productos_desde_csv = [] 
try: 
    with open('datos.csv', mode='r', encoding='utf-8') as archivo_csv: 
        lector_diccionario = csv.DictReader(archivo_csv) 
        for fila in lector_diccionario: 
            fila['id'] = int(fila['id']) 
            fila['precio'] = int(fila['precio']) 
            fila['stock'] = int(fila['stock']) 
            productos_desde_csv.append(fila) 
except FileNotFoundError: 
    print("Error: El archivo 'datos.csv' no se encontró.") 
 
# ----- Bloque 3: Conversión a JSON y Validación ----- 
# if productos_desde_csv: 
#     datos_json = json.dumps(productos_desde_csv, indent=4) 
#     with open('salida.json', 'w') as archivo_salida: 
#         archivo_salida.write(datos_json) 
         
#     print("\nArchivo 'salida.json' creado con éxito.") 
     
#     print("\n--- Ejecutando el validador ---") 
#     datos_validados = validar_datos('salida.json') 
#     if datos_validados: 
#         print("Datos validados correctamente:", datos_validados)

# comento temporalmente la parte de validacion para poder ejecutar el programa con el error, ya que el archivo salida.json tiene un precio no numerico

# Modularización = dividir el programa en archivos/módulos según su responsabilidad.
# En este caso:
# app.py = programa principal.
# validar_productos.py = se encarga de validar productos.