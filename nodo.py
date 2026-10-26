class Nodo:
    def __init__(self, info):
        self.info = info  # Campo INFO del nodo
        self.liga = None  # Campo LIGA del nodo (inicialmente NIL / None)


# --- Inserta_inicio ---
def inserta_inicio(p, dato):
    """Inserta un nodo al inicio de una lista simplemente ligada."""
    q = Nodo(dato)
    q.liga = p
    p = q
    return p


# --- Crea_inicio ---
def crea_inicio():
    print("--- Creación de la Lista (Crea_inicio) ---")
    p = None
    
    info_inicial = input("Ingrese el valor del primer nodo (P^.INFO): ")
    p = Nodo(info_inicial)
    p.liga = None
    
    res = int(input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0: "))
    
    while res == 1:
        dato = input("Ingrese el valor del nuevo nodo (DATO): ")
        p = inserta_inicio(p, dato)
        res = int(input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0: "))
        
    return p


# --- Búsqueda_recursivo ---
def busqueda_recursivo(p, x):
    """Busca recursivamente un elemento con información X en la lista."""
    if p is not None:
        if p.info == x:
            print("El elemento se encuentra en la lista")
            return True
        else:
            return busqueda_recursivo(p.liga, x)
    else:
        print("El elemento no se encuentra en la lista")
        return False


# --- Función para Eliminar un Elemento ---
def eliminar_elemento(p, x):
    """Elimina la primera aparición de un elemento con información X en la lista."""
    if p is None:
        print("La lista está vacía.")
        return p
    
    # Si el elemento a eliminar está en el primer nodo
    if p.info == x:
        print(f"Elemento '{x}' eliminado del inicio.")
        return p.liga  # El nuevo inicio es el siguiente nodo
    
    actual = p
    while actual.liga is not None and actual.liga.info != x:
        actual = actual.liga
        
    # Si se encontró el elemento en el siguiente nodo
    if actual.liga is not None:
        actual.liga = actual.liga.liga  # Salta el nodo a eliminar
        print(f"Elemento '{x}' eliminado correctamente.")
    else:
        print(f"El elemento '{x}' no se encuentra en la lista para eliminar.")
        
    return p


# --- Función auxiliar para recorrer y visualizar la lista ---
def recorrer_lista(p, mensaje="\nContenido actual de la lista (del inicio al final):"):
    actual = p
    print(mensaje)
    if actual is None:
        print("NIL (Lista vacía)")
        return
    while actual is not None:
        print(f"[{actual.info}] -> ", end="")
        actual = actual.liga
    print("NIL")


# --- Bloque Principal de Ejecución ---
if __name__ == "__main__":
    # 1. Creamos la lista
    mi_lista = crea_inicio()
    recorrer_lista(mi_lista)
    
    # 2. Probar Búsqueda
    print("\n--- Búsqueda en la Lista ---")
    x_buscar = input("Ingrese el elemento a buscar: ")
    busqueda_recursivo(mi_lista, x_buscar)
    
    # 3. Probar Inserción de un nuevo elemento al inicio
    print("\n--- Inserción de un nuevo elemento ---")
    x_insertar = input("Ingrese el valor a insertar al inicio: ")
    mi_lista = inserta_inicio(mi_lista, x_insertar)
    recorrer_lista(mi_lista)
    
    # 4. Probar Eliminación de un elemento
    print("\n--- Eliminación de un elemento ---")
    x_eliminar = input("Ingrese el valor del elemento que desea eliminar: ")
    mi_lista = eliminar_elemento(mi_lista, x_eliminar)
    recorrer_lista(mi_lista)
    
    # 5. Demostración de dos nodos distintos apuntando a un mismo nodo
    print("\n--- Demostración: Dos nodos diferentes apuntando a un mismo nodo ---")
    
    # Creamos un nodo común al que apuntarán ambos
    nodo_comun = Nodo("Común")
    nodo_comun.liga = None
    
    # Creamos dos nodos o ramas independientes
    nodo_a = Nodo("Rama_A")
    nodo_b = Nodo("Rama_B")
    
    # Hacemos que la liga de ambos apunte exactamente al mismo nodo común
    nodo_a.liga = nodo_comun
    nodo_b.liga = nodo_comun
    
    recorrer_lista(nodo_a, "\nRecorriendo desde Rama A:")
    recorrer_lista(nodo_b, "Recorriendo desde Rama B:")
    
    if nodo_a.liga is nodo_b.liga:
        print("\n¡Comprobado! Las ligas de 'Rama_A' y 'Rama_B' apuntan al mismo objeto en memoria.")