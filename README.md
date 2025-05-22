# Docker Microservicios

<!-- [TODO] agregar descripción --> 

## Estructura del proyecto

Este repositorio contiene los siguientes directorios y archivos:

```bash
    ├── cliente                              # componente GUI que funciona como cliente
    ├── gestor-de-clientes                   # microservicio gestor de clientes
    ├── docs                                 # carpeta de documentación
    │  ├── context-view.png                  # vista del contexto del sistema
    │  ├── global-assurance.drawio           # archivo editable de daiagramas del sistema 
    ├── notificador                          # microservicio notificador 
    ├── pagos                                # microservicio pagos
    ├── reporteador                          # microservicio reporteador
    ├── simulador                            # componente que simula los pagos realizados
    ├── tyk                                  # archivos compartidos con el gateway
    │  ├── apps                              # definición de APIs en el gateway
    │  |  ├── keyless-gestor-clientes.json   # definición de microservicio API
    │  |  ├── keyless-notificador.json       # definición de microservicio Notifier
    │  |  ├── keyless-pagos.json             # definición de microservicio Payment
    │  |  ├── keyless-reporteador.json       # definición de microservicio Reporter
    │  ├── tyk.standalone.conf               # archivo de configuración de tyk
    ├── .gitignore                           # exclusiones de git
    ├── docker-compose.yml                   # definición de contenedores para ambiente docker
    ├── README.md                            # este archivo
```

## Ejecución

Abrimos nuestro bot de telegram
`https://t.me/ChatBotArquitectura_bot`

Descarga el código del repositorio utilizando el siguiente comando:

`git clone https://github.com/JPflores20/Tarea-Patron-Microservicios.git`

Ingresa a la carpeta del proyecto:

`cd docker-microservicios`

Construimos los contenedores
`docker-commpose build -d`

Iniciamos los contenedores
`docker-commpose up -d`

Ingresamos al localhost
`http://localhost/`

Añadimos clientes para que se cree la base de datos
(Presionamos el boton de añadir cliente)

       --- Opcional podemos ingresar al puerto "8003/records" para ver que se esté ejecutando correctamente la base
       --- http://localhost:8003/records

Esperamos unos momentos a que se cree el archivo .json (se puede visualizar siguiendo el paso opcional)

Abrimos un cliente, verificamos el historial de pagos 

Enviamos una notificacion a nuestro bot en telegram para confirmar

Para detener el sistema utiliza el siguiente comando:

`docker-compose down`




### ¿Necesito instalar Docker?

Por supuesto, la herramienta Docker es vital para la ejecución de este sistema. Para conocer más acerca de Docker puedes visitar el siguiente [enlace](https://medium.com/@javiervivanco/que-es-docker-79d506f7b2fc).

> Para realizar la instalación de Docker en Windows puedes consultar el siguiente [enlace](https://medium.com/@tushar0618/installing-docker-desktop-on-window-10-501e594fc5eb)


> Para realizar la instalación de Docker en Linux puedes consultar el siguiente [enlace](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-es)

## Versión

3.0.1 - Mayo 2025

## Autores

- Perla Velasco
- Yonathan Martinez
- Jorge Solis"# Tarea-Patron-Microservicios" 
