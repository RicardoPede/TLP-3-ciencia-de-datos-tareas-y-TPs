import pandas

lista_alumnos = [
    {"nombre": "Juan", "edad": 18},
    {"nombre": "Pedro", "edad": 19},
    {"nombre": "Maria", "edad": 21},
    {"nombre": "Jose", "edad": 21},
    {"nombre": "Luis", "edad": 22},
    {"nombre": "Ana", "edad": 23},
    {"nombre": "Carlos", "edad": 24},
    {"nombre": "Sofia", "edad": 25},
    {"nombre": "Lucia", "edad": 26},
    {"nombre": "Miguel", "edad": 27},
    {"nombre": "Santiago", "edad": 28},
    {"nombre": "Dolores", "edad": 29},
    {"nombre": "Carmen", "edad": 30},
    {"nombre": "Ricardo", "edad": 31},
    {"nombre": "Fernando", "edad": 32},
    {"nombre": "Joaquin", "edad": 33},
    {"nombre": "Natalia", "edad": 34},
    {"nombre": "Elena", "edad": 34},
    {"nombre": "Sara", "edad": 19},
    {"nombre": "Julieta", "edad": 19},
    {"nombre": "Lorena", "edad": 31},
    {"nombre": "Luisa", "edad": 30},
    {"nombre": "Marta", "edad": 28},
    {"nombre": "Mariana", "edad": 21},
    {"nombre": "Gabriela", "edad": 26},
    {"nombre": "Liliana", "edad": 22},
    {"nombre": "Rocio", "edad": 23},
    {"nombre": "Sonia", "edad": 23},
    {"nombre": "Valeria", "edad": 22},
    {"nombre": "Carolina", "edad": 21},
]

def analisis_estadistico(lista_alumnos):

    if not isinstance(lista_alumnos, list):                                 # se valida que el argumento sea una lista
        raise ValueError("El argumento debe ser una lista")                 # si no lo es, se lanza un error
    if not all(isinstance(alumno["edad"], int) for alumno in lista_alumnos): # se valida que todos los elementos de la lista sean enteros
        raise ValueError("La lista debe contener solo valores enteros")     # si no lo son, se lanza un error
    if not all(alumno["edad"] > 0 for alumno in lista_alumnos):             # se valida que todos los elementos de la lista sean positivos
        raise ValueError("La lista debe contener solo valores enteros positivos") # si no lo son, se lanza un error
    
    lista = [alumno["edad"] for alumno in lista_alumnos]        # se crea una lista con las edades mediante una comprension de listas que recorre la lista de alumnos
    lista.sort()                                                # se ordena la lista 

    df_all = pandas.DataFrame(lista, columns=['x'])             # se crea un DataFrame con las edades
    print(df_all)
    df_all['fi'] = df_all.groupby('x')['x'].transform('count')  # se crea una columna "fi" que contiene la frecuencia absoluta de cada valor

    data_frame = df_all.drop_duplicates().reset_index(drop=True) # se crea un nuevo DataFrame con los valores únicos y las frecuencias correspondientes

    # se crean las columnas restantes
    data_frame["Fi"] = data_frame["fi"].cumsum() # se crea una columna "Fi" que contiene la suma acumulada de las frecuencias absolutas
    data_frame["ri"] = (data_frame["fi"] / data_frame["fi"].sum()).round(3) # se crea una columna "ri" que contiene la frecuencia relativa, que se calcula dividiendo la frecuencia absoluta de cada valor entre el tamaño total de la muestra
    data_frame["Ri"] = (data_frame["ri"].cumsum()).round(3) # se crea una columna "Ri" que contiene la suma acumulada de las frecuencias relativas
    data_frame["pi%"] = (data_frame["ri"] * 100).round() # se crea una columna "pi%" que contiene la probabilidad, que se obtiene de la frecuencia relativa
    data_frame["Pi%"] = (data_frame["Ri"] * 100).round() # se crea una columna "Pi%" que contiene la suma acumulada de las probabilidades

    print(data_frame)
    return data_frame

analisis_estadistico(lista_alumnos)