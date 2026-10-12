# Repositorio Web Académico - UNSCH

Avance inicial del proyecto final de **Programación Orientada a Objetos (IS-282)**. El sistema modela un repositorio académico donde estudiantes de Ingeniería de Sistemas pueden publicar y buscar materiales de curso.

## Alcance de este avance

Esta primera entrega es una aplicación de consola enfocada en los temas vistos hasta herencia:

- Clases y objetos: `Usuario`, `Curso`, `Recurso` y `RepositorioAcademico`.
- Encapsulamiento: atributos internos y propiedades de solo lectura.
- Herencia simple: `Estudiante` y `Administrador` heredan de `Usuario` mediante `super()`.
- Sobrescritura: cada tipo de usuario informa su propio rol.
- Reglas iniciales: correo institucional, usuarios activos, formatos permitidos y límite de 20 MB.
- Publicación y búsqueda básica de recursos en memoria.

No incluye todavía una interfaz web, base de datos, carga física de archivos, calificaciones ni moderación completa. Esas funciones se implementarán en las siguientes etapas del curso.

## Estructura

```text
.
├── docs/                     # Alcance y plan del avance
├── src/repositorio_academico/ # Clases del dominio
├── tests/                    # Pruebas automatizadas
├── main.py                   # Demostración ejecutable
└── README.md
```

## Requisitos

- Python 3.10 o superior.
- No se requieren dependencias externas.

## Ejecución

Desde la carpeta raíz del proyecto:

```bash
python3 main.py
```

## Pruebas

```bash
python3 -m unittest discover -s tests -v
```

## Equipo

Reemplacen los espacios antes de la entrega final:

| Integrante | Responsabilidad inicial |
| --- | --- |
| Integrante 1 | Modelo de usuarios y autenticación |
| Integrante 2 | Recursos, cursos y reglas de publicación |
| Integrante 3 | Pruebas, documentación e integración |

## Próximos pasos

1. Guardar usuarios y recursos en archivos JSON.
2. Incorporar calificaciones y reportes de recursos.
3. Completar las relaciones UML y la moderación administrativa.
4. Desarrollar una interfaz web responsive.
