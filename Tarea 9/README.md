## Actividad Failure Injection
### ¿que es?
Es una técnica que introduce fallos en un sistema con el propósito de evaluar su resistencia, comportamiento y capacidad de recuperación frente a errores.
### ¿Cómo funciona?
Se inyectan errores en diferentes niveles del sistema
#### -Fallos en hardware: Por ejemplo, desconectar dispositivos, simular cortes de energía, o fallos de red.
#### -Errores de software: Introducir excepciones o comportamientos anómalos en funciones o componentes específicos.
#### -Fallos en servicios externos: Simular que servicios externos están inaccesibles, responden con errores o tienen alta latencia.
#### -Datos corruptos o inválidos: Proveer al sistema datos incorrectos o inesperados.
### Ejemplos
#### Chaos Engineering: Popularizado por herramientas como Chaos Monkey de Netflix, que se utiliza para causar fallos aleatorios en entornos de producción.
#### Gremlin: Herramienta para diseñar y ejecutar experimentos de inyección de fallos.
#### AWS Fault Injection Simulator (FIS): Proporciona capacidades para simular fallos en entornos basados en AWS.
### Ejemplo utilizando chaos toolkit
intalar chaostoolkit y extensiones específicas para Kubernetes
```python
pip install chaostoolkit
pip install chaostoolkit-kubernetes
```
```python
{
  "version": "1.0.0",
  "title": "Simular la eliminación de un pod crítico en Kubernetes",
  "description": "Este experimento elimina un pod para observar cómo responde el sistema.",
  "tags": ["kubernetes", "resiliencia", "chaos"],
  "steady-state-hypothesis": {
    "title": "El sistema debe mantenerse estable",
    "probes": [
      {
        "type": "probe",
        "name": "check_service_availability",
        "provider": {
          "type": "http",
          "timeout": 5,
          "url": "http://mi-servicio/health",
          "method": "GET"
        },
        "tolerance": {
          "type": "jsonpath",
          "path": "$.status",
          "expect": "healthy"
        }
      }
    ]
  },
  "method": [
    {
      "type": "action",
      "name": "delete_pod",
      "provider": {
        "type": "python",
        "module": "chaosk8s.pod.actions",
        "func": "delete_pod",
        "arguments": {
          "name": "mi-pod-crucial",
          "namespace": "mi-namespace"
        }
      }
    }
  ],
  "rollbacks": [
    {
      "type": "action",
      "name": "reinstate_pod",
      "provider": {
        "type": "python",
        "module": "chaosk8s.pod.actions",
        "func": "create_pod",
        "arguments": {
          "name": "mi-pod-crucial",
          "namespace": "mi-namespace",
          "manifest_path": "./pod-definition.yaml"
        }
      }
    }
  ]
}
```
Ejecuta Chaos Toolkit
```python
chaos runkubernetes.json
```

