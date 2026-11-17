def ordenar_insercion(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

precios = [450.50, 120.0, 89.99, 300.0, 15.5]
print("Precios originales:", precios)
precios_ordenados = ordenar_insercion(precios.copy())
print("Precios ordenados (Inserción):", precios_ordenados)