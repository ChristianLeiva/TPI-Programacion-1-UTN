import csv

#Definir funciones

def cargar_cvs():
    pass

def mostrar_menu():
    pass

def capturar_opcion():
    pass

def calcular_estadísticas():
    pass

def ordenar_países():
    pass

def exportar_csv():
    pass

#Programa principal
datos = cargar_cvs()

while True:
    mostrar_menu()
    opcion= capturar_opcion()
    
    if opcion == 1:
        calcular_estadísticas()
    elif opcion == 2:
        ordenar_países()
    elif opcion == 3:
        exportar_csv()
    elif opcion == 4:
        print("Saliendo del programa...")
        break
