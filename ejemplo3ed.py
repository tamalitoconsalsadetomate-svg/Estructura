import random
import statistics

# 1. Generar lista de 50 números aleatorios entre 1 y 100
numeros = [random.randint(150, 250) for _ in range(50)]

# 2. Cálculos estadísticos
media = statistics.mean(numeros)
mediana = statistics.median(numeros)

# multimode se usa por si existe más de un número con la frecuencia máxima
moda = statistics.multimode(numeros)

varianza_muestral = statistics.variance(numeros)
desviacion_muestral = statistics.stdev(numeros)

varianza_poblacional = statistics.pvariance(numeros)
desviacion_poblacional = statistics.pstdev(numeros)

# 3. Mostrar resultados
print(f"Lista de números:\n{numeros}\n")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Varianza (muestral): {varianza_muestral:.2f}")
print(f"Desviación estándar (muestral): {desviacion_muestral:.2f}")
print(f"Varianza (poblacional): {varianza_poblacional:.2f}")
print(f"Desviación estándar (poblacional): {desviacion_poblacional:.2f}")