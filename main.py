"""Demostración del primer avance del Repositorio Web Académico."""

from src.repositorio_academico import Curso, Estudiante, Recurso, RepositorioAcademico


def main():
    repositorio = RepositorioAcademico("Repositorio Web Académico UNSCH")

    curso_poo = Curso("IS-282", "Programación Orientada a Objetos")
    repositorio.registrar_curso(curso_poo)

    estudiante = Estudiante(
        "U001",
        "20251001",
        "ana.quispe@unsch.edu.pe",
        "clave-demo",
        4,
    )
    repositorio.registrar_usuario(estudiante)

    recurso = Recurso(
        "R001",
        "Ejemplo de herencia simple",
        "Código de apoyo para practicar super() y sobrescritura.",
        estudiante,
        curso_poo,
        "Código",
        "herencia_simple.py",
        0.4,
    )

    publicado = repositorio.publicar_recurso(recurso)

    print(f"{repositorio.nombre}\n")
    print(f"Usuario registrado: {estudiante.nombre_completo} ({estudiante.obtener_rol()})")
    print(f"Recurso publicado: {'Sí' if publicado else 'No'}")
    print("\nResultados de búsqueda para 'herencia':")

    for resultado in repositorio.buscar_recursos("herencia"):
        print(f"- {resultado.titulo} | {resultado.curso.codigo} | {resultado.nombre_archivo}")


if __name__ == "__main__":
    main()
