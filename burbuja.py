def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

calificaciones = [85, 42, 91, 28, 67, 75]
print("Calificaciones originales:", calificaciones)
calificaciones_ordenadas = ordenar_burbuja(calificaciones.copy())
print("Calificaciones ordenadas (Burbuja):", calificaciones_ordenadas)