import random
import time


class Frijoles:

    def __init__(self, num_alumnos, num_materias):
        self.num_alumnos = num_alumnos
        self.num_materias = num_materias

    def Genraralumnos(self):
        return [
            [
                round(random.uniform(5.0, 10.0), 2)
                for _ in range(self.num_materias)
            ]
            for _ in range(self.num_alumnos)
        ]

    def Generarmaterias(self):
        return [
            [
                round(random.uniform(5.0, 10.0), 2)
                for _ in range(self.num_alumnos)
            ]
            for _ in range(self.num_materias)
        ]

    def Buscarcalificacionalumnos(self, matriz, id_alumno, id_materia):
        inicio = time.perf_counter_ns()
        calificacion = matriz[id_alumno][id_materia]
        fin = time.perf_counter_ns()
        tiempo = fin - inicio
        return calificacion, tiempo

    def buscar_calificacion_materias_primero(self, matriz, id_alumno, id_materia):
        inicio = time.perf_counter_ns()
        calificacion = matriz[id_materia][id_alumno]
        fin = time.perf_counter_ns()
        tiempo_ns = fin - inicio
        return calificacion, tiempo_ns

    def mostrar_matriz_completa(self, matriz, titulo):
        print("\n" + "=" * 70)
        print(f" MATRIZ COMPLETA: {titulo}")
        print("=" * 70)
        for i, fila in enumerate(matriz):
            valores_str = " | ".join(f"{nota:5.2f}" for nota in fila)
            print(f"Fila [{i:3d}]:  [ {valores_str} ]")
        print("=" * 70)



def Ejecutar():
    num_alumnos = 500
    num_materias = 6
    evaluador = Frijoles(num_alumnos=num_alumnos, num_materias=num_materias)
    matrizalumnos = evaluador.Genraralumnos()
    matrizmaterias = evaluador.Generarmaterias()
    evaluador.mostrar_matriz_completa( matrizalumnos, titulo=f"Estructura [Alumno][Materia] ({num_alumnos} Alumnos x {num_materias} Materias)",)
    evaluador.mostrar_matriz_completa(matrizmaterias, titulo=f"Estructura [Materia][Alumno] ({num_materias} Materias x {num_alumnos} Alumnos)",)
    alumnopueba, materiaprueba = 320, 4
    cal1, tiempo1 = evaluador.Buscarcalificacionalumnos(matrizalumnos, alumnopueba, materiaprueba)
    cal2, tiempo2 = evaluador.buscar_calificacion_materias_primero(matrizmaterias, alumnopueba, materiaprueba)
    print(f"Estructura 1 [Alumno][Materia]  -> Calificacion: {cal1:.2f} | Tiempo: {tiempo1} ns" )
    print(f"Estructura 2 [Materia][Alumno]  -> Calificacion: {cal2:.2f} | Tiempo: {tiempo2} ns")
    
Ejecutar()