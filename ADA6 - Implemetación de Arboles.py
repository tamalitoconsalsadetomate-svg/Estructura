class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, actual, valor):
        if valor < actual.valor:
            if actual.izquierdo is None:
                actual.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(actual.izquierdo, valor)
        elif valor > actual.valor:
            if actual.derecho is None:
                actual.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(actual.derecho, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, actual, valor):
        if actual is None or actual.valor == valor:
            return actual
        if valor < actual.valor:
            return self._buscar_recursivo(actual.izquierdo, valor)
        return self._buscar_recursivo(actual.derecho, valor)

    
    def inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo, resultado):
        if nodo:
            self._inorden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecho, resultado)

    def preorden(self):
        resultado = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado

    def _preorden_recursivo(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self._preorden_recursivo(nodo.izquierdo, resultado)
            self._preorden_recursivo(nodo.derecho, resultado)

    def postorden(self):
        resultado = []
        self._postorden_recursivo(self.raiz, resultado)
        return resultado

    def _postorden_recursivo(self, nodo, resultado):
        if nodo:
            self._postorden_recursivo(nodo.izquierdo, resultado)
            self._postorden_recursivo(nodo.derecho, resultado)
            resultado.append(nodo.valor)


arbol = ArbolBinarioBusqueda()
    
valores = [50, 30, 70, 20, 40, 60, 80]
for v in valores:
    arbol.insertar(v)
        
print("--- DEMOSTRACIÓN DE ÁRBOL BINARIO ---")
print(f"Valores insertados: {valores}")
print("Recorriendo el árbol...")
print("Inorden  :", arbol.inorden())
print("Preorden :", arbol.preorden())
print("Postorden:", arbol.postorden())
    
buscado = 40
encontrado = arbol.buscar(buscado)
print(f"¿El valor {buscado} está en el árbol?: {'Sí' if encontrado else 'No'}")