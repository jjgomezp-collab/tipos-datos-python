"""
Programa para calcular el área de un rectángulo.
Solicita al usuario el ancho y el alto,
calcula el área y muestra el resultado.
"""

# Entrada de datos
ancho = float(input("Ingrese el ancho del rectángulo: "))
alto = float(input("Ingrese el alto del rectángulo: "))

# Proceso
area_rectangulo = ancho * alto
es_area_grande = area_rectangulo > 20

# Salida de resultados
print("\nResultados:")
print(f"Ancho: {ancho}")
print(f"Alto: {alto}")
print(f"Área: {area_rectangulo}")

if es_area_grande:
    print("El área es grande.")
else:
    print("El área es pequeña.")
