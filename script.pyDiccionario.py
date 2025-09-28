# 1. Crear un Diccionario:
# Crear un diccionario llamado 'informacion_personal' con la información inicial mia
informacion_personal = {
    "Nombre": "Priscila Villavicencio",
    "Edad": 28,
    "Ciudad": "Quito",
    "Profesion": "Contadora"
}
print(f"Diccionario Inicial: {informacion_personal}")



# 2. Acceder y Modificar Valores:

# Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
# Se cambiará la ciudad de "Quito" a "Guayaquil" (un cambio ficticio ).
ciudad_actual = informacion_personal["Ciudad"]
informacion_personal["Ciudad"] = "Guayaquil"
print(f"\n2a. Ciudad Modificada de '{ciudad_actual}' a '{informacion_personal['Ciudad']}'.")


#  AGREGAR una nueva clave-valor para un atributo no listado inicialmente, como "empresa".
informacion_personal["Empresa"] = "SODIG Ecuador"
print(f"2b. Nueva clave 'Empresa' agregada: {informacion_personal['Empresa']}.")

# ---

# 3. Verificar Existencia de Claves:

# Verifica si la clave "telefono" existe en el diccionario.
if "telefono" not in informacion_personal:
    # Si no existe, agrégala con un número de teléfono ficticio.
    informacion_personal["Telefono"] = "0991234567"
    print(f"\n3. Clave 'Telefono' no existía y fue agregada: {informacion_personal['Telefono']}.")
else:
    print("\n3. La clave 'Telefono' ya existía.")



# 4. Eliminar una Clave:

# Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
del informacion_personal["Edad"]
print("\n4. Clave 'edad' eliminada.")


# 5. Imprimir el Diccionario Final:

# Imprime el diccionario resultante después de realizar todas las operaciones.
print("\n---")
print("5. Diccionario Final:")
print(informacion_personal)