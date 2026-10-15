def torre_hanoi_pasos(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 desde la varilla {origen} -> varilla {destino}")
        return
    
    torre_hanoi_pasos(n - 1, origen, auxiliar, destino)
    
    print(f"Mover disco {n} desde la varilla {origen} -> varilla {destino}")
    
    torre_hanoi_pasos(n - 1, auxiliar, destino, origen)

print("--- INICIO DE LOS MOVIMIENTOS ---")
torre_hanoi_pasos(30, 'A', 'C', 'B')
print("--- ¡TORRES DE HANÓI RESUELTAS! ---")