import math

def calcular_distancia(x1, y1, x2, y2):
    """
    Calcula la distancia entre dos puntos (x1, y1) y (x2, y2).
    Valida que los parámetros sean números.
    """
    if not (isinstance(x1, (int, float)) and isinstance(y1, (int, float)) and 
            isinstance(x2, (int, float)) and isinstance(y2, (int, float))):
        raise ValueError("Todos los parámetros deben ser números.")
    
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

def validar_entrada(valor, tipo):
    """
    Valida que el valor sea del tipo especificado.
    """
    if not isinstance(valor, tipo):
        raise ValueError(f"El valor {valor} no es del tipo {tipo}.")

def validar_archivo_existe(ruta):
    """
    Valida que el archivo en la ruta especificada exista.
    """
    import os
    if not os.path.isfile(ruta):
        raise FileNotFoundError(f"El archivo en la ruta {ruta} no existe.")

# Ejemplo de uso
if __name__ == "__main__":
    try:
        validar_entrada(10, int)
        print("Validación de entero exitosa.")
        
        distancia = calcular_distancia(0, 0, 3, 4)
        print(f"La distancia es: {distancia}")
        
        validar_archivo_existe("README.md")
        print("El archivo README.md existe.")
        
    except (ValueError, FileNotFoundError) as e:
        print(e)
