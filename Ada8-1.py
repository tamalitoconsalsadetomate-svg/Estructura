import heapq

def dijkstra(grafo, origen):
    # Distancias iniciales a infinito
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[origen] = 0
    
    # Cola de prioridad: (distancia, nodo)
    cola_prioridad = [(0, origen)]
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        # Si la distancia en la cola es mayor a la registrada, omitir
        if distancia_actual > distancias[nodo_actual]:
            continue
            
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            
            # Si se encuentra un camino más corto hacia el vecino
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))
                
    return distancias

# Ejemplo de uso
if __name__ == "__main__":
    grafo_ejemplo = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'Z': 6},
        'E': {'C': 10, 'D': 2, 'Z': 3},
        'Z': {'D': 6, 'E': 3}
    }
    
    origen = 'A'
    resultado = dijkstra(grafo_ejemplo, origen)
    print(f"Distancias más cortas desde el nodo '{origen}':")
    for nodo, dist in resultado.items():
        print(f"  Nodo {nodo}: {dist}")