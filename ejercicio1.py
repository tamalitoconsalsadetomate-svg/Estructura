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

def evaluar_posfija(expresion):
    pila = Pila()
    tokens = expresion.split()

    for token in tokens:
        if token.replace('.', '', 1).isdigit():
            pila.apilar(float(token))
        elif token in "+-*/":
            if len(pila.items) < 2:
                return "Error: Expresión mal formada."
            b = pila.desapilar()
            a = pila.desapilar()
            
            if token == '+': resultado = a + b
            elif token == '-': resultado = a - b
            elif token == '*': resultado = a * b
            elif token == '/':
                if b == 0:
                    return "Error: División por cero."
                resultado = a / b
            
            pila.apilar(resultado)
        else:
            return f"Error: Token desconocido '{token}'"
            
    return pila.desapilar()

expresion = "5 1 2 + 4 * + 3 -" 
print(f"Expresión posfija: {expresion}")
resultado = evaluar_posfija(expresion)
print(f"Resultado de la evaluacion: {resultado}")