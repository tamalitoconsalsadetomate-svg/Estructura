# Estructura
Estructura de datos 3SA
------EJER - ARREGLOS-------
Este programa es un sistema de ventas de un supermercado que utiliza un arreglo bidimensional (meses, departamentos) de 3*12. Cada espacio guarda un monto ganado por mes en x departamento. Se compone de 6 partes:
**Control**: Es la clase que construye los demás métodos. Se ejecuta al crear un objeto, inicializa la matriz y define las listas.
**Indices**: Crea los punteros para buscar cada cosa que se pide, toma el texto que el usuario escribe y verifica que el departamento y el mes existen realmente, convierte eso en índices y devuelve los pares correspondientes.
**Insertar_ventas**: Es el método que actualiza la matriz. Comprueba que el monto a ingresar no es negativo, verifica con el método índices dónde debe ser insertado, convierte el valor y lo guarda en su posición correspondiente.
**Buscar_venta**: Es el método de consulta. Solicita las coordenadas a índices, busca la posición correspondiente y muestra lo que buscaste y lo regresa.
**eliminar_venta**: que es el método de eliminación, no borra como tal la celda, sino que más bien reinicia el valor, contiene las coordenadas con índices, guarda provisionalmente el valor para mostrarlo al usuario y asigna nuevamente 0.0 a la celda y, por último, un método de mostrar la matriz. Imprime una cabecera con los meses abreviados (Ene, Feb, Mar...) y luego recorre fila por fila la matriz mostrando el nombre del departamento junto a sus 12 montos alineados.
**mostrar_tabla**:Es el método que visualiza y muestra al usuario todo lo hecho por el programa anteriormente.
