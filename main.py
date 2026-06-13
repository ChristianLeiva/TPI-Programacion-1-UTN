import csv

# Variable global con el nombre correcto del archivo
LISTA_PAISES = 'datos.csv'

# ==========================================
# DEFINICIÓN DE FUNCIONES
# ==========================================

def cargar_datos_csv(nombre_archivo):
    """
    Lee el archivo CSV y carga los países en una lista de diccionarios.
    Maneja errores si el archivo no existe o tiene un formato incorrecto.
    """
    lista_paises = []
    try:
        # Usamos 'as archivo_abierto' para no pisar el nombre de la variable 'nombre_archivo'
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo_abierto:
            lector = csv.DictReader(archivo_abierto)
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
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado. Asegúrate de que esté en la misma carpeta.")
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer el archivo: {e}")
        
    return lista_paises


def mostrar_menu():
    print("\n========================================")
    print("      SISTEMA DE GESTIÓN DE PAÍSES      ")
    print("========================================")
    print("1. Agregar un nuevo país")
    print("2. Actualizar datos de un país")
    print("3. Buscar un país")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas globales")
    print("7. Salir")
    print("========================================")


def agregar_pais(lista_paises):
    """Pide los datos de un nuevo país, los valida y los añade a la lista."""
    print("\n--- REGISTRO DE NUEVO PAÍS ---")
    
    # 1. Validar el Nombre (Que no esté vacío y que NO EXISTA previamente)
    while True:
        nombre = input("Ingrese el nombre del país: ").strip()
        
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
            continue

        pais_existente = False
        for pais in lista_paises:
            if pais["nombre"].lower() == nombre.lower():
                pais_existente = True
                break  # Encontramos un duplicado, cortamos el for
                
        if pais_existente:
            print(f"Error: El país '{nombre}' ya se encuentra registrado. Ingrese otro diferente.")
        else:
            break  # El nombre es válido y no está repetido, salimos del while

    # 2. Validar la Población
    while True:
        try:
            poblacion = int(input("Ingrese la cantidad de población: "))
            if poblacion >= 0:
                break
            print("Error: La población no puede ser un número negativo.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    # 3. Validar la Superficie
    while True:
        try:
            superficie = int(input("Ingrese la superficie (en km²): "))
            if superficie >= 0:
                break
            print("Error: La superficie no puede ser un número negativo.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    # 4. Validar el Continente
    continente = input("Ingrese el continente al que pertenece: ").strip()
    while not continente:
        print("Error: El continente no puede estar vacío.")
        continente = input("Ingrese el continente al que pertenece: ").strip()

    # 5. Crear el diccionario y agregarlo a la lista
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    lista_paises.append(nuevo_pais)
    print(f"\n¡Éxito! '{nombre}' ha sido registrado correctamente.")

def actualizar_datos(lista_paises):
    pass

def buscar_pais(lista_paises):
    pass

def filtrar_paises(lista_paises):
    pass

def ordenar_paises(lista_paises):
    pass

def mostrar_estadisticas(lista_paises):
    pass


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================
datos = cargar_datos_csv(LISTA_PAISES)

while True:
    mostrar_menu()
    try:
        opcion = int(input("Ingrese una opción (1-7): "))

        if opcion not in [1, 2, 3, 4, 5, 6, 7]:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 7.")
        else:
            if opcion == 1:
                agregar_pais(datos) 
            elif opcion == 2:
                actualizar_datos(datos)
            elif opcion == 3:
                buscar_pais(datos)
            elif opcion == 4:
                filtrar_paises(datos)
            elif opcion == 5:
                ordenar_paises(datos)
            elif opcion == 6:
                mostrar_estadisticas(datos)
            elif opcion == 7:
                print("\n¡Gracias por utilizar el sistema! Saliendo del programa...")
                break  # Rompe el bucle while e interrumpe el programa limpiamente
                
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")