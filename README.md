# Gestión de Datos de Países en Python
## Trabajo Práctico Integrador - Programación 1
### Tecnicatura Universitaria en Programación - UTN (Facultad Regional Chubut)

[cite_start]Este proyecto consiste en una aplicación de consola desarrollada en Python que permite la gestión, filtrado y análisis estadístico de un dataset de países cargado desde un archivo CSV. El sistema aplica conceptos fundamentales de programación como estructuras de datos (listas y diccionarios), modularización y algoritmos de ordenamiento.

---

## 👥 Integrantes
* **Soledad Ortiz** - [Enlace a Perfil de GitHub]
* **Chritian Nicolás Leiva** - [[Enlace a Perfil de GitHub](https://github.com/ChristianLeiva)]

---

## 📄 Documentación y Video
* [cite_start]**Video Demostrativo:** [Insertar Link aquí] (Duración: 10-15 min) [cite: 112, 126]
* [cite_start]**Informe Técnico (PDF):** [Enlace al PDF o ver archivo en la raíz] [cite: 127]

---

## 🚀 Funcionalidades Principales
[cite_start]El sistema ofrece un menú interactivo con las siguientes capacidades[cite: 55, 56]:

1.  [cite_start]**Gestión de Datos:** Agregar nuevos países y actualizar población o superficie de registros existentes[cite: 57, 58].
2.  [cite_start]**Búsqueda:** Localización de países por nombre (coincidencia exacta o parcial)[cite: 59].
3.  [cite_start]**Filtrado Avanzado:** Por continente, rango de población y rango de superficie[cite: 60, 62, 63, 64].
4.  [cite_start]**Ordenamiento:** Listado alfabético o numérico (por población/superficie) de forma ascendente o descendente[cite: 65, 69, 70, 71].
5.  [cite_start]**Estadísticas:** * País con mayor y menor población[cite: 73].
    * [cite_start]Promedios de población y superficie[cite: 75, 82].
    * [cite_start]Conteo de países por continente[cite: 83].

---

## 🛠️ Tecnologías Utilizadas
* [cite_start]**Lenguaje:** Python 3.x[cite: 15].
* [cite_start]**Persistencia:** Lectura y manejo de archivos CSV[cite: 17, 91].
* [cite_start]**Estructuras:** Listas y Diccionarios para la manipulación en memoria[cite: 16].

---

## 💻 Instrucciones de Uso

### Requisitos Previos
Tener instalado Python 3.x en su sistema.

### Instalación y Ejecución
1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/usuario/nombre-repositorio.git](https://github.com/usuario/nombre-repositorio.git)

2. Navegar a la carpeta del proyecto:
    ```bash
    cd nombre-repositorio

3. Ejecutar el programa:
    ```bash
    python main.py

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
* **Validaciones:** Asegúrate de que tu código maneje errores de formato en el CSV y entradas inválidas del usuario, tal como pide la consigna[cite: 84, 85].
* **Modularización:** Recuerda que cada función debe tener una sola responsabilidad (una función = una responsabilidad).
* **Video:** Verifica que el enlace al video tenga permisos públicos antes de realizar la entrega final[cite: 126].
