class Cntrol:
    def __init__(self):
        self.departamentos=["Ropa", "Deportes", "Jugueteria"]
        self.meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        self.matriz_ventas=[[0.0 for _ in range (12)] for _ in range (3)]

    def indices(self,departamento,mes):
        dep_clean= departamento.strip().capitalize()
        mes_clean=mes.strip().capitalize()
        if dep_clean not in self.departamentos:
            print("Error")
            return None, None
        if mes_clean not in self.meses:
            print("Error")
            return None,None
        fila=self.departamentos.index(dep_clean)
        columna=self.meses.index(mes_clean)
        return fila,columna

    def insertar_venta(self,departamento,mes,monto):
        if monto < 0:
            print("El monto no uede ser negeativo")
            return
        fila,col=self.indices(departamento,mes)
        if fila is not None and col is not None:
            self.matriz_ventas[fila][col] = float(monto)
            print(f" Venta registrada exitosamente: {self.departamentos[fila]} en {self.meses[col]} -> ${monto:,.2f}")

    def buscar_venta(self,departamento,mes):
        fila,col=self.indices(departamento,mes)
        if fila is not None and col is not None:
            monto=self.matriz_ventas[fila][col]
            print(f" Buscando venta... {self.departamentos[fila]} - {self.meses[col]}: ${monto:,.2f}")
            return monto

    def eliminar_venta(self,departamento,mes):
        fila,col=self.indices(departamento,mes)
        if fila is not None and col is not None:
            venta_anterior=self.matriz_ventas[fila][col]
            self.matriz_ventas[fila][col]=0.0
            print(f" Venta eliminada de {self.departamentos[fila]} ({self.meses[col]}). Registro anterior: ${venta_anterior:,.2f}")

    def mostrar_tabla(self):
        """Método adicional para visualizar toda la matriz en formato tabla."""
        print("\n" + "="*85)
        print("REPORTE GENERAL DE VENTAS MENSUALES".center(85))
        print("="*85)
        header = f"{'Departamento':<15} | " + " | ".join([m[:3] for m in self.meses])
        print(header)
        print("-" * len(header))
        for i, dep in enumerate(self.departamentos):
            fila_str = f"{dep:<15} | " + " | ".join([f"{val:>5.0f}" for val in self.matriz_ventas[i]])
            print(fila_str)
        print("="*85 + "\n")



sistema = Cntrol()

print("--- 1. Insertando Ventas ---")
sistema.insertar_venta("Ropa", "Enero", 15000)
sistema.insertar_venta("Deportes", "Febrero", 23000.50)
sistema.insertar_venta("Jugueteria", "Diciembre", 50000)


sistema.mostrar_tabla()

    
print("--- 2. Buscando Ventas ---")
sistema.buscar_venta("Deportes", "Febrero")
sistema.buscar_venta("Ropa", "Marzo") 

  
print("\n--- 3. Eliminando Ventas ---")
sistema.eliminar_venta("Deportes", "Febrero")
sistema.mostrar_tabla()