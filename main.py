import csv

#Variable global
archivo = 'datos.csv'

#Definir funciones
def cargar_csv():
    datos = []
    with open(archivo, 'r') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append(fila)
    return datos

def mostrar_menu():
    print("Menú de opciones:")
    print("1. Agregar nuevo país")
    print("2. Actualizar datos población/superficie de un país")
    print("3. Buscar país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Salir")

def agregar_país():
    pass

def actualizar_datos():
    pass

def buscar_país():
    pass

def filtrar_países():
    pass

def ordenar_países():
    pass

def mostrar_países():
    pass


#Programa principal
datos = cargar_cvs()

while True:
    mostrar_menu()
    try:
        opcion = int(input("Ingrese una opción (1-7): "))

        if opcion not in [1, 2, 3, 4, 5, 6, 7]:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 7.")
        
        else:
            if opcion == 1:
                agregar_país()
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                pass
            elif opcion == 6:
                pass
            else:
                print("Saliendo del programa...")
                break
            
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entre 1 y 7.")
