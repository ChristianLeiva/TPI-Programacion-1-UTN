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
    print("\n--- ACTUALIZACIÓN DE DATOS ---")
    #Pedir al usuario el nombre del país a actualizar
    país_actualizar= input("Ingrese el nombre del país a actualizar: ").strip()
    
    #Corroborar que el usuario no ingrese campos vacíos
    if not país_actualizar:
        print("Error: El nombre del país no puede estar vacío")
        return
    
    #Buscar país
    pais_encontrado= None
    for p in lista_paises:
        if país_actualizar.lower() == (p['nombre']).lower(): 
            pais_encontrado = p
            break
    
    if not pais_encontrado:
        print(f"El nombre del país {país_actualizar} no está registrado")
        return
    
    #Mostrar opciones
    print("¿Qué datos desea actualizar?")
    print("1. Actualizar población")
    print("2.Actualizar superfice")
    print("3.Actualzar población y superficie.")

    #Pedir dato y corroborar que se ingresó sea el tipo de dato pedido 
    try:
        opcion= int(input("Ingrese la opción elegida: "))
    except ValueError:
        print("Error: debe ingresar un número")
        return 
    
    #Se corrobora que la opción sea válida
    if opcion not in [1,2,3]:
        print("Error: Debe elegir una opción válida.") 
        return
    
    #Si la opción ingresada es 1 o 3
    if opcion == 1 or opcion == 3:
        print("\n--- Actualización de población ---")
        try:
            poblacion_actualizar= int(input("Ingrese el número de población actualizado: "))    #Pide el ingreso del dato  
            if poblacion_actualizar <= 0:                                                       #Verifica que sea mayor que 0
                print("Error: La población no puede ser igual o menor que 0.")
                return
            pais_encontrado['poblacion'] = poblacion_actualizar                                 #Reemplazar el valor la población establecido en el cvs por el ingresado por el usuario
            print(f"Se actualizó con éxito la población del país {país_actualizar}")
        except ValueError:
            print("Error: debe ingresa un número.")
    #Si la opción es 2 o 3
    if opcion == 2 or opcion == 3:
        print("\n--- Actualización de superficie ---")

        try:
            superficie_actualizar= int(input("Ingrese la superficie actualizada: "))    #Pide el valor del dato a actualizar
            if superficie_actualizar <= 0:                                              #Verifica que sea mayor que 0
                print("Error: La superficie no puede ser igual o menor que 0.")
                return

            pais_encontrado['superficie'] = superficie_actualizar                       #Reemplaza el valor de superficie establecido en el cvs por el ingresado por el usuario
            print(f"Se actualizó con éxito la superficie del país {país_actualizar}.")
        except ValueError:
            print("Error: debe ingresar un número.")
            return

def buscar_pais(lista_paises):
    #Crea la lista para guardar posibles oincidencias y pide el nombre del país a buscar
    coincidencias_p= []
    pais_buscar= input("Ingrese el nombre del país que desea buscar: ").strip()

    #Verifica que el dato no esté vacío
    if pais_buscar == "" :
        print("Error: No puede ingresar nombres vacíos.")
        return 

    #Busca la coincidencia 
    for p in lista_paises:
        if pais_buscar.lower() == (p['nombre']).lower():    #Si la coincdencia es exacta imprime la información del país 
            print(f"Información del país buscado: \n{p}")
            return p
        
        if pais_buscar.lower() in (p['nombre']).lower():    #Si la coincidencia es parcial agrega el país a la lista de coincidencias
            coincidencias_p.append(p)
    
    #Si hay elementos en la lista coincidencias_p, los imprime, de lo contrario envía un mensaje
    if coincidencias_p:                                     
        print(f"Se encontraron {len(coincidencias_p)} coincidencias parciales")
        for c in coincidencias_p:
            print(f"\n{c}")
    else:
        print("No se encontró ningún país con el nombre ingresado. Intente nuevamente.")


def filtrar_paises(lista_paises):
    #Mostrar opciones
    print("\n--- FILTRAR PAÍS POR CONTINENTE, RANGO DE POBLACIÓN O RANGO DE SUPERFICIE ---")
    print("1_Continente")
    print("2_Rango de población")
    print("3_Rango de superficie")
    
    #Pedir ingreso de opción y validar que se ingrese el tipo de dato pedido
    try:
        opcion= int(input("Ingrese la opción deseada:"))
    except ValueError:
        print("Error: debe ingresar un número.")
        return
    
    if opcion not in [1,2,3]:
        print("Error: Solo puede ingresar los números: 1, 2 o 3. Intente nuevamente.")
        return
    
    if opcion == 1:
        print("\n--- Eligió la opción de filtrar por continente ---")
        #Crea lista de continentes para agregar los países si se encuentran coincidencias
        lista_continentes= []
        f_continente= input("Ingrese el nombre del contienente: ").strip()
        
        #Corroborar el correcto ingreso del dato
        if not f_continente:
            print("Error: No puede ingresar un dato vacío. Intente nuevamente.")
            return
        
        if f_continente.isdigit():
            print("Error: No puede ingresar un número. Intente nuevamente.")
            return
        
        #Buscar el país y si se encuentra agragarlo a la lista 
        for p in lista_paises:
            if f_continente.lower() == (p['continente']).lower():
                lista_continentes.append(p)
        
        #Si la lista tiene elementos los imprime, de lo contrario devuelve un mensaje
        if lista_continentes != []:
            print(f"Paises filtrados por el continente de {f_continente}: {len(lista_continentes)} ")
            for p in lista_continentes:
                print(f"\n{p}")
        else:
            print(f"No se encontraron países en el continente {f_continente}")
    
        return lista_continentes
        
        

    elif opcion == 2:
        print("\n--- Eligió la opción de filtrar por rango de población ---")
        #Crea la lista de rango de población para agregar los países que estén en el rango ingresado
        lista_rango_poblacion= []

        #Se piden los rangos y se verifica que se ingrese el tipo de dato pedido
        try:
            f_rango_i= int(input("Ingrese el número de inicio del rango: "))
            f_rango_f= int(input("Ingrese el número de finalización del rango: "))
        except ValueError:
            print("Error: debe ingresar un número.")

        #Se corrobora que los valores sean lógicos
        if f_rango_i > f_rango_f:
            print("Error: el rango inical no puede ser mayor que el rango final.")
            return
        
        #Se busca la coincidencia de rangos y si se encuentra se agrega a la lista
        for p in lista_paises:
            if (p['poblacion']) >= f_rango_i and (p['poblacion']) <= f_rango_f:
                lista_rango_poblacion.append(p)

        #Si la lista tiene cargados elementos se los imprime, de lo contrario se envía un mensaje
        if lista_rango_poblacion:
            print(f"Se encontraron {len(lista_rango_poblacion)} países con el rango de población ingresado.")
            for p in lista_rango_poblacion:
                print(f"\n{p}")
        else:
            print("Error: El rango de población que ingresó no coincide con el de ningún país cargado.")
        
        return lista_rango_poblacion

    else:
        print("\n--- Eligió la opción de filtrar por rango de superficie ---")
        #Crea una lista de rango de superficie para ingresar los países que estén en el rango ingresado
        lista_rango_superficie= []

        #Se piden los rangos y se verifica que se ingrese el tipo de dato pedido
        try:
            f_rango_i= int(input("Ingrese el número de inicio del rango: "))
            f_rango_f= int(input("Ingrese el número de finalización del rango: "))
            
        except ValueError:
            print("Error: debe ingresar un número.")
        
        #Se busca la coincidencia de rangos y si se encuentra se agrega a la lista
        for p in lista_paises:
            if (p['superficie']) >= f_rango_i and (p['superficie']) <= f_rango_f:
                lista_rango_superficie.append(p)
        
        #Si la lista tiene cargados elementos se los imprime, de lo contrario se envía un mensaje
        if lista_rango_superficie:
            print(f"Se encontraron {len(lista_rango_superficie)} países con el rango de superficie ingresado.")
            for p in lista_rango_superficie:
                print(f"\n{p}")
        else:
            print("Error: El rango de superficie que ingresó no coincide con el de ningún país cargado.")
        return lista_rango_superficie

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
    """Calcula y muestra estadísticas sobre la lista de países."""
    if not lista_paises:
        print("Aviso: No hay datos para calcular estadísticas.")
        return

    # 1. País con más y menos población
    pais_mas_poblado = max(lista_paises, key=lambda x: x["poblacion"])
    pais_menos_poblado = min(lista_paises, key=lambda x: x["poblacion"])

    # 2. Promedio de superficie
    total_superficie = sum(pais["superficie"] for pais in lista_paises)
    promedio_superficie = total_superficie / len(lista_paises)

    # 3. Conteo por continente
    conteo_continentes = {}
    for pais in lista_paises:
        cont = pais["continente"]
        if cont in conteo_continentes:
            conteo_continentes[cont] += 1
        else:
            conteo_continentes[cont] = 1

    # --- MUESTRA EN CONSOLA ---
    print("\n--- ESTADÍSTICAS GLOBALES ---")
    print(f"País más poblado: {pais_mas_poblado['nombre']} ({pais_mas_poblado['poblacion']} hab.)")
    print(f"País menos poblado: {pais_menos_poblado['nombre']} ({pais_menos_poblado['poblacion']} hab.)")
    print(f"Promedio de superficie: {promedio_superficie:,.2f} km²")
    print("\nDistribución por continentes:")
    for continente, cantidad in conteo_continentes.items():
        print(f"- {continente}: {cantidad} país(es)")

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
