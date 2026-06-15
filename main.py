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
    print("7. Mostrar lista de países")
    print("8. Salir")
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
    
    with open(LISTA_PAISES, 'a', encoding='utf-8', newline='') as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)       
        escritor.writerow(nuevo_pais)
        lista_paises.append(nuevo_pais)
    print(f"\n¡Éxito! '{nombre}' ha sido registrado correctamente.")

def actualizar_datos(lista_paises):
    pass

def buscar_pais(lista_paises):
    pass

def filtrar_paises(lista_paises):
    pass

def ordenar_paises(lista_paises):    
    if not lista_paises:
        print("Aviso: No hay países cargados en el sistema para ordenar.")
        return

    print("\n--- ORDENAR PAÍSES ---")
    print("1. Por Nombre (Alfabético)")
    print("2. Por Población")
    print("3. Por Superficie")
    print("4. Por Continente")
    print("5. Cancelar y volver al menú principal")
    
    opcion = input("Elija el criterio de ordenamiento (1-5): ").strip()
    
    if opcion == '5':
        return
        
    if opcion not in ['1', '2', '3', '4']:
        print("Error: Opción inválida.")
        return

    # Preguntamos el sentido del ordenamiento
    sentido = input("¿Desea ordenarlo de forma Ascendente (A) o Descendente (D)? ").strip().upper()
    while sentido not in ['A', 'D']:
        print("Error: Ingrese 'A' para Ascendente o 'D' para Descendente.")
        sentido = input("¿Desea ordenarlo de forma Ascendente (A) o Descendente (D)? ").strip().upper()
        
    # Si elige D, reverse será True. Si elige A, reverse será False.
    es_descendente = (sentido == 'D')

    # Aplicamos el sort con lambda dependiendo de la opción
    if opcion == '1':
        # x representa a cada diccionario (país) de la lista. x["nombre"] saca el valor de esa clave.
        lista_paises.sort(key=lambda x: x["nombre"], reverse=es_descendente)
        criterio = "Nombre"
    elif opcion == '2':
        lista_paises.sort(key=lambda x: x["poblacion"], reverse=es_descendente)
        criterio = "Población"
    elif opcion == '3':
        lista_paises.sort(key=lambda x: x["superficie"], reverse=es_descendente)
        criterio = "Superficie"
    elif opcion == '4':
        lista_paises.sort(key=lambda x: x["continente"], reverse=es_descendente)
        criterio = "Continente"

    print(f"\n¡Éxito! La lista de países ha sido ordenada por {criterio} de forma {'Descendente' if es_descendente else 'Ascendente'}.")

    mostrar_lista_paises(lista_paises)

def mostrar_estadisticas(lista_paises):
    pass

def mostrar_lista_paises(lista_paises):
    if not lista_paises:
        print("\nNo hay países registrados para mostrar.")
        return
    
    for p in range(len(lista_paises)):
    # Formateamos con comas y reemplazamos por puntos
        pob = f"{lista_paises[p]['poblacion']:,}".replace(',', '.')
        sup = f"{lista_paises[p]['superficie']:,}".replace(',', '.')
    
        # Imprimimos usando las variables ya formateadas
        print(f"{p+1}. {lista_paises[p]['nombre']} - Población: {pob} - Superficie: {sup} km² - Continente: {lista_paises[p]['continente']}")
# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================
datos = cargar_datos_csv(LISTA_PAISES)

while True:
    mostrar_menu()
    try:
        opcion = int(input("Ingrese una opción (1-8): "))

        if opcion not in [1, 2, 3, 4, 5, 6, 7, 8]:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 8.")
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
                mostrar_lista_paises(datos)
            elif opcion == 8:
                print("\n¡Gracias por utilizar el sistema! Saliendo del programa...")
                break  # Rompe el bucle while e interrumpe el programa limpiamente
                
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")