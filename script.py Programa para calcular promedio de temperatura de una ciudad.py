# Datos de la matriz de temperaturas
temperaturas = [
    [  # Ciudad 1: Baños
        [  # Semana 1
            {"dia": "Lunes", "temperatura": 25},
            {"dia": "Martes", "temperatura": 26},
            {"dia": "Miercoles", "temperatura": 25},
            {"dia": "Jueves", "temperatura": 27},
            {"dia": "Viernes", "temperatura": 28},
            {"dia": "Sabado", "temperatura": 28},
            {"dia": "Domingo", "temperatura": 26}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temperatura": 24},
            {"dia": "Martes", "temperatura": 25},
            {"dia": "Miercoles", "temperatura": 26},
            {"dia": "Jueves", "temperatura": 27},
            {"dia": "Viernes", "temperatura": 26},
            {"dia": "Sabado", "temperatura": 25},
            {"dia": "Domingo", "temperatura": 27}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temperatura": 26},
            {"dia": "Martes", "temperatura": 27},
            {"dia": "Miercoles", "temperatura": 28},
            {"dia": "Jueves", "temperatura": 26},
            {"dia": "Viernes", "temperatura": 25},
            {"dia": "Sabado", "temperatura": 24},
            {"dia": "Domingo", "temperatura": 25}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temperatura": 27},
            {"dia": "Martes", "temperatura": 28},
            {"dia": "Miercoles", "temperatura": 26},
            {"dia": "Jueves", "temperatura": 25},
            {"dia": "Viernes", "temperatura": 24},
            {"dia": "Sabado", "temperatura": 25},
            {"dia": "Domingo", "temperatura": 26}
        ]
    ],

]
ciudades = ["Baños"]


def calcular_promedio_temperatura(datos_temperatura, nombre_ciudades):
    """
    Calcula y muestra el promedio de temperatura para cada ciudad por semana.

    Args:
        datos_temperatura (list): Una lista anidada con los datos de temperatura.
        nombre_ciudades (list): Una lista con los nombres de las ciudades.
    """
    print("Promedio de temperaturas por ciudad y semana:\n")

    for ciudad_idx, ciudad_datos in enumerate(datos_temperatura):
        print(f"--- Promedios para {nombre_ciudades[ciudad_idx]} ---")
        for semana_idx, semana_datos in enumerate(ciudad_datos):
            # Extraer solo los valores de temperatura de la lista de diccionarios
            temperaturas_semana = [dia["temperatura"] for dia in semana_datos]

            # Calcular el promedio de la semana
            promedio_semana = sum(temperaturas_semana) / len(temperaturas_semana)

            # Mostrar el resultado
            print(f"  > El promedio de la semana {semana_idx + 1} es: {promedio_semana:.2f}°C")
        print("\n")


# Llamada a la función para ejecutar el cálculo
calcular_promedio_temperatura(temperaturas, ciudades)