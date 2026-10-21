from collections import deque

class Cola:
    def __init__(self):
        self.elementos = deque()

    def esta_vacia(self):
        return len(self.elementos) == 0

    def encolar(self, item):
        self.elementos.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.popleft()
        return None

    def tamaño(self):
        return len(self.elementos)

    def __str__(self):
        return str(list(self.elementos))

def sumar_colas(cola1: Cola, cola2: Cola) -> Cola:
    cola_resultado = Cola()
    c1_temp = deque(cola1.elementos)
    c2_temp = deque(cola2.elementos)
    
    while c1_temp and c2_temp:
        val1 = c1_temp.popleft()
        val2 = c2_temp.popleft()
        cola_resultado.encolar(val1 + val2)
        
    return cola_resultado

class SistemaSeguros:
    def __init__(self):
        self.colas_servicios = {}
        self.turnos_otorgados = {}

    def simular_llegada(self, num_servicio: int):
        """Un cliente llega (C + número de servicio) y se le asigna un turno."""
        if num_servicio not in self.colas_servicios:
            self.colas_servicios[num_servicio] = Cola()
            self.turnos_otorgados[num_servicio] = 0
        
        self.turnos_otorgados[num_servicio] += 1
        ticket = self.turnos_otorgados[num_servicio]
        
        self.colas_servicios[num_servicio].encolar(ticket)
        print(f"[LLEGADA] Cliente asignado al Servicio {num_servicio}. Su número de atención es: C{num_servicio}-{ticket}")

    def atender_cliente(self, num_servicio: int):
        """El personal de atención llama al siguiente cliente (A + número de servicio)."""
        if num_servicio not in self.colas_servicios or self.colas_servicios[num_servicio].esta_vacia():
            print(f"[ATENCIÓN] No hay clientes en espera para el Servicio {num_servicio}.")
        else:
            ticket = self.colas_servicios[num_servicio].desencolar()
            print(f"[LLAMANDO] ¡Turno C{num_servicio}-{ticket} al módulo de atención del Servicio {num_servicio}!")


if __name__ == "__main__":
    print("=== PRUEBA PROBLEMA 1: Suma de Colas ===")
    cola_a = Cola()
    for n in [3, 4, 2, 8, 12]:
        cola_a.encolar(n)
        
    cola_b = Cola()
    for n in [6, 2, 9, 11, 3]:
        cola_b.encolar(n)
        
    cola_res = sumar_colas(cola_a, cola_b)
    print(f"Cola A:        {cola_a}")
    print(f"Cola B:        {cola_b}")
    print(f"Cola Resultado: {cola_res}\n")

    print("=== PRUEBA PROBLEMA 2: Sistema de Seguros ===")
    sistema = SistemaSeguros()
    
    sistema.simular_llegada(1)
    sistema.simular_llegada(1)
    sistema.simular_llegada(2)
    
    print()
    sistema.atender_cliente(1)
    sistema.atender_cliente(1)
    sistema.atender_cliente(1) 

    print("\n--- Modo Interactivo Consola (Opcional) ---")
    print("Comandos disponibles:")
    print("  C <num> -> Simula llegada de cliente (ej: C 1)")
    print("  A <num> -> Atiende a un cliente (ej: A 1)")
    print("  SALIR   -> Terminar programa")
    
    while True:
        try:
            entrada = input("\nIngrese comando: ").strip()
            if entrada.upper() == "SALIR":
                break
            
            partes = entrada.split()
            if len(partes) == 2:
                comando = partes[0].upper()
                servicio = int(partes[1])
                
                if comando == 'C':
                    sistema.simular_llegada(servicio)
                elif comando == 'A':
                    sistema.atender_cliente(servicio)
                else:
                    print("Comando no reconocido. Use 'C' para llegada o 'A' para atención.")
            else:
                print("Formato incorrecto. Ejemplo: C 1 o A 2")
        except ValueError:
            print("Por favor, ingrese un número de servicio válido.")