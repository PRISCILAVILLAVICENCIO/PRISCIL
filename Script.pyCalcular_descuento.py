def calcular_descuento(monto_total, porcentaje_descuento=10):
  """
  Calcula el monto del descuento basado en el monto total y un porcentaje.

  Args:
    monto_total (float): El costo total de la compra.
    porcentaje_descuento (float): El porcentaje de descuento a aplicar. Por defecto es 10.

  Returns:
    float: El monto del descuento calculado.
  """
  descuento = monto_total * (porcentaje_descuento / 100)
  return descuento

# Llamadas a la función con valores fijos
print("--- Cálculo de Descuentos ---")

# Primera llamada: solo se pasa el monto total se aplica el 10%
monto_compra_1 = 150.00
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - descuento_1
print(f"Primera compra:")
print(f"  Monto total: ${monto_compra_1:.2f}")
print(f"  Descuento (10%): ${descuento_1:.2f}")
print(f"  Monto a pagar: ${monto_final_1:.2f}\n")

# Segunda llamada: se pasa el monto total y un porcentaje de descuento personalizado
monto_compra_2 = 250.75
descuento_personalizado = 15
descuento_2 = calcular_descuento(monto_compra_2, descuento_personalizado)
monto_final_2 = monto_compra_2 - descuento_2
print(f"Segunda compra:")
print(f"  Monto total: ${monto_compra_2:.2f}")
print(f"  Descuento ({descuento_personalizado}%): ${descuento_2:.2f}")
print(f"  Monto a pagar: ${monto_final_2:.2f}")