# Tarea: Trabajo con Archivos de Texto en Python
# Solución 1

# 1. Escritura de Archivo de Texto

# El bloque 'with open' abre el archivo y se asegura de que se cierre automáticamente.
# 'w' significa que abriremos el archivo en modo de escritura (write).
# Si el archivo no existe, lo creará. Si existe, lo sobrescribirá.
print("Creando y escribiendo en el archivo my_notes.txt.")
with open('my_notes.txt', 'w', encoding='utf-8') as file:
    # Escribimos tres líneas de notas personales en el archivo.
    # El carácter '\n' es un salto de línea para que cada nota esté en su propia línea.
    file.write("Recordatorio 1: Preparar la presentación para el lunes.\n")
    file.write("Recordatorio 2: Comprar víveres después de clase.\n")
    file.write("Recordatorio 3: Llamar a la abuela el fin de semana.\n")
print("El archivo ha sido escrito exitosamente.")
print("-" * 20) # Separador para mayor claridad

# 2. Lectura de Archivo de Texto

# 'r' significa que abriremos el archivo en modo de lectura (read).
print("Abriendo y leyendo el archivo my_notes.txt línea por línea:")
try:
    with open('my_notes.txt', 'r', encoding='utf-8') as file:
        # Leemos la primera línea del archivo.
        linea = file.readline()

        # Usamos un bucle 'while' para leer el archivo línea por línea.
        # El bucle continuará mientras el métodoo readline() no devuelva una cadena vacía (el final del archivo).
        while linea:
            # Mostramos la línea leída en la consola.

            print(f"Línea leída: {linea.strip()}")
            # Leemos la siguiente línea para la próxima iteración del bucle.
            linea = file.readline()

except FileNotFoundError:
    print("Error: El archivo my_notes.txt no fue encontrado.")

#3. Cierre de Archivos

print("-" * 20)
print("Operación completada. El archivo fue cerrado automáticamente.")