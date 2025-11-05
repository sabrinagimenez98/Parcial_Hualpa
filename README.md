# Parcial_Hualpa
# Sistema Jerárquico de Datos con Recursividad y CSV

# Descripción del Proyecto

Este proyecto implementa una aplicación en Python que gestiona datos organizados jerárquicamente utilizando carpetas y archivos CSV. La estructura refleja un modelo de **Continente > País > Ciudad**, permitiendo almacenar, consultar, modificar y eliminar ítems de forma persistente.

Se utiliza **recursividad** para recorrer toda la jerarquía de carpetas y consolidar los datos en una única estructura para su procesamiento.

## Estructura Jerárquica

La jerarquía se representa directamente en el sistema de archivos:

datos/ 
├── América/ 
│ └── Argentina/ 
│  ├── Córdoba.csv 
│  ├── Buenos Aires.csv 
├── Europa/ 
│ └── España/ 
│  ├── Madrid.csv 
│  ├── Barcelona.csv 
│ └── Italia/ 
│  ├── Nápoles.csv

Cada archivo CSV contiene ítems individuales representados como diccionarios en Python, con atributos como `nombre`, `poblacion` y `superficie`.

## Funcionalidades

- **Alta de ítems**: Inserta nuevos datos creando carpetas y archivos si no existen.
- **Lectura global**: Recorre toda la jerarquía con recursividad y muestra todos los ítems.
- **Filtrado**: Permite buscar ítems por atributos como nombre o población.
- **Modificación**: Actualiza atributos de ítems existentes.
- **Eliminación**: Borra ítems y actualiza el archivo correspondiente.
- **Estadísticas**: Muestra cantidad total, suma y promedio de población, y conteo por continente.
- **Ordenamiento**: Permite ordenar los ítems por nombre, población o superficie.

## Tecnologías Utilizadas

- Python 3.x
- Librerías estándar: `os`, `csv`
- Estructuras: listas, diccionarios

## Instalación y Uso

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/jerarquia-datos.git
   cd jerarquia-datos

2. Ejecutar el programa:
python main.py

3. Seguir el menú interactivo para gestionar los ítems.

🎥 Video Explicativo

Contenido: Diseño jerárquico, estructura de carpetas, funcionamiento del programa y ejemplo de uso.

Enlace video explicativo: https://youtu.be/mrn7JNnq7Z4

👥 Equipo de Trabajo

Sabrina [UTN Mendoza]

Ismael [UTN Mendoza]

📌 Conclusión 
Este proyecto demuestra el uso de recursividad, persistencia y diseño jerárquico aplicado a datos reales. Es una base sólida para sistemas más complejos como gestores de inventario, catálogos geográficos o bases de datos distribuidas.
En conclusion, con esta segunda parte del segundo parcial pudimos aplicar en su totalidad todos los contenidos vistos durante el cursado de la materia de Programacion uno, como tambien tuvimos que saber organizar nuestros tiempos para llegar a todas las entregas de manera exitosa. 