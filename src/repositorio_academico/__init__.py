"""Clases del avance inicial del Repositorio Web Académico."""

from .curso import Curso
from .consola import AplicacionConsola
from .recurso import Recurso
from .repositorio import RepositorioAcademico
from .usuario import Administrador, Estudiante, Usuario

__all__ = [
    "Administrador",
    "AplicacionConsola",
    "Curso",
    "Estudiante",
    "Recurso",
    "RepositorioAcademico",
    "Usuario",
]
