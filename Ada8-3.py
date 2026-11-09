def warshall(matriz_booleana):
    n = len(matriz_booleana)
    alcanzabilidad = [row[:] for row in matriz_booleana]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                alcanzabilidad[i][j] = alcanzabilidad[i][j] or (alcanzabilidad[i][k] and alcanzabilidad[k][j])
                
    return alcanzabilidad

# Ejemplo de uso
if __name__ == "__main__":
    # 1 representa conexión existente, 0 representa no conexión
    matriz_booleana = [
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1]
    ]
    
    resultado = warshall(matriz_booleana)
    print("Matriz de Clausura Transitiva (Alcanzabilidad):")
    for fila in resultado:
        print([1 if val else 0 for val in fila])