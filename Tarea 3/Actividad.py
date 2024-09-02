import pickle

def guardar_estado(contador, nombre_archivo):
    with open(nombre_archivo, 'wb') as archivo:
        pickle.dump(contador, archivo)
    print(f"Estado guardado en {nombre_archivo}")

def cargar_estado(nombre_archivo):
    try:
        with open(nombre_archivo, 'rb') as archivo:
            contador = pickle.load(archivo)
        print(f"Estado cargado desde {nombre_archivo}")
        return contador
    except FileNotFoundError:
        print(f"No se encontró el archivo {nombre_archivo}. Iniciando con contador en 0.")
        return 0
    except Exception as e:
        print(f"Error al cargar el estado: {e}")
        return 0

def main():
    nombre_archivo = 'estado_contador.pkl'
    contador = cargar_estado(nombre_archivo)
    
    while True:
        print(f"Contador actual: {contador}")
        accion = input("Ingrese 'a' para aumentar, 's' para salir: ").strip().lower()
        if accion == 'a':
            contador += 1
        elif accion == 's':
            guardar_estado(contador, nombre_archivo)
            break
        else:
            print("Acción no reconocida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
