import requests
from bs4 import BeautifulSoup
import time

def obtener_reproducciones(youtube_link):
    try:
        response = requests.get(youtube_link)
        response.raise_for_status()  # Lanza un error si la solicitud falló

        # Analizar el contenido HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscar el elemento que contiene el número de reproducciones
        views = soup.find("meta", itemprop="interactionCount")['content']
        return views
    except Exception as e:
        print(f"Error al obtener datos: {e}")
        return None

def main():
    youtube_link = input("Ingresa el enlace de YouTube: ")
    
    while True:
        reproducciones = obtener_reproducciones(youtube_link)
        if reproducciones is not None:
            print(f"Número de reproducciones: {reproducciones}")
        else:
            print("No se pudo obtener el número de reproducciones.")
        
        # Esperar 60 segundos antes de actualizar
        time.sleep(60)

if __name__ == "__main__":
    main()
