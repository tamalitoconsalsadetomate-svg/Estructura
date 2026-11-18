import time
import random


def shell_sort(arr, mostrar_pasos=False):
    """Ordenamiento ShellSort (por incrementos decrecientes)."""
    datos = arr.copy()
    n = len(datos)
    gap = n // 2
    comparaciones = 0
    intercambios = 0
    paso = 1

    while gap > 0:
        for i in range(gap, n):
            temp = datos[i]
            j = i
            while j >= gap:
                comparaciones += 1
                if datos[j - gap] > temp:
                    datos[j] = datos[j - gap]
                    intercambios += 1
                    j -= gap
                else:
                    break
            datos[j] = temp
        if mostrar_pasos:
            print(f"  [Paso {paso} | Gap = {gap}]: {datos}")
            paso += 1
        gap //= 2

    return datos, comparaciones, intercambios


def quick_sort(arr, mostrar_pasos=False):
    """Ordenamiento Quicksort (Divide y Vencerás con partición de Lomuto)."""
    datos = arr.copy()
    stats = {"comparaciones": 0, "intercambios": 0}

    def particion(inicio, fin):
        pivote = datos[fin]
        i = inicio - 1
        for j in range(inicio, fin):
            stats["comparaciones"] += 1
            if datos[j] <= pivote:
                i += 1
                datos[i], datos[j] = datos[j], datos[i]
                stats["intercambios"] += 1
        datos[i + 1], datos[fin] = datos[fin], datos[i + 1]
        stats["intercambios"] += 1
        if mostrar_pasos:
            print(f"  [Pivote {pivote} en pos {i + 1}]: {datos}")
        return i + 1

    def _quick_sort_rec(inicio, fin):
        if inicio < fin:
            pi = particion(inicio, fin)
            _quick_sort_rec(inicio, pi - 1)
            _quick_sort_rec(pi + 1, fin)

    if len(datos) > 1:
        _quick_sort_rec(0, len(datos) - 1)
    return datos, stats["comparaciones"], stats["intercambios"]


def heap_sort(arr, mostrar_pasos=False):
    """Ordenamiento Heapsort (Montículo binario máximo)."""
    datos = arr.copy()
    n = len(datos)
    stats = {"comparaciones": 0, "intercambios": 0}

    def heapify(tam, raiz):
        mayor = raiz
        izq = 2 * raiz + 1
        der = 2 * raiz + 2

        if izq < tam:
            stats["comparaciones"] += 1
            if datos[izq] > datos[mayor]:
                mayor = izq

        if der < tam:
            stats["comparaciones"] += 1
            if datos[der] > datos[mayor]:
                mayor = der

        if mayor != raiz:
            datos[raiz], datos[mayor] = datos[mayor], datos[raiz]
            stats["intercambios"] += 1
            heapify(tam, mayor)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    if mostrar_pasos:
        print(f"  [Max-Heap inicial]: {datos}")

    for i in range(n - 1, 0, -1):
        datos[i], datos[0] = datos[0], datos[i]
        stats["intercambios"] += 1
        heapify(i, 0)
        if mostrar_pasos:
            print(f"  [Extraído {datos[i]}]: {datos}")

    return datos, stats["comparaciones"], stats["intercambios"]


def _radix_positivos(arr, mostrar_pasos=False, etiqueta=""):
    """Subrutina auxiliar de Radix Sort por cubetas (LSD)."""
    if not arr:
        return [], 0
    datos = arr.copy()
    max_num = max(datos)
    exp = 1
    movimientos = 0

    while max_num // exp > 0:
        cubetas = [[] for _ in range(10)]
        for num in datos:
            digito = (num // exp) % 10
            cubetas[digito].append(num)
            movimientos += 1

        datos = [num for cubeta in cubetas for num in cubeta]
        if mostrar_pasos:
            print(f"  [Dígito 10^{len(str(exp)) - 1} {etiqueta}]: {datos}")
        exp *= 10

    return datos, movimientos


def radix_sort(arr, mostrar_pasos=False):
    """Ordenamiento Radix Sort con soporte para enteros positivos y negativos."""
    negativos = [-x for x in arr if x < 0]
    positivos = [x for x in arr if x >= 0]

    neg_ord, mov1 = _radix_positivos(negativos, mostrar_pasos, "(negativos)")
    pos_ord, mov2 = _radix_positivos(positivos, mostrar_pasos, "(positivos)")

    resultado = [-x for x in reversed(neg_ord)] + pos_ord
    return resultado, 0, (mov1 + mov2)


def pedir_entero(mensaje, minimo=None):
    """Solicita un entero validando errores de captura."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Error: El valor debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Error: Ingresa un número entero válido.")


def capturar_numeros():
    """Permite capturar los números manualmente o generarlos de forma aleatoria."""
    cantidad = pedir_entero("\n¿Cuántos números deseas ingresar?: ", minimo=1)
    print("¿Cómo deseas capturar los datos?")
    print("  1. Ingresarlos manualmente uno por uno")
    print("  2. Generar números aleatorios automáticamente")
    modo = input("Selecciona (1 o 2): ").strip()

    numeros = []
    if modo == "2":
        limite = pedir_entero("Valor máximo aleatorio (ej. 100): ", minimo=1)
        numeros = [random.randint(0, limite) for _ in range(cantidad)]
        print(f"Lista generada: {numeros}")
    else:
        for i in range(cantidad):
            num = pedir_entero(f"  Ingresa el número [{i + 1}/{cantidad}]: ")
            numeros.append(num)
    return numeros


def main():
    print("=" * 58)
    print("   SISTEMA INTERACTIVO DE MÉTODOS DE ORDENAMIENTO")
    print("=" * 58)

    numeros = capturar_numeros()

    algoritmos = {
        "1": ("ShellSort", shell_sort),
        "2": ("Quicksort", quick_sort),
        "3": ("Heapsort", heap_sort),
        "4": ("Radix Sort", radix_sort),
    }

    while True:
        print("\n" + "-" * 58)
        print(f"Arreglo actual ({len(numeros)} elementos): {numeros}")
        print("-" * 58)
        print("Elige el método de ordenamiento:")
        print("  1. ShellSort")
        print("  2. Quicksort")
        print("  3. Heapsort")
        print("  4. Radix Sort")
        print("  5. Ingresar un nuevo conjunto de números")
        print("  6. Comparar los 4 métodos simultáneamente (Benchmark)")
        print("  7. Salir")

        opcion = input("\nOpción: ").strip()

        if opcion == "7":
            print("\nPrograma finalizado. ¡Hasta luego!")
            break
        elif opcion == "5":
            numeros = capturar_numeros()
            continue
        elif opcion in algoritmos:
            nombre, funcion = algoritmos[opcion]
            ver_pasos = (
                len(numeros) <= 15
                and input("¿Mostrar traza paso a paso? (s/n): ").strip().lower() == "s"
            )

            inicio = time.perf_counter()
            ordenado, comp, mov = funcion(numeros, mostrar_pasos=ver_pasos)
            fin = time.perf_counter()
            tiempo_ms = (fin - inicio) * 1000

            print(f"\n>>> Resultado con {nombre}:")
            print(f"    Arreglo original  : {numeros}")
            print(f"    Arreglo ordenado  : {ordenado}")
            print(f"    Comparaciones     : {comp}")
            print(f"    Movimientos/Inter.: {mov}")
            print(f"    Tiempo ejecución  : {tiempo_ms:.6f} ms")
        elif opcion == "6":
            print("\n>>> BENCHMARK COMPARATIVO:")
            print(f"{'Método':<14} | {'Tiempo (ms)':<14} | {'Comparaciones':<15} | {'Movimientos'}")
            print("-" * 64)
            for _, (nombre, funcion) in algoritmos.items():
                inicio = time.perf_counter()
                _, comp, mov = funcion(numeros, mostrar_pasos=False)
                fin = time.perf_counter()
                t_ms = (fin - inicio) * 1000
                print(f"{nombre:<14} | {t_ms:<14.6f} | {comp:<15} | {mov}")
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()