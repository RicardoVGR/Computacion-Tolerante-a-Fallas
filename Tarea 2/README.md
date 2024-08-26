# EJEMPLO: Otras herramientas para el manejo de errores 
### Valdivia Guerra Ricardo Emmanuel.
### Computación Tolerante a Fallas.
# Desarrollo ##
## Instalación de Airbrake
instalamos utilizando el comando de windows
```bash
pip install airbrake-python
```
## Utilizacion en python
Después de instalar la biblioteca, debes configurarla con tu clave de proyecto y otros parámetros dados por Airbreake
```python
import airbrake
# Configura Airbrake con tu Project ID y Project Key
airbrake.configure(project_id=123456,project_key='your_project_key_here')
# Otras configuraciones opcionales
airbrake.set_environment('production')  # Define el entorno (producción, desarrollo, etc.)
```
## Captura de Excepciones con Airbrake
```python
import airbrake
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        airbrake.notify(e) # Notificar el error a Airbrake
        # También puedes registrar el error o manejarlo como desees
        print("Error: División por cero no permitida.")
# Ejemplo de uso
result = divide(10, 0)
```
Notificado el error lo mostrara en su pagina marcando parametros y estadisticas 
![texto](https://gdm-catalog-fmapi-prod.imgix.net/ProductScreenshot/2635bea5-0442-48fa-956f-3d7b791790ea.png?auto=format&q=50)
