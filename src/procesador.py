import csv

class Analizador:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.datos = self._leer_archivo()
    
    def _leer_archivo(self):
        """Método privado para leer el archivo CSV y almacenar los datos"""
        datos = []
        with open(self.archivo_csv, mode='r', encoding='latin-1') as file:
            lector = csv.DictReader(file)
            for fila in lector:
                datos.append(fila)
        return datos
    
    def ventas_totales_por_provincia(self):
        """Retorna un diccionario con el total de ventas agrupado por provincia"""
        ventas_por_provincia = {}
        
        for fila in self.datos:
            provincia = fila['PROVINCIA']

            # Descartar los registros que digan "ND"
            if provincia == "ND":
                continue

            venta = float(fila['TOTAL_VENTAS'])
            
            if provincia in ventas_por_provincia:
                ventas_por_provincia[provincia] += venta
            else:
                ventas_por_provincia[provincia] = venta
                
        return ventas_por_provincia
    
    def ventas_por_provincia(self, nombre_provincia):
        """Retorna el total de ventas de una provincia específica"""
        venta_total = 0.0
        
        for fila in self.datos:
            if fila['PROVINCIA'].lower() == nombre_provincia.lower():
                venta_total += float(fila['TOTAL_VENTAS'])
                
        return venta_total