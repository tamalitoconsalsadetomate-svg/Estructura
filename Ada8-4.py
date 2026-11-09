class DisjointSet:
    def __init__(self, n):
        self.padre = list(range(n))
        
    def find(self, i):
        if self.padre[i] == i:
            return i
        self.padre[i] = self.find(self.padre[i]) # Compresión de caminos
        return self.padre[i]

    def union(self, i, j):
        raiz_i = self.find(i)
        raiz_j = self.find(j)
        if raiz_i != raiz_j:
            self.padre[raiz_i] = raiz_j
            return True
        return False

def kruskal(num_nodos, aristas):
    # Ordenar aristas por su peso (peso, u, v)
    aristas.sort(key=lambda x: x[2])
    
    dsu = DisjointSet(num_nodos)
    mst = []
    costo_total = 0
    
    for u, v, peso in aristas:
        if dsu.union(u, v):
            mst.append((u, v, peso))
            costo_total += peso
            
    return mst, costo_total

# Ejemplo de uso
if __name__ == "__main__":
    num_nodos = 4
    # Formato de aristas: (nodo1, nodo2, peso)
    aristas = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    
    aristas_mst, costo = kruskal(num_nodos, aristas)
    print("Aristas incluidas en el Árbol de Expansión Mínima (MST):")
    for u, v, peso in aristas_mst:
        print(f"  Arista ({u} - {v}) con peso: {peso}")
    print(f"Costo Total del MST: {costo}")