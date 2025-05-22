# Reporteador

Microservicio responsable de generar los documentos de las pólizas de seguro

## Estructura del proyecto

Este repositorio contiene los siguientes directorios y archivos:

```bash
    ├── src                          # código fuente
    │  ├── controllers               # lógica del microservicio 
    │  |  ├── __init__.py            # indica la definición de modulo python
    │  |  ├── policy_controller.py   # logica del controlador de polizas
    │  ├── helpers                   # funciones auxiliares del microservicio
    │  |  ├── __init__.py            # indica la definición de modulo python
    │  |  ├── processor.py           # archivo auxiliar para procesar la plantilla de la póliza
    │  ├── __init__.py               # indica la definición de modulo python
    │  ├── application.py            # definición de rutas del microservicio
    ├── templates                    # definición de plantillas de polizas
    │  ├── template-policy.docx      # plantilla de póliza
    ├── tests                        # definición de pruebas del microservicio
    │  ├── __init__.py               # indica la definición de modulo python
    │  ├── test_report.py            # definición de pruebas del controlador policy
    ├── Dockerfile                   # definición de comandos docker del microservicio 
    ├── main.py                      # archivo principal de ejecución
    ├── .gitignore                   # exclusiones de git
    ├── README.md                    # este archivo
    ├── requirements.txt             # depencias del microservicio
```



## Versión

3.0.1 - Mayo 2025

## Autores

- Perla Velasco
- Yonathan Martinez
- Jorge Solis