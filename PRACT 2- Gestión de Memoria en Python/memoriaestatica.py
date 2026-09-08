def memoria_estatica():
    calificaciones = [0] * 5
    for i in range(5):
        calificacion = int(input(f"Ingresa la calificación {i + 1}: "))
        calificaciones[i] = calificacion
    print("\nCalificaciones:")
    print(calificaciones)

memoria_estatica()