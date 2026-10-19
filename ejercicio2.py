class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

class NavegadorWeb:
    def __init__(self):
        self.historial_atras = Pila()    
        self.historial_adelante = Pila() 
        self.pagina_actual = None

    def visitar_pagina(self, url):
        if self.pagina_actual:
            self.historial_atras.apilar(self.pagina_actual)
        self.pagina_actual = url
        self.historial_adelante = Pila()
        print(f"-> Navegando a: {url}")

    def ir_atras(self):
        if self.historial_atras.esta_vacia():
            print("<- No hay paginas anteriores en el historial.")
            return
        self.historial_adelante.apilar(self.pagina_actual)
        self.pagina_actual = self.historial_atras.desapilar()
        print(f"<- Retrocediendo a: {self.pagina_actual}")

    def ir_adelante(self):
        if self.historial_adelante.esta_vacia():
            print("-> No hay páginas adelante en el historial.")
            return
        self.historial_atras.apilar(self.pagina_actual)
        self.pagina_actual = self.historial_adelante.desapilar()
        print(f"-> Avanzando a: {self.pagina_actual}")

    def mostrar_estado(self):
        print(f"   [Pagina Actual]: {self.pagina_actual}\n")


navegador = NavegadorWeb()
    
navegador.visitar_pagina("google.com")
navegador.mostrar_estado()
    
navegador.visitar_pagina("github.com")
navegador.mostrar_estado()
    
navegador.visitar_pagina("python.org")
navegador.mostrar_estado()
    
print("--- ACCION: Boton Atras ---")
navegador.ir_atras()
navegador.mostrar_estado()
    
print("--- ACCION: Boton Atras ---")
navegador.ir_atras()
navegador.mostrar_estado()
    
print("--- ACCION: Boton Adelante ---")
navegador.ir_adelante()
navegador.mostrar_estado()