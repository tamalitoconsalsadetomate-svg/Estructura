def floyd_warshall(matriz_adyacencia):
    n = len(matriz_adyacencia)
    # Copia de la matriz para no modificar la original
    dist = [row[:] for row in matriz_adyacencia]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    return dist

INF = float('inf')

# Ejemplo de uso
if __name__ == "__main__":
    # Matriz representación de grafo (4 nodos: 0, 1, 2, 3)
    matriz_grafo = [
        [0,   5,   INF, 10],
        [INF, 0,   3,   INF],
        [INF, INF, 0,   1],
        [INF, INF, INF, 0]
    ]
    
    resultado = floyd_warshall(matriz_grafo)
    print("Matriz de distancias más cortas entre todos los pares:")
    for fila in resultado:
        print([val if val != INF else "INF" for val in fila])