"""Punto de entrada del Repositorio Web Académico en modo consola."""

from src.repositorio_academico import AplicacionConsola, RepositorioAcademico


def main():
    repositorio = RepositorioAcademico("Repositorio Web Académico UNSCH")
    AplicacionConsola(repositorio).iniciar()


if __name__ == "__main__":
    main()
