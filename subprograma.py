class NodoIngrediente:
    def __init__(self, ingrediente):
        self.info = ingrediente  
        self.liga = None         


class Postre:
    def __init__(self, nombre):
        self.nombre = nombre                 
        self.cabeza_ingredientes = None       


class SistemaPostres:
    def __init__(self):
        self.POSTRES = []

    def buscar_postre(self, nombre):
        """Busca un postre en el arreglo por su nombre."""
        for i, postre in enumerate(self.POSTRES):
            if postre.nombre.lower() == nombre.lower():
                return i
        return -1

    def imprimir_ingredientes(self, nombre):
        idx = self.buscar_postre(nombre)
        if idx == -1:
            print(f"Error: El postre '{nombre}' no se encuentra registrado.")
            return
        
        postre = self.POSTRES[idx]
        print(f"\nIngredientes del postre '{postre.nombre}':")
        actual = postre.cabeza_ingredientes
        
        if actual is None:
            print("  (La lista de ingredientes está vacía)")
            return
        
        while actual is not None:
            print(f"  - {actual.info}")
            actual = actual.liga

    def insertar_ingrediente(self, nombre, nuevo_ingrediente):
        idx = self.buscar_postre(nombre)
        if idx == -1:
            print(f"Error: No se puede insertar. El postre '{nombre}' no existe.")
            return
        
        postre = self.POSTRES[idx]
        nuevo_nodo = NodoIngrediente(nuevo_ingrediente)
        nuevo_nodo.liga = postre.cabeza_ingredientes
        postre.cabeza_ingredientes = nuevo_nodo
        print(f"Éxito: Ingrediente '{nuevo_ingrediente}' agregado al postre '{postre.nombre}'.")

    def eliminar_ingrediente(self, nombre, ingrediente_a_borrar):
        idx = self.buscar_postre(nombre)
        if idx == -1:
            print(f"Error: El postre '{nombre}' no existe.")
            return
        
        postre = self.POSTRES[idx]
        actual = postre.cabeza_ingredientes
        
        if actual is None:
            print(f"El postre '{postre.nombre}' no tiene ingredientes para eliminar.")
            return
        
        if actual.info.lower() == ingrediente_a_borrar.lower():
            postre.cabeza_ingredientes = actual.liga
            print(f"Éxito: Ingrediente '{ingrediente_a_borrar}' eliminado de '{postre.nombre}'.")
            return
        
        while actual.liga is not None and actual.liga.info.lower() != ingrediente_a_borrar.lower():
            actual = actual.liga
            
        if actual.liga is not None:
            actual.liga = actual.liga.liga
            print(f"Éxito: Ingrediente '{ingrediente_a_borrar}' eliminado de '{postre.nombre}'.")
        else:
            print(f"Aviso: El ingrediente '{ingrediente_a_borrar}' no se encontró en la lista.")

    def dar_alta_postre(self, nombre, lista_ingredientes):
        idx = self.buscar_postre(nombre)
        if idx != -1:
            print(f"Error: El postre '{nombre}' ya se encuentra registrado.")
            return
        
        nuevo_postre = Postre(nombre)
        for ing in reversed(lista_ingredientes):
            nodo = NodoIngrediente(ing)
            nodo.liga = nuevo_postre.cabeza_ingredientes
            nuevo_postre.cabeza_ingredientes = nodo
            
        self.POSTRES.append(nuevo_postre)
        self.POSTRES.sort(key=lambda x: x.nombre.lower())
        print(f"Éxito: Postre '{nombre}' dado de alta correctamente.")

    def dar_baja_postre(self, nombre):
        idx = self.buscar_postre(nombre)
        if idx == -1:
            print(f"Error: El postre '{nombre}' no existe en el sistema.")
            return
        
        postre_eliminado = self.POSTRES.pop(idx)
        print(f"Éxito: Postre '{postre_eliminado.nombre}' y su lista de ingredientes dados de baja.")

    def eliminar_duplicados_postres(self):
        print("\n--- Ejecutando subprograma: Eliminación de postres duplicados ---")
        vistos = set()
        postres_unicos = []
        duplicados_removidos = 0

        for postre in self.POSTRES:
            nombre_lower = postre.nombre.lower()
            if nombre_lower not in vistos:
                vistos.add(nombre_lower)
                postres_unicos.append(postre)
            else:
                duplicados_removidos += 1

        self.POSTRES = postres_unicos
        print(f"Se eliminaron {duplicados_removidos} postres duplicados del arreglo.")