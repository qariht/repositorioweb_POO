# Avance 02 - Gestión interactiva por consola

## Propósito

Entregar una aplicación de consola ejecutable y verificable del Repositorio Web Académico antes de incorporar persistencia, interfaz web y funcionalidades avanzadas.

## Conceptos aplicados

| Concepto visto | Aplicación en el avance |
| --- | --- |
| Clase y objeto | `Usuario`, `Estudiante`, `Administrador`, `Curso`, `Recurso` y `RepositorioAcademico`. |
| Constructor | Todas las clases inicializan su estado mediante `__init__`. |
| Encapsulamiento | La contraseña se guarda como atributo privado; las colecciones se exponen como tuplas. |
| Herencia simple | `Estudiante` y `Administrador` extienden a `Usuario`. |
| `super()` | Las subclases reutilizan la inicialización común de `Usuario`. |
| Sobrescritura | `obtener_rol()` cambia según el tipo de usuario. |

## Funcionalidades demostrables

1. Registrar usuarios institucionales con correo `@unsch.edu.pe`.
2. Autenticar usuarios activos.
3. Registrar cursos.
4. Publicar recursos de estudiantes registrados.
5. Validar extensiones `.py`, `.tex`, `.pdf` y `.zip` y el límite de 20 MB.
6. Buscar recursos publicados por texto o código de curso.
7. Bloquear usuarios desde un administrador.
8. Usar menús distintos para estudiante y administrador después del inicio de sesión.

## Límites intencionales

El estado se conserva solo mientras el programa está abierto. La carga real de archivos, JSON, relaciones UML completas, calificaciones, reportes, moderación detallada y la interfaz web se desarrollarán cuando correspondan a los temas posteriores del curso.

## Reparto sugerido para tres integrantes

| Integrante | Tarea para la siguiente iteración |
| --- | --- |
| 1 | Persistencia en JSON de usuarios, cursos y recursos. |
| 2 | Clases de calificación, reporte y moderación. |
| 3 | Menú de consola, pruebas adicionales y actualización del UML. |
