# Gestión de Datos de Países en Python
## Trabajo Práctico Integrador - Programación 1
### Tecnicatura Universitaria en Programación - UTN (Facultad Regional Chubut)

 Este proyecto consiste en una aplicación de consola desarrollada en Python que permite la gestión, filtrado y análisis estadístico de un dataset de países cargado desde un archivo CSV. El sistema aplica conceptos fundamentales de programación como estructuras de datos (listas y diccionarios), modularización y algoritmos de ordenamiento.

---

## 👥 Integrantes
* **Soledad Ortiz** - [Enlace a Perfil de GitHub]
* **Chritian Nicolás Leiva** - [[Enlace a Perfil de GitHub](https://github.com/ChristianLeiva)]

---

## 📄 Documentación y Video
* **Video Demostrativo:** [Insertar Link aquí] (Duración: 10-15 min)
* **Informe Técnico (PDF):** [Enlace al PDF o ver archivo en la raíz]

---

## 🚀 Funcionalidades Principales
El sistema ofrece un menú interactivo con las siguientes capacidades:

1.   **Gestión de Datos:** Agregar nuevos países y actualizar población o superficie de registros existentes.
2.   **Búsqueda:** Localización de países por nombre (coincidencia exacta o parcial).
3.   **Filtrado Avanzado:** Por continente, rango de población y rango de superficie.
4.   **Ordenamiento:** Listado alfabético o numérico (por población/superficie) de forma ascendente o descendente.
5.   **Estadísticas:** * País con mayor y menor población.
    *  Promedios de población y superficie.
    *  Conteo de países por continente.

---

## 🛠️ Tecnologías Utilizadas
*  **Lenguaje:** Python.
*  **Persistencia:** Lectura y manejo de archivos CSV.
*  **Estructuras:** Listas y Diccionarios para la manipulación en memoria.

---

## 💻 Instrucciones de Uso

### Requisitos Previos
Tener instalado Python 3.x en su sistema.

### Instalación y Ejecución
1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/ChristianLeiva/TPI-Programacion-1-UTN.git]

2. Navegar a la carpeta del proyecto:
    ```bash
    cd TPI-Programacion-1-UTN.

3. Ejecutar el programa:
    ```bash
    main.py

📊 Ejemplos de Entrada y Salida
Carga de Datos (CSV)
El programa utiliza un archivo paises.csv con el siguiente formato:
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América

Interacción en Consola
Entrada: Seleccionar opción "Filtrar por Continente" e ingresar "América".
Salida: Listado detallado de todos los países pertenecientes al continente americano presentes en el dataset.

📂 Estructura del Repositorio
main.py: Punto de entrada de la aplicación.


funciones.py: Módulos con la lógica de negocio (filtros, ordenamientos, etc.).


paises.csv: Dataset base de países.


Documentacion_TPI.pdf: Informe académico completo.

README.md: Este archivo.


### Notas adicionales para tu entrega:
* **Validaciones:** Asegúrate de que tu código maneje errores de formato en el CSV y entradas inválidas del usuario, tal como pide la consigna.
* **Modularización:** Recuerda que cada función debe tener una sola responsabilidad (una función = una responsabilidad).
* **Video:** Verifica que el enlace al video tenga permisos públicos antes de realizar la entrega final.
