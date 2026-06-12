import csv

#Variable global
archivo = 'datos.csv'

#Definir funciones
def cargar_datos_csv(nombre_archivo):
    """
    Lee el archivo CSV y carga los países en una lista de diccionarios.
    Maneja errores si el archivo no existe o tiene un formato incorrecto.
    """
    lista_paises = []
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    # Convertimos los datos numéricos a enteros como pide la consigna
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }
                    lista_paises.append(pais)
                except (ValueError, KeyError):
                    print(f"Advertencia: Fila omitida por error de formato o datos faltantes: {fila}")
                    
        print(f"¡Éxito! Se cargaron {len(lista_paises)} países correctamente.")
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado. Verifique la ruta.")
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer el archivo: {e}")
        
    return lista_paises

def mostrar_menu():
    print("Menú de opciones:")
    print("1. Agregar nuevo país")
    print("2. Actualizar datos población/superficie de un país")
    print("3. Buscar país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Salir")

def agregar_pais(lista_paises):
    """
    Pide al usuario los datos de un nuevo país, los valida 
    y los agrega a la lista global en formato de diccionario.
    """
    print("\n--- Registro de nuevo país ---")
    
    # 1. Validar el Nombre (que no esté vacío)
    nombre = input("Ingrese el nombre del país: ").strip()
    while not nombre:
        print("Error: El nombre no puede estar vacío.")
        nombre = input("Ingrese el nombre del país: ").strip()
        
    # 2. Validar la Población (Debe ser un entero positivo)
    while True:
        try:
            poblacion = int(input("Ingrese la cantidad de población: "))
            if poblacion >= 0:
                break
            else:
                print("Error: La población no puede ser un número negativo.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    # 3. Validar la Superficie (Debe ser un entero positivo)
    while True:
        try:
            superficie = int(input("Ingrese la superficie (en km²): "))
            if superficie >= 0:
                break
            else:
                print("Error: La superficie no puede ser un número negativo.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    # 4. Validar el Continente (que no esté vacío)
    continente = input("Ingrese el continente al que pertenece: ").strip()
    while not continente:
        print("Error: El continente no puede estar vacío.")
        continente = input("Ingrese el continente al que pertenece: ").strip()

    # 5. Crear el diccionario del nuevo país
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    # 6. Agregarlo a la lista global
    lista_paises.append(nuevo_pais)
    print(f"\n¡Éxito! '{nombre}' ha sido registrado correctamente en el sistema.")

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
