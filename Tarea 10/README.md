# service mesh
## ¿Qué es Service Mesh?
Un service mesh es una infraestructura dedicada que se añade a las aplicaciones distribuidas,
como microservicios, para agregar capacidades como ges+ón de tráfico, observabilidad y
seguridad sin modificar el código de la aplicación.

## ¿que es chocolatey?
gestor de paquetes para Windows que permite instalar y actualizar aplicaciones de forma automatizada. Es similar a los gestores de paquetes de GNU/Linux, como pacman, yum, aptitude, o apt-get

## Instalación de minikube
minikube start --cpus 6 --memory 8192 --vm-driver=virtualbox
Estos parámetros son necesarios debido a la cantidad de pods,
si no tienen estos recursos es probable que el proyecto no funcione correctamente
## Elegimos la versión y descargamos
https://github.com/istio/istio/tags
## Descomprimimos la carpeta
Entramos a la carpeta y copiamos la ruta donde se encuentra el directorio bin:
C:\Users\Usuario\Documents\istio-1.10.2\bin

## Luego ingresar a la variables de entorno de Windows y en el path colocamos la ruta anterior.
Es recomendable colocar en las variables del sistema y del usuario
## Instalación de Chocolatey
https://chocolatey.org/install
## Instalación de istioctl en la consola de Windows
choco install istioctl
## Comprobacion del funcionamiento de minikube
kubectl get ns
Aparecerán los que vienen en nuestro cluster de minikube
## Instalación del namespace de istio
istioctl install
## Instalación del proyecto, usaremos el siguiente repositorio
https://github.com/GoogleCloudPlatform/microservices-demo
## Descargaremos el archivo kubernetes-manifests.yaml y lo incluiremos en nuestra carpeta de istio
que descomprimimos anteriormente
## Deploy del archivo kubernetes-manifests.yaml
En la consola entraremos a la carpeta de istio y usaremos el comando
kubectl apply -f kubernetes-manifests.yaml
Así se comenzará a crear los microservicios que vienen programados
## Para comprobar que se crearon los pods usaremos
kubectl get pod
Ahora solo falta los proxy que harán de intermediarios entre pods, entonces primero usaremos
kubectl get ns default --show-labels
y veremos que solo tenemos un perfil default, nos falta el de istio Con el comando
kubectl label namespace default istio-injection=enabled
Podremos realizar la injección de los proxy que necesitamos
Para eso tendremos que borrar los pods con el comando
kubectl delete -f kubernetes-manifests.yaml
y esperar a que los procesos finalicen

## Repetimos el comando
kubectl apply -f kubernetes-manifests.yaml
y ahora nos saldrá 2 procesos por servicio, esto nos quiere decir que nuestro servicios están
correctos

## Visualización de los servicios
En la ruta C:\Users\Usuario\Documents\istio-1.10.2\samples\addons (donde tenemos la carpeta de istio)
Usando el comando kubectl apply -f kiali.yaml (por ejemplo) para levantar el servicio de visualización de tráfico
Y hacer lo mismo con los demás servicios que vienen en la carpeta addons, se recomienda hacer uno por uno

## Verificación
Con el comando kubectl get pod -n istio-system
Veremos que nuestros servicios ya están listos
Ahora con el comando
kubectl get svc -n istio-system
Veremos los servicios, con sus respectivas ip y puertos asignados
## Para terminar usaremos el comando
kubectl port-forward svc/kiali -n istio-system 20001
Y se iniciará el servicio de kiali, ingresaremos de 2 formas
localhost:20001 o 127.0.0.1:20001
Y ya podríamos ver nuestra práctica completa
Tener en cuenta que este proyecto es exigente en recursos para nuestro pc
Así que los pods pueden reiniciarse varias veces pero siempre regresarán a la normalidad de manera automática
