### Trabajo Práctico N3

## Configuración del Programa

El programa está desarrollado en Python, un lenguaje de programación de alto nivel que permite una programación eficaz de scripts y un desarrollo rápido de aplicaciones en diversas áreas en una amplia variedad de plataformas.

El programa utiliza las bibliotecas `pandas`. `Pandas` se utiliza para la manipulación y análisis de datos, especialmente para la lectura y escritura de archivos CSV. 

***
## Iniciación
***
Se crea un nuevo directorio para el proyecto: Esto se puede hacer desde la terminal con el comando `mkdir nombre_del_proyecto`.
Se navega al nuevo directorio: Se usa el comando `cd nombre_del_proyecto`.
Se crea un entorno virtual: Es opcional, pero es una buena práctica para aislar las dependencias del proyecto. Se hace con el comando `python -m venv venv`.
Se activa el entorno virtual: En Windows, se usa el comando `.\venv\Scripts\activate`.


***
## Ejecución del Proyecto
***

```bash
python main.py
```

## Objetivo:
El objetivo de este ejercicio es crear una función en python que tome como entrada una lista de edades de 30 alumnos del curso de segundo año de la tecnicatura superior en desarrollo de software multiplataforma y generar un análisis estadístico básico, calculando la frecuencia absoluta (fi), la frecuencia acumulada (Fi), la frecuencia relativa (ri), la frecuencia relativa acumulada (Ri), la probabilidad (pi) y la probabilidad acumulada (Pi).

## Instrucciones:
Define una función llamada “analisis_estadistico” que acepte como parámetro una lista de valores numéricos.

Implementa el cálculo de las siguientes columnas:
● fi: Frecuencia absoluta de cada valor en la lista.
● Fi: Frecuencia acumulada, es decir, la suma acumulada de las frecuencias absolutas.
● ri: Frecuencia relativa, que se calcula dividiendo la frecuencia absoluta de cada valor entre el tamaño total de la muestra.
● Ri: Frecuencia relativa acumulada, la suma acumulada de las frecuencias relativas.
● pi: Probabilidad, que se obtiene dividiendo la frecuencia absoluta de cada valor entre el tamaño total de la muestra.
● Pi: Probabilidad acumulada, la suma acumulada de las probabilidades.

Se debe devolver un Dataframe que contenga estas columnas como claves y las listas correspondientes como valores asociados.

## Criterios de evaluación:
Función analisis_estadistico: La función debe tener el nombre exacto “analisis_estadistico” y aceptar una lista de valores numéricos como parámetro.

Dato de retorno: Se debe devolver el Dataframe con el contenido solicitado.

Manejo de casos especiales: La función debe manejar adecuadamente casos donde la lista de valores esté vacía, no contenga elementos no numéricos o no sea una lista en concreto.

Comentarios: Se deben incluir comentarios en el código para explicar qué hace cada parte de 

Uso correcto de la librería: Se debe usar la librería de Pandas para realizar los cálculos.

## Presentación del Trabajo Práctico:

La presentación del trabajo práctico debe realizarse en un repositorio de GitHub, el cual debe ser público para su posterior revisión y evaluación.