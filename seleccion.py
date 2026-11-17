def ordenar_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

tiempos = [12.5, 10.2, 11.8, 9.9, 14.1]
print("Tiempos originales:", tiempos)
tiempos_ordenados = ordenar_seleccion(tiempos.copy())
print("Tiempos ordenados (Selección):", tiempos_ordenados)